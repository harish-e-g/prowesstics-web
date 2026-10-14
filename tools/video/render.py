import cv2, numpy as np, json, subprocess
SRC="Ladera_JKFenner_Smart_Line_Film_1080p.mp4"  # partner source cut, see README
E=json.load(open("alpha.json")); E={k:np.array(v) for k,v in E.items()}; n=len(E["bug"]); fps=24
t=np.arange(n)/fps
def boost(x, floor): return np.where(x>floor, np.clip(x*1.8,0,1), 0)
A={"title":np.where(t<7, boost(E["title"],0.12), 0), "end":np.where(t>117.2, boost(E["end"],0.12), 0)}
b=E["bug"]; on=np.where((b>0.5)&(t>5))[0]; a_b=np.zeros(n); a_b[on.min():on.max()+1]=1; A["bug"]=a_b
print("bug on", on.min()/fps, on.max()/fps)
# frame windows only where the original logo is not present at all are skipped
OV={k:cv2.imread(f"ov_{k}.png",cv2.IMREAD_UNCHANGED) for k in A}
BOX={"title":(772,350,1148,473),"end":(738,343,1182,495),"bug":(1710,996,1888,1080)}
for k in OV:
    x0,y0,x1,y1=BOX[k]; o=OV[k][y0:y1,x0:x1].astype(np.float32); OV[k]=(o[...,:3], o[...,3:4]/255.0)
cap=cv2.VideoCapture(SRC)
enc=subprocess.Popen(["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","bgr24","-s","1920x1080","-r","24","-i","-","-i",SRC,
    "-map","0:v","-map","1:a","-c:v","libx264","-preset","medium","-crf","24","-profile:v","high","-pix_fmt","yuv420p",
    "-c:a","aac","-b:a","160k","-movflags","+faststart","-shortest","film_v3.mp4"],stdin=subprocess.PIPE)
i=0
while True:
    ok,f=cap.read()
    if not ok: break
    for k in ("title","end","bug"):
        al=A[k][i] if i<n else 0
        if al<=0.001: continue
        x0,y0,x1,y1=BOX[k]; rgb,alpha=OV[k]; alpha=alpha*al
        roi=f[y0:y1,x0:x1].astype(np.float32); f[y0:y1,x0:x1]=(rgb*alpha+roi*(1-alpha)).astype(np.uint8)
    enc.stdin.write(f.tobytes()); i+=1
enc.stdin.close(); enc.wait(); print("frames",i, "rc",enc.returncode)
