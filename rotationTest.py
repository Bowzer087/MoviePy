from moviepy.editor import *
from moviepy.video.fx import rotate

from scipy import ndimage
from scipy import misc

import imageio
import rotateImage

w = 640
h = w*9/16 # 16/9 screen
moviesize = w,h

startTime = 0

imageArray = []

frameRate = 40

rotatingImage = imageio.imread('test.png')

rotation = 360

'''
	rotation is the amount of rotaion in degress the image does, 360 would be 1 full rotation 
	
'''

countingRotation = rotation/360

'''
	countingRotation is the amount of rotaion the image does.  It's calcualted based off of 360 being one full rotaion 
	example
		180 = 1/2 rotation
		360 = 1 full rotation
		540 = 1 1/2 roation
		720 = 2 full rotations

	If the first key frame is larger than the second that means the image is going counter clockwise
	example
		keyframe 0 = 0 rotation
		keyframe 40 = 360 rotation means the image rotated one time clock wise
		keyframe 50 = 180 rotation means the image rotated counter clockwise 1/2 rotation


'''



rotationDuration = 5
'''
	rotationDuration is the length of time the rotation occurs between certain key frames
	example
		image starts at 0 secs and goes until 1 sec and flips one time.
		rotationDuration would be 1 (for 1 sec)

		image starts at 0 secs and goes until 2 secs BUT there's a change in the roation at the 1 sec mark
		roationDuration would need to be set twice and would be 1 sec both times.

'''

rotationDurationPerFrame = round(float(rotationDuration)/frameRate,6)

amountToRatePerFrame = float(rotation)/frameRate

startingRotation = 0

while (startTime < rotationDuration):
	rotatedImage = rotateImage.rotateImage(rotatingImage,startTime,rotationDurationPerFrame,startingRotation)
	countingRotation = countingRotation + 1
	startTime = startTime + rotationDurationPerFrame
	startingRotation = startingRotation + amountToRatePerFrame
	imageArray.append(rotatedImage)


final = CompositeVideoClip(imageArray, size = moviesize)

final.set_duration(5).write_videofile("exports/rotationTest_5secs.mp4", fps=frameRate,codec='mpeg4',bitrate="4000k",audio_codec="mp3")