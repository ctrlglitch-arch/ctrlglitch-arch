#!/usr/bin/env python3
"""Generate a multicolor rotating ASCII black-hole GIF for a GitHub README.
Install: python -m pip install pillow
Run:     python generate_ascii_blackhole.py
Output:  assets/ascii-blackhole.gif
"""
from PIL import Image, ImageDraw, ImageFont
import math, os

W, H, COLS, ROWS = 720, 470, 90, 42
FRAMES, DURATION = 48, 70
RAMP = " .,:;irsXA253hMHGS#9B&@"
PALETTE = [(45,220,255),(125,100,255),(255,55,155),(255,115,75)]

def font_for(size):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
              "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",
              "C:/Windows/Fonts/consola.ttf"]:
        try: return ImageFont.truetype(p,size)
        except OSError: pass
    return ImageFont.load_default()

def rot_x(p,a):
    x,y,z=p; c,s=math.cos(a),math.sin(a)
    return x,y*c-z*s,y*s+z*c

def rot_y(p,a):
    x,y,z=p; c,s=math.cos(a),math.sin(a)
    return x*c+z*s,y,-x*s+z*c

def mix(a,b,t):
    return tuple(int(a[i]*(1-t)+b[i]*t) for i in range(3))

def render(fi):
    angle=2*math.pi*fi/FRAMES
    grid=[[None for _ in range(COLS)] for _ in range(ROWS)]
    zbuf=[[-1e9 for _ in range(COLS)] for _ in range(ROWS)]
    for i in range(300):
        u=2*math.pi*i/300
        for j in range(80):
            v=2*math.pi*j/80
            rr=1.55+0.50*math.cos(v)
            p=rot_y(rot_x((rr*math.cos(u),0.50*math.sin(v),rr*math.sin(u)),0.70),angle)
            x,y,z=p; sc=1/(1+0.075*z)
            sx=int(COLS/2+x*15.8*sc); sy=int(ROWS/2+y*8.2*sc)
            if 0<=sx<COLS and 0<=sy<ROWS and z>zbuf[sy][sx]:
                glow=max(0,min(1,0.18+0.50*(0.5+0.5*math.sin(u*3.2-angle*1.5))+0.25*(0.5+0.5*math.cos(v*1.8))))
                glyph=RAMP[min(len(RAMP)-1,int(glow*(len(RAMP)-1)))]
                q=(u/(2*math.pi)*len(PALETTE)+fi/FRAMES*1.7)%len(PALETTE)
                pi=int(q); col=mix(PALETTE[pi],PALETTE[(pi+1)%len(PALETTE)],q-pi)
                col=tuple(int(c*(0.35+0.65*glow)) for c in col)
                grid[sy][sx]=(glyph,col); zbuf[sy][sx]=z
    for i in range(1000):
        t=2*math.pi*i/1000; phase=t+angle*0.22
        sx=int(COLS/2+38*math.cos(phase))
        sy=int(ROWS/2+10*math.sin(phase)+1.3*math.sin(2*t+angle))
        ph=(t+angle*1.3)%(2*math.pi)
        if 1.05<ph<1.8: continue
        if 0<=sx<COLS and 0<=sy<ROWS:
            q=(t/(2*math.pi)*len(PALETTE)+fi/FRAMES)%len(PALETTE)
            pi=int(q); col=mix(PALETTE[pi],PALETTE[(pi+1)%len(PALETTE)],q-pi)
            grid[sy][sx]=(".:+*"[int((0.5+0.5*math.sin(t*8-angle*2))*3.99)],col)
    cx,cy=COLS//2,ROWS//2
    for y in range(ROWS):
        for x in range(COLS):
            if ((x-cx)/1.4)**2+((y-cy)/0.75)**2<5.3: grid[y][x]=None
    cw,ch=W/COLS,H/ROWS; font=font_for(11)
    im=Image.new("RGB",(W,H),(2,3,9)); d=ImageDraw.Draw(im)
    for k in range(170):
        x=(k*47+fi*2)%COLS; y=(k*23+fi//2)%ROWS
        if grid[y][x] is None:
            c=PALETTE[(k//13+fi//8)%len(PALETTE)]
            d.text((int(x*cw),int(y*ch)), "." if k%4 else "+", font=font,
                   fill=tuple(int(v*0.34) for v in c))
    for y,row in enumerate(grid):
        for x,item in enumerate(row):
            if item: d.text((int(x*cw),int(y*ch)),item[0],font=font,fill=item[1])
    f=font_for(12)
    d.text((18,12),"ASCII BLACK HOLE  /  ROTATION SEQUENCE",font=f,fill=(145,160,190))
    d.text((18,H-25),"CTRLGLITCH  //  EVENT HORIZON",font=f,fill=(95,125,165))
    return im.convert("P",palette=Image.Palette.ADAPTIVE,colors=192)

def main():
    os.makedirs("assets",exist_ok=True)
    images=[render(i) for i in range(FRAMES)]
    images[0].save("assets/ascii-blackhole.gif",save_all=True,append_images=images[1:],
                   duration=DURATION,loop=0,optimize=True,disposal=2)
    print("Generated assets/ascii-blackhole.gif")

if __name__=="__main__": main()
