import cv2
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import sys

# load the image and grab its width and height
image = cv2.imread(sys.argv[1])
image = cv2.resize(image, (256,256))
(h, w) = image.shape[:2]

def quantize(img):
    image = img.copy()
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = MiniBatchKMeans(n_clusters=5)
    labels = clt.fit_predict(image)
    quant = clt.cluster_centers_.astype("uint8")[labels]
    quant = quant.reshape((img.shape[0], img.shape[1], 3))
    # quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
    return quant

def bilateral(img):
    return cv2.bilateralFilter(img,9,75,75)

def shrink(img):
    return cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)

def stretch(img):
    return cv2.resize(img, (0,0), fx=2, fy=2, interpolation=cv2.INTER_NEAREST)

newimg = image.copy()
imgs = []

for _ in xrange(3):
    newimg = shrink(newimg)
    imgs.append(newimg)
    newimg = quantize(newimg)
    imgs.append(newimg)
    newimg = bilateral(newimg)
for img in imgs:
    img = cv2.resize(img, (256,256), interpolation=cv2.INTER_NEAREST)
    cv2.imshow("image", img)
    cv2.waitKey(0)
