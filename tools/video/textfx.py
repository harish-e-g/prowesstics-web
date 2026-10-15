import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
FONT="/usr/share/fonts/opentype/inter/Inter-Regular.otf"
def remove_text(f, box, bright=True, thr=10, dil=3, radius=6):
    x0,y0,x1,y1=box; roi=f[y0:y1,x0:x1]; g=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY).astype(np.int16)
    bg=cv2.medianBlur(g.astype(np.uint8),31).astype(np.int16)
    m=((g-bg)>thr) if bright else ((bg-g)>thr)
    m=cv2.dilate(m.astype(np.uint8)*255,np.ones((dil,dil),np.uint8),iterations=2)
    f[y0:y1,x0:x1]=cv2.inpaint(roi,m,radius,cv2.INPAINT_TELEA)
def draw_text(f, text, cx, cy, size, color=(255,255,255), alpha=1.0, spacing=0, shadow=True, font=FONT):
    if alpha<=0.003: return
    fnt=ImageFont.truetype(font,size)
    # measure
    tmp=ImageDraw.Draw(Image.new("L",(10,10)))
    if spacing:
        widths=[tmp.textlength(ch,font=fnt) for ch in text]; w=sum(widths)+spacing*(len(text)-1)
    else:
        w=tmp.textlength(text,font=fnt)
    asc,desc=fnt.getmetrics(); h=asc+desc
    W,H=int(w)+24,h+24; layer=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(layer)
    def put(dx,dy,fill):
        if spacing:
            x=12+dx
            for ch,cw in zip(text,widths): d.text((x,12+dy),ch,font=fnt,fill=fill); x+=cw+spacing
        else: d.text((12+dx,12+dy),text,font=fnt,fill=fill)
    if shadow:
        sh=Image.new("RGBA",(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
        d2=d; d=ds; put(0,2,(0,0,0,120)); d=d2
        sh=Image.fromarray(cv2.GaussianBlur(np.array(sh),(0,0),3)); layer=Image.alpha_composite(sh,layer); d=ImageDraw.Draw(layer)
    put(0,0,color+(255,))
    L=np.array(layer).astype(np.float32); a=L[...,3:4]/255.0*alpha; rgb=L[...,:3][...,::-1]
    x0=int(cx-W/2); y0=int(cy-H/2)
    xa,ya=max(0,x0),max(0,y0); xb,yb=min(f.shape[1],x0+W),min(f.shape[0],y0+H)
    roi=f[ya:yb,xa:xb].astype(np.float32); sa=a[ya-y0:yb-y0, xa-x0:xb-x0]; srgb=rgb[ya-y0:yb-y0, xa-x0:xb-x0]
    f[ya:yb,xa:xb]=(srgb*sa+roi*(1-sa)).astype(np.uint8)
