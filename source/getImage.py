import cv2
 
# Camera 1 is the webcam connected via USB
camera_port = 1
 
# Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Initializes the camera capture object with the cv2.VideoCapture class with the camera_port index.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")

def capture():
	camera_capture = get_image()
	file = "test_99.jpg"
	cv2.imwrite(file, camera_capture)
	return file
	# Releases the camera capture object
	del(camera)