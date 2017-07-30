import cv2
import csv
import sys
import numpy as np

with open(sys.argv[1], 'r') as rf:
	rdr = csv.reader(rf, delimiter=' ')
	w = int(rdr.next()[0])
	h = int(rdr.next()[0])
	img = np.zeros((h,w,3), np.uint8)
	i = 0
	for row in rdr:
		row = rdr.next()
		x = i % w
		y = i / w
		pix = list(map(lambda x: int(x), row[0:3]))
		img.itemset((y,x,0),pix[0])
		img.itemset((y,x,1),pix[1])
		img.itemset((y,x,2),pix[2])
		i += 1

cv2.imshow("image", img)
cv2.waitKey(0)