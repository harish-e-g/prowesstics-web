import cv2, numpy as np, json
SRC="Ladera_JKFenner_Smart_Line_Film_1080p.mp4"  # partner source cut, see README
cap=cv2.VideoCapture(SRC); fps=cap.get(cv2.CAP_PROP_FPS)
def grab(t):
    cap.set(cv2.CAP_PROP_POS_MSEC, t*1000); ok,f=cap.read(); return f
R={"title":(789,360,1131,463,3.5),"end":(752,355,1168,483,119.5),"bug":(1723,1004,1876,1077,30)}
T={}
for k,(x0,y0,x1,y1,t) in R.items():
    f=grab(t); T[k]=cv2.cvtColor(f[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY); cv2.imwrite(f"tpl_{k}.png",f[y0:y1,x0:x1])
cap.set(cv2.CAP_PROP_POS_FRAMES,0)
scores={k:[] for k in R}; i=0
while True:
    ok,f=cap.read()
    if not ok: break
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    for k,(x0,y0,x1,y1,_) in R.items():
        roi=g[max(0,y0-4):min(1080,y1+4), x0-4:x1+4]
        s=cv2.matchTemplate(roi,T[k],cv2.TM_CCOEFF_NORMED).max()
        scores[k].append(round(float(s),3))
    i+=1
json.dump({"fps":fps,"scores":scores},open("scores.json","w"))
print(i, fps)
for k in R:
    s=np.array(scores[k]); 
    line=''.join(' ' if v<0.2 else '.' if v<0.4 else 'o' if v<0.6 else '#' for v in s[::12])
    print(k, line)
