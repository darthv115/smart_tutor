

import getImage
# playing with a previous image
import recogniseDigits
from subprocess import call
import time

def smart_tutor():
	print "Starting...."

	cmd_beg= 'espeak '
	cmd_end= ' | aplay ../assets/wav_files/Text.wav  2>/dev/null' 
	cmd_out= '--stdout > ../assets/wav_files/Text.wav '

	print 'Hello, whats your name?'
	text='Hello, whats your name?'
	text = text.replace(' ', '_')
	call([cmd_beg+cmd_out+text+cmd_end], shell=True)
	time.sleep(7)

	print "What do you want to learn?"
	text1="What do you want to learn?"
	text1 = text1.replace(' ', '_')
	call([cmd_beg+cmd_out+text1+cmd_end], shell=True)
	time.sleep(7)

	print "Aha, numbers!"
	text3="Aha, numbers!"
	text3 = text3.replace(' ', '_')
	call([cmd_beg+cmd_out+text3+cmd_end], shell=True)
	time.sleep(7)

	print "Let us do some addition."
	text3="Let us do some addition."
	text3 = text3.replace(' ', '_')
	call([cmd_beg+cmd_out+text3+cmd_end], shell=True)
	time.sleep(7)

	print "Add two and two."
	text3="Add two and two."
	text3 = text3.replace(' ', '_')
	call([cmd_beg+cmd_out+text3+cmd_end], shell=True)
	time.sleep(7)

	# ********************************** Image Part *****************************

	# Get the image from the camera
	# img_file = getImage.capture()
	img_file = "../assets/images/test_4.jpg"

	digits = recogniseDigits.recog(img_file)
	# Drop the first element (0)
	digits = digits[1:]

	print "digits: ", digits

	if (digits[0] == 4):
		text4="Correct Answer, Well done."
		text4 = text4.replace(' ', '_')
		call([cmd_beg+cmd_out+text4+cmd_end], shell=True)
		time.sleep(7)
		print "Correct Answer, Well done."
	else:
		text7="Incorrect, Try again."
		text7 = text7.replace(' ', '_')
		call([cmd_beg+cmd_out+text7+cmd_end], shell=True)
		time.sleep(7)
		print "Incorrect, Try again."

# !end

if __name__ == '__main__':
	smart_tutor()