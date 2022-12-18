from VSG_ModuleEO import *
from random import randint

for i in range(100):
    xnew = randint(1,1000)
    ynew = randint(1,1000)
    vcircle(xc=log(xnew)*100,
            yc=log(ynew)*100,
            r=3,fill=red,
            stroke=black,
            xg=xnew,
            yg=ynew,
            label=str(xnew)+','+str(ynew))

vgrid(gxlog=True, gylog=True, gxlabel='XAxis', gylabel='YAxis')
vdisplay()

        
