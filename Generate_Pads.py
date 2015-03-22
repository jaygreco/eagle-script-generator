
#########################################################################
#									#
# Python script to generate standardized device layouts in eagle.	#
# Default is through-hole DIP, but this can easily be changed. 		#
# Simply change the pad spacing (0.1" is default), choose the number 	#
# of X and Y pads, the X and Y spacing, and run the script. 		#
# It will generate an EAGLE .scr script file. 				#
#									#
#########################################################################

#Import the time module
import datetime

#Get the current time for filename purposes
now = datetime.datetime.now()

#Generate the file string
filestr = "Generated pads " + now.strftime("%Y-%m-%d-%H%M") + ".scr"

#Create a file reference, overwriting one if it already exisits.
fo = open(filestr, "w+")

#Set the general parameters for both SMD and through hole. 
isSMD = True
numpadsX = 2
numpadsY = 7
xspacing = 0.4
yspacing = 0.1

if isSMD:
	#SMD pad info. If using through hole, there is no need to change these items.
	#0.05 x 0.025 is default
	dimensions = "0.05 x 0.025"
	#0 is default
	roundness = "0"

	#Write the Eagle configuration commands necessary to place the pads.
	#These can be changed if a surface mount part is required, for example.
	tempstr = "CHANGE SMD " + dimensions + " \n"
	fo.write(tempstr)

	tempstr = "CHANGE ROUNDNESS " + roundness + " \n"
	fo.write(tempstr)

else:
	#Through hole pad info. If using SMD, there is no need to change these items.
	#SQUARE, ROUND, OCTAGON, LONG, OFFSET
	shape = "ROUND"
	#0.04 is default
	drill = "0.04"
	#auto is default
	diameter = "0.076"

	#Write the Eagle configuration commands necessary to place the pads.
	#These can be changed if a surface mount part is required, for example.
	tempstr = "CHANGE SHAPE " + shape + " \n"
	fo.write(tempstr)

	tempstr = "CHANGE DRILL " + drill + " \n"
	fo.write(tempstr)

	tempstr = "CHANGE DIAMETER " + diameter + " \n"
	fo.write(tempstr)

if isSMD:
	#Loop through and create the pads themselves.
	for x in range (0, numpadsX):

		#This isn't super pretty, but it's an easy way to make the pin assignments "corrent",
		#With pin 1 in the upper left and pin n in the upper right. Otherwise it would bother me.

		#This is either the first column, or an even column.
		if (x%2==0):
			for y in range (0, numpadsY):

				#This is the Eagle command which actually creates the pad.
				command = 'smd (' + str(x*xspacing) + ' ' + str(-y*yspacing) + ');'
				fo.write(command)
				fo.write('\n')
		#This is an odd column, so go backwards. 		
		else:
			for y in range (-numpadsY+1, 1):

				#This is the Eagle command which actually creates the pad.
				command = 'smd (' + str(x*xspacing) + ' ' + str(y*yspacing) + ');'
				fo.write(command)
				fo.write('\n')

else:
	#Loop through and create the pads themselves.
	for x in range (0, numpadsX):

		#This isn't super pretty, but it's an easy way to make the pin assignments "corrent",
		#With pin 1 in the upper left and pin n in the upper right. Otherwise it would bother me.

		#This is either the first column, or an even column.
		if (x%2==0):
			for y in range (0, numpadsY):

				#This is the Eagle command which actually creates the pad.
				command = 'pad (' + str(x*xspacing) + ' ' + str(-y*yspacing) + ');'
				fo.write(command)
				fo.write('\n')
		#This is an odd column, so go backwards. 		
		else:
			for y in range (-numpadsY+1, 1):

				#This is the Eagle command which actually creates the pad.
				command = 'pad (' + str(x*xspacing) + ' ' + str(y*yspacing) + ');'
				fo.write(command)
				fo.write('\n')

#Close the file reference.
fo.close()
