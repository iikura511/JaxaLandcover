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
    print 'Usage: extract_bl.py file_name'

fname=param[1]
f=open(fname)
lines=f.readlines()
f.close()

for line in lines:
  if line.find('s_lon')!=-1: s_lon=float(line.split()[1])
  if line.find('s_lat')!=-1: s_lat=float(line.split()[1])
  if line.find('e_lon')!=-1: e_lon=float(line.split()[1])
  if line.find('e_lat')!=-1: e_lat=float(line.split()[1])
  if line.find('dlat')!=-1: dlat=float(line.split()[1])
  if line.find('dlon')!=-1: dlon=float(line.split()[1])
  print line,

nlon=(e_lon-s_lon)/dlon
nlat=(e_lat-s_lat)/dlat
print nlon,nlat
#exit()

slatx=int(s_lat)
elatx=int(e_lat)
slonx=int(s_lon)
elonx=int(e_lon)
print slatx,elatx,slonx,slatx

imax=12000*(elatx-slatx+1)
jmax=12000*(elonx-slonx+1)

print imax,jmax

#exit()

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


#oldx=cv2.resize(old,(600,600))
#cv2.imshow('old',oldx*20)
#cv2.waitKey(0)

x=np.arange(float(jmax))
y=np.arange(float(imax))
ex_func=interpolate.RegularGridInterpolator((x,y),old,method='nearest')

xx=((s_lon+np.arange(nlon+1)*dlon)-float(slonx))*12000.0
yy=(float(elatx+1)-(e_lat-np.arange(nlat+1)*dlat))*12000.0
xxx,yyy=np.meshgrid(xx,yy)
new=ex_func((yyy,xxx))
#newx=cv2.resize(new,(600,600))
#cv2.imshow('new',newx/10)
#cv2.waitKey(0)

ut.xs=s_lon
ut.dx=dlon
ut.ye=e_lat
ut.dy=dlat
ut.write_tif('new_bl.tif',new.astype(np.uint8),2)

cv2.destroyAllWindows()

exit()
