import cv2, pytesseract, re, json
from concurrent.futures import ProcessPoolExecutor
SRC="Ladera_JKFenner_Smart_Line_Film_1080p.mp4"  # partner source cut, see README
FPS=24
WIN=[(1.3,9.8),(23.8,27.2),(102.3,106.6),(112.3,115.6)]
def frames():
    cap=cv2.VideoCapture(SRC); i=0
    while True:
        ok,f=cap.read()
        if not ok: break
        t=i/FPS
        if any(a<=t<=b for a,b in WIN): yield i,f
        i+=1
def ocr(args):
    i,f=args; g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY); res=[]
    for sc in (2.0,3.0):
        gg=cv2.resize(g,None,fx=sc,fy=sc,interpolation=cv2.INTER_CUBIC)
        d=pytesseract.image_to_data(gg,output_type=pytesseract.Output.DICT,config="--psm 11")
        for k,w in enumerate(d["text"]):
            if re.fullmatch(r"(?i)\W*(jk|jkf|fenner|fenner\W.*|plc|\(india\)|india\)?|limited)\W*",w or ""):
                res.append([w,round(d["left"][k]/sc),round(d["top"][k]/sc),round(d["width"][k]/sc),round(d["height"][k]/sc)])
        if res: break
    return i,res
with ProcessPoolExecutor(2) as ex:
    out={i:r for i,r in ex.map(ocr,frames(),chunksize=4)}
json.dump(out,open("detect.json","w"))
hit=sorted(k for k,v in out.items() if v)
print(len(out),"frames scanned,",len(hit),"with hits")
