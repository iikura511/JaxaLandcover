#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cd /Volumes/Transcend/JAXA土地被覆

import sys
import jaxa_util as ut
import cv2
import numpy as np
from scipy import interpolate

param=sys.argv
if len(param)!=2:
    print 'Usage: extract_utm.py file_name'

fname=param[1]
f=open(fname)
lines=f.readlines()
f.close()

for line in lines:
  if line.find('xs')!=-1: ut.xs=float(line.split()[1])
  if line.find('xe')!=-1: ut.xe=float(line.split()[1])
  if line.find('ys')!=-1: ut.ys=float(line.split()[1])
  if line.find('ye')!=-1: ut.ye=float(line.split()[1])
  if line.find('dx')!=-1: ut.dx=float(line.split()[1])
  if line.find('dy')!=-1: ut.dy=float(line.split()[1])
  print line,


ul=ut.utm2bl([ut.xs,ut.ye])
ur=ut.utm2bl([ut.xe,ut.ye])
ll=ut.utm2bl([ut.xs,ut.ys])
lr=ut.utm2bl([ut.xe,ut.ys])

s_lat=np.min([ul[0],ur[0],ll[0],lr[0]])
e_lat=np.max([ul[0],ur[0],ll[0],lr[0]])
s_lon=np.min([ul[1],ur[1],ll[1],lr[1]])
e_lon=np.max([ul[1],ur[1],ll[1],lr[1]])

slatx=int(s_lat)
elatx=int(e_lat)
slonx=int(s_lon)
elonx=int(e_lon)
print slatx,elatx,slonx,elonx
ut.lat0=elatx+1
ut.lon0=slonx

imax=12000*(elatx-slatx+1)
jmax=12000*(elonx-slonx+1)
old=np.zeros(imax*jmax,dtype=np.uint8).reshape(imax,jmax)

for i in range(slatx,elatx+1):
  ist=12000*(elatx-i) ; ien=12000*(elatx+1-i)
  for j in range(slonx,elonx+1):
    fname='LC_N'+str(i)+'E'+str(j)+'.tif'
    gt,proj,temp=ut.read_tif(fname)
    print fname
    jst=12000*(j-slonx) ; jen=12000*(j+1-slonx)
    print ist,ien,jst,jen
    old[ist:ien,jst:jen]=temp


#oldx=cv2.resize(old,(600*(elonx-slonx+1),600*(elatx-slatx+1)))
#cv2.imshow('old',oldx*20)
#cv2.waitKey(0)

ut.dlat=1.0/12000
ut.dlon=1.0/12000
imax=int((ut.xe-ut.xs)/ut.dx)
jmax=int((ut.ye-ut.ys)/ut.dy)
new=ut.convert(old,imax,jmax)
#newx=cv2.resize(new,(600,600))
#cv2.imshow('new',newx*20)
#cv2.waitKey(0)

ut.write_tif('new_utm.tif',new.astype(np.uint8),1)

#cv2.destroyAllWindows()

exit()
