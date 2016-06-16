from scipy import ndimage
from scipy import misc

from moviepy.editor import *
from moviepy.video.fx import rotate

def rotateImage(image,startTime,rotationDurationPerFrame,amountToRatePerFrame):

	if (rotationDurationPerFrame == 0):
		durationVar = 1/40
	else:
		durationVar = rotationDurationPerFrame/30
	# print "rotDegree = ",rotDegree
	rotate_face = ndimage.rotate(image, amountToRatePerFrame)
	# print rotate_face
	im = ImageClip(rotate_face).set_pos((120,30)).set_duration(rotationDurationPerFrame).set_start(startTime)
	return im