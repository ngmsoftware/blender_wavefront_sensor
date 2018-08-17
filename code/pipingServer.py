#!/usr/bin/python

import os
import matplotlib.pyplot as plt
import itertools
import math
import time
import json


def computeRegion(x, y, LIMx, LIMy):
	curIdxX = -1
	curIdxY = -1
	idxX = -1
	idxY = -1
	for curIdxX in range(1,len(LIMx)):
		if x>LIMx[curIdxX-1] and x<LIMx[curIdxX]:
			idxX = curIdxX-1
			break

	for curIdxY in range(1,len(LIMy)):
		if y>LIMy[curIdxY-1] and y<LIMy[curIdxY]:
			idxY = curIdxY-1
			break

	return (idxX, idxY)





def doPrint(x, y, LIMx, LIMy, cx, cy, calCx, calCy):
	print('PRINT [start]...')

	lenX = len(LIMx)-1
	lenY = len(LIMy)-1

	maxLimX = max(LIMx)
	maxLimY = max(LIMy)
	minLimX = min(LIMx)
	minLimY = min(LIMy)

	print('PRINT [ploting clusters]...')
	t = time.time()
	#Xtmp = []
	#Ytmp = []
	plt.subplot(1,3,1)
	plt.cla()
	for idxX in range(0,lenX):	
		for idxY in range(0,lenY):
			#Xtmp =  Xtmp + x[idxX][idxY][:10:]
			#Ytmp =  Ytmp + y[idxX][idxY][:10:]
			plt.plot(x[idxX][idxY][:20:],y[idxX][idxY][:20:], '.b', markersize=2)
			plt.plot(calCx[idxX][idxY],calCy[idxX][idxY], 'g.', markersize=7)
			plt.plot(cx[idxX][idxY],cy[idxX][idxY], 'r.', markersize=7)
	plt.title('Light hits')
	plt.axis([minLimX, maxLimX, minLimY, maxLimY])
	plt.axis('equal')
	print('PRINT [ploted clusters]... %.4f'%(time.time()-t))

	qX = []
	qY = []
	qV = []
	qU = []
	print('PRINT [assembling vector field]...')
	t = time.time()
	for idxX in range(lenX):	
		for idxY in range(lenY):
			qX.append(calCx[idxX][idxY])
			qY.append(calCy[idxX][idxY])
			qV.append(cx[idxX][idxY]-calCx[idxX][idxY])
			qU.append(cy[idxX][idxY]-calCy[idxX][idxY])
	print('PRINT [assembled vector field]... %.4f'%(time.time()-t))
	


	print('PRINT [ploting vector field]...')
	t = time.time()
	plt.subplot(1,3,2)
	plt.cla()
	plt.quiver(qX, qY, qV, qU, scale=.15, headwidth=3, headlength=4, linewidth=.7, units='xy')
	plt.title('Wavefront direction')
	print('PRINT [ploted vector field]... %.4f'%(time.time()-t))



	print('PRINT [assembling image]...')
	t = time.time()
	D = [[0 for i in range(lenX)] for j in range(lenY)]
	for idxX in range(0,lenX):	
		for idxY in range(lenY):
			D[lenY-idxY-1][idxX] = math.sqrt( (cx[idxX][idxY]-calCx[idxX][idxY])**2 + (cy[idxX][idxY]-calCy[idxX][idxY])**2)
	print('PRINT [assembled image]... %.4f'%(time.time()-t))


	print('PRINT [ploting image]...')
	t = time.time()
	plt.subplot(1,3,3)
	plt.cla()
	plt.imshow(D, cmap=plt.get_cmap('Reds'), vmin=0.0, vmax=0.065, interpolation='spline16')
	plt.title('Wavefront magnitude')
	print('PRINT [ploted image]... %.4f'%(time.time()-t))


	t = time.time()
	print('PRINT [will show]')
	#plt.show()
	#plt.draw()
	plt.pause(0.001)
	print('PRINT [did show]... %.4f'%(time.time()-t))


	print('PRINT [end]...')








def doProcess(x, y, cx, cy, N, data, LIMx, LIMy):

	lenX = len(LIMx)-1
	lenY = len(LIMy)-1

	maxLimX = max(LIMx)
	maxLimY = max(LIMy)
	minLimX = min(LIMx)
	minLimY = min(LIMy)

	print('PROC [start]...')
	t = time.time()

	print('will PROC %d data points.'%len(data))

	for i in range(lenX):
		for j in range(lenY):
			x[i][j] = []
			y[i][j] = []
			cx[i][j] = 0.0
			cy[i][j] = 0.0

	for d in data:
		(idxX, idxY) = computeRegion(d[0],d[1], LIMx, LIMy)
		if idxX>=0 and idxY>=0:
			x[idxX][idxY].append(d[0])
			y[idxX][idxY].append(d[1])
			N[idxX][idxY] = N[idxX][idxY]+1
			cx[idxX][idxY] = (cx[idxX][idxY]*(N[idxX][idxY]-1)+d[0])/N[idxX][idxY]
			cy[idxX][idxY] = (cy[idxX][idxY]*(N[idxX][idxY]-1)+d[1])/N[idxX][idxY]

	del(data[:])
	for i in range(lenX):
		for j in range(lenY):
			N[i][j] = 0


	print('PROC [end]... %.4f'%(time.time()-t))








def doCalibrate(calCx, calCy, cx, cy, LIMx, LIMy):

	lenX = len(LIMx)-1
	lenY = len(LIMy)-1

	print('CAL [start]...')

	for idxX in range(lenX):	
		for idxY in range(lenY):
			calCx[idxX][idxY] = cx[idxX][idxY]
			calCy[idxX][idxY] = cy[idxX][idxY]

	print('CAL [end]...')











def doSave(x, y, cx, cy, calCx, calCy, filename):
	fid = open(filename,'wt')

	str = json.dumps({'x':x, 'y':y, 'cx':cx, 'cy':cy, 'calCx':calCx, 'calCy':calCy })

	strTest = 'x = cell(12,12);\ny=cell(12,12);\ncx = zeros(12,12);\ncy=zeros(12,12);\ncalCx = zeros(12,12);\ncalCy=zeros(12,12);\n';
	for i in range(12):
		for j in range(12):
			tmpX = ''
			tmpY = ''
			for k in range(len(x[i][j])):
				tmpX = tmpX + ',%.6f'%x[i][j][k]
				tmpY = tmpY + ',%.6f'%y[i][j][k]
			strTest = strTest + '\nx{%d,%d} = [%s];'%(i+1,j+1,tmpX[1:])
			strTest = strTest + '\ny{%d,%d} = [%s];'%(i+1,j+1,tmpY[1:])
			strTest = strTest + '\ncx(%d,%d) = %.6f;'%(i+1,j+1,cx[i][j])
			strTest = strTest + '\ncy(%d,%d) = %.6f;'%(i+1,j+1,cy[i][j])
			strTest = strTest + '\ncalCx(%d,%d) = %.6f;'%(i+1,j+1,calCx[i][j])
			strTest = strTest + '\ncalCy(%d,%d) = %.6f;'%(i+1,j+1,calCy[i][j])


	print('Data saved as '+filename)

	fid.write(strTest)

	fid.close()







def main():

	LIMx = [-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
	LIMy = [-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

	lenX = len(LIMx)-1
	lenY = len(LIMy)-1

	maxLimX = max(LIMx)
	maxLimY = max(LIMy)
	minLimX = min(LIMx)
	minLimY = min(LIMy)

	filename = '/tmp/render.m'
	data = []
	x = [[[] for i in range(lenX)] for j in range(lenY)]
	y = [[[] for i in range(lenX)] for j in range(lenY)]
	cx = [[0.0 for i in range(lenX)] for j in range(lenY)]
	cy = [[0.0 for i in range(lenX)] for j in range(lenY)]
	N = [[0 for i in range(lenX)] for j in range(lenY)]
	calCx = [[0.0 for i in range(lenX)] for j in range(lenY)]
	calCy = [[0.0 for i in range(lenX)] for j in range(lenY)]



	plt.figure(figsize=(3*5, 5), dpi=100)
	plt.ion()
	plt.show()

	while "forever":
		text = raw_input()

		if text[0:5]=='NIRPS':
			text = text[6:]

			if text[0:4] == 'SAVE':

				doSave(x, y, cx, cy, calCx, calCy, filename)



			elif text[0:4] == 'FILE':

				filename = text[5:]




			elif text[0:5] == 'PRINT':

				doPrint(x, y, LIMx, LIMy, cx, cy, calCx, calCy)



			elif text[0:4] == 'PROC':

				doProcess(x, y, cx, cy, N, data, LIMx, LIMy)



			elif text[0:3] == 'CAL':

				doCalibrate(calCx, calCy, cx, cy, LIMx, LIMy)


			else:
				data.append(map(float, text.split(',')))

		else:
			print('[ignored]: '+text)


			
if __name__ == '__main__':
	main()