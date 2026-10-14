import cv2, numpy as np, json
SRC="Ladera_JKFenner_Smart_Line_Film_1080p.mp4"  # partner source cut, see README
R={"title":(789,360,1131,463),"end":(752,355,1168,483),"bug":(1723,1004,1876,1077)}
T={k:cv2.cvtColor(cv2.imread(f"tpl_{k}.png"),cv2.COLOR_BGR2GRAY).astype(np.float32) for k in R}
Tz={k:(T[k]-T[k].mean()) for k in R}
cap=cv2.VideoCapture(SRC); A={k:[] for k in R}
while True:
    ok,f=cap.read()
    if not ok: break
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY).astype(np.float32)
    for k,(x0,y0,x1,y1) in R.items():
        r=g[y0:y1,x0:x1]; rz=r-r.mean(); t=Tz[k]
        A[k].append(round(float((rz*t).sum()/(t*t).sum()),3))
json.dump(A,open("alpha.json","w"))
for k in A:
    a=A[k]; print(k,'0-8:',' '.join(f'{v:.2f}' for v in a[0:192:4])); print(k,'112-120:',' '.join(f'{v:.2f}' for v in a[2688::4]))
