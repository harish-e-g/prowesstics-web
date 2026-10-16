"""Universal edit of the Smart Assembly film: company logos, no client name anywhere on screen,
universal subtitle and end line. Output video only (audio handled afterwards)."""
import cv2, numpy as np, json, subprocess, sys
from textfx import remove_text, draw_text
SRC="Ladera_JKFenner_Smart_Line_Film_1080p.mp4"  # partner source cut, see README
OUT=sys.argv[1] if len(sys.argv)>1 else "film_u_video.mp4"
ONLY=None if len(sys.argv)<3 else set(int(x) for x in sys.argv[2].split(","))
FPS=24
SEMI="/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"; MED="/usr/share/fonts/opentype/inter/Inter-Medium.otf"
E={k:np.array(v) for k,v in json.load(open("alpha.json")).items()}; n=len(E["bug"]); t=np.arange(n)/FPS
def boost(x,floor): return np.where(x>floor,np.clip(x*1.8,0,1),0)
A={"title":np.where(t<7,np.where((t>1.2)&(t<6.2),boost(E["title"],0.05),boost(E["title"],0.12)),0),"end":np.where(t>117.2,boost(E["end"],0.12),0)}
on=np.where((E["bug"]>0.5)&(t>5))[0]; ab=np.zeros(n); ab[on.min():on.max()+1]=1; A["bug"]=ab
OV={}; BOX={"title":(772,350,1148,473),"end":(738,343,1182,495),"bug":(1710,996,1888,1080)}
for k in BOX:
    o=cv2.imread(f"ov_{k}.png",cv2.IMREAD_UNCHANGED); x0,y0,x1,y1=BOX[k]; o=o[y0:y1,x0:x1].astype(np.float32); OV[k]=(o[...,:3],o[...,3:4]/255)
# subtitle / end-line text alpha follows the title / end card
TA=np.clip(E["title"],0,1)*(t<7); EA=np.clip(E["end"],0,1)*(t>117.2)
# --- client-name detections, interpolated across short gaps
D={int(k):v for k,v in json.load(open("detect.json")).items()}
def label_box(ws):
    jk=[w for w in ws if w[0].strip("()").upper()=="JK"]; fe=[w for w in ws if w[0].upper().startswith("FENNER") and w[2]<650]
    pl=[w for w in ws if w[0].upper()=="PLC"]
    if not fe and not jk: return None
    h=max([w[4] for w in fe+jk+pl if w[4]<40] or [10])
    ys=[w[2] for w in fe+jk+pl]
    if fe: f=fe[0]; x0=jk[0][1] if jk else f[1]-int(f[3]*0.42); x1=(pl[0][1]+pl[0][3]) if pl else f[1]+int(f[3]*1.62)
    else: j=jk[0]; x0=j[1]; x1=j[1]+int(j[3]*5.6)
    y=min(ys); return [x0,y,x1,y+h]
def jkf_box(ws):
    j=[w for w in ws if w[0].upper()=="JKF"]
    return [j[0][1],j[0][2],j[0][1]+j[0][3],j[0][2]+j[0][4]] if j else None
def series(fn, lo, hi):
    pts={i:fn(D[i]) for i in D if lo<=i/FPS<=hi and D.get(i)}
    pts={i:b for i,b in pts.items() if b}
    keys=sorted(pts); res={}
    for i in range(int(lo*FPS),int(hi*FPS)+1):
        if i in pts: res[i]=pts[i]; continue
        prv=[k for k in keys if k<i and i-k<=8]; nxt=[k for k in keys if k>i and k-i<=8]
        if prv and nxt:
            a,b=prv[-1],nxt[0]; w=(i-a)/(b-a); res[i]=[int(pts[a][m]*(1-w)+pts[b][m]*w) for m in range(4)]
        elif prv and i-prv[-1]<=3: res[i]=pts[prv[-1]]
        elif nxt and nxt[0]-i<=3: res[i]=pts[nxt[0]]
    return res
LAB={}; [LAB.update(series(label_box,a,b)) for a,b in [(5.1,9.2),(102.8,106.3),(112.9,115.2)]]
JKF=series(jkf_box,24.5,26.7)
# engraved "JKF" prefix on the pulley rim (frames 594-639): tracked box, then the dark letters are inpainted
TRK={int(k):v for k,v in json.load(open("jkf_track.json")).items()}
ENG={i:TRK[i][1:] for i in range(606,638)}
xs=np.polyfit(range(606,617),[TRK[i][1] for i in range(606,617)],1); ys=np.polyfit(range(606,617),[TRK[i][2] for i in range(606,617)],1)
for i in range(594,606): ENG[i]=[int(round(np.polyval(xs,i))),int(round(np.polyval(ys,i))),TRK[606][3],TRK[606][4]]
for i in range(638,641): ENG[i]=TRK[637][1:] if 637 in TRK else TRK[636][1:]
def erase_engraving(f,b):
    x,y,w,h=b; X0,Y0,X1,Y1=x-4,y-3,x+w+3,y+h+3; roi=f[Y0:Y1,X0:X1]; g=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY).astype(np.int16)
    bg=cv2.medianBlur(g.astype(np.uint8),9).astype(np.int16); m=((bg-g)>14).astype(np.uint8)*255
    m=cv2.dilate(m,np.ones((3,3),np.uint8),iterations=2)
    if m.any(): f[Y0:Y1,X0:X1]=cv2.inpaint(roi,m,4,cv2.INPAINT_TELEA)
# fixed masks for the subtitle line and the end-card line
cap=cv2.VideoCapture(SRC)
def frame(i): cap.set(cv2.CAP_PROP_POS_FRAMES,i); return cap.read()[1]
def text_mask(f,box,thr):
    x0,y0,x1,y1=box; g=cv2.cvtColor(f[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY).astype(np.int16)
    bg=cv2.medianBlur(g.astype(np.uint8),31).astype(np.int16); m=((g-bg)>thr).astype(np.uint8)*255
    return cv2.dilate(m,np.ones((3,3),np.uint8),iterations=3)
SUBBOX=(540,678,1380,728); ENDBOX=(560,696,1360,734)
SUBM=text_mask(frame(72),SUBBOX,8); ENDM=text_mask(frame(2868),ENDBOX,6)
def inpaint_fixed(f,box,mask,strength):
    x0,y0,x1,y1=box; roi=f[y0:y1,x0:x1]; fixed=cv2.inpaint(roi,mask,7,cv2.INPAINT_TELEA)
    if strength>=0.999: f[y0:y1,x0:x1]=fixed
    else:
        m=(cv2.GaussianBlur(mask,(0,0),1.5)/255.0*strength)[...,None]; f[y0:y1,x0:x1]=(fixed*m+roi*(1-m)).astype(np.uint8)
def sign_clean(f):
    # navy fascia sign on the factory wall during the opening: inpaint any light lettering inside it
    hsv=cv2.cvtColor(f[150:420,900:1920],cv2.COLOR_BGR2HSV)
    navy=cv2.inRange(hsv,(100,90,40),(125,255,140))
    cnts,_=cv2.findContours(navy,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        x,y,w,h=cv2.boundingRect(c)
        if 120<w<700 and 18<h<90 and w/h>3 and cv2.contourArea(c)>0.6*w*h:
            X,Y=x+900+3,y+150+3; roi=f[Y:Y+h-6,X:X+w-6]
            g=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY); med=np.median(g)
            m=((g.astype(np.int16)-med)>18).astype(np.uint8)*255; m=cv2.dilate(m,np.ones((3,3),np.uint8),iterations=2)
            if m.any(): f[Y:Y+h-6,X:X+w-6]=cv2.inpaint(roi,m,3,cv2.INPAINT_TELEA)
def replace_label(f,b,text,fg,font,light=True):
    x0,y0,x1,y1=b; H,W=f.shape[:2]; pad=max(2,(y1-y0)//4)
    X0,Y0,X1,Y1=max(0,x0-pad),max(0,y0-pad),min(W,x1+pad),min(H,y1+pad)
    if X1-X0<4 or Y1-Y0<4: return
    reg=f[Y0:Y1,X0:X1]; g=cv2.cvtColor(reg,cv2.COLOR_BGR2GRAY)
    sel=g>=np.percentile(g,60) if light else g<=np.percentile(g,40)
    col=np.median(reg[sel],axis=0) if sel.any() else np.median(reg.reshape(-1,3),axis=0)
    f[Y0:Y1,X0:X1]=col.astype(np.uint8)
    h=y1-y0; size=max(6,int(round(h/0.72)))
    draw_text(f,text,(x0+x1)/2,(y0+y1)/2+h*0.02,size,color=fg,alpha=1,shadow=False,font=font)
cap=cv2.VideoCapture(SRC)
enc=None if ONLY else subprocess.Popen(["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","bgr24","-s","1920x1080","-r","24","-i","-",
    "-c:v","libx264","-preset","medium","-crf","22","-pix_fmt","yuv420p",OUT],stdin=subprocess.PIPE)
i=0
while True:
    ok,f=cap.read()
    if not ok: break
    if ONLY is None or i in ONLY:
        tt=i/FPS
        if tt<5.8: sign_clean(f)
        if 7<=i<=33:  # leftover frames of the spoken-name caption (the line itself is cut)
            m=np.zeros((100,320),np.uint8); m[18:78,40:280]=255; f[940:1040,800:1120]=cv2.inpaint(f[940:1040,800:1120],m,9,cv2.INPAINT_TELEA)
        if TA[i]>0.01: inpaint_fixed(f,SUBBOX,SUBM,min(1,TA[i]*1.6))
        if i in ENG: erase_engraving(f,ENG[i])
        if i in LAB: replace_label(f,LAB[i],"AUTOMATION",(58,52,46),SEMI)
        if i in JKF: replace_label(f,JKF[i],"PRW",(240,236,230),MED,light=False)
        if EA[i]>0.01: inpaint_fixed(f,ENDBOX,ENDM,min(1,EA[i]*1.6))
        for k in ("title","end","bug"):
            al=A[k][i]
            if al<=0.001: continue
            x0,y0,x1,y1=BOX[k]; rgb,alpha=OV[k]; a=alpha*al; roi=f[y0:y1,x0:x1].astype(np.float32); f[y0:y1,x0:x1]=(rgb*a+roi*(1-a)).astype(np.uint8)
        if TA[i]>0.01: draw_text(f,"Full-factory automation  ·  Digital traceability  ·  One Control Tower",960,704,27,alpha=float(TA[i]))
        if EA[i]>0.01: draw_text(f,"FULL-FACTORY AUTOMATION  ·  DIGITAL TRANSFORMATION",960,715,17,color=(160,178,205),alpha=float(EA[i]),spacing=3,shadow=False)
        if ONLY is not None: cv2.imwrite(f"u_{i}.png",f)
    if enc: enc.stdin.write(f.tobytes())
    i+=1
if enc: enc.stdin.close(); enc.wait()
print("done",i)
