import time					  													## Import time library
import RPi.GPIO as GPIO       								## Import GPIO library

GPIO.setmode(GPIO.BOARD)      								## Use board pin numbering
GPIO.setwarnings(False)       								## Ignore warning for now

pinArray = [11, 13, 15, 19, 21]   							## declare connected GPIO pin

GPIO.setup(pinArray[0], GPIO.OUT) 							## Setup GPIO Pins to OUT
GPIO.setup(pinArray[1], GPIO.OUT)
GPIO.setup(pinArray[2], GPIO.OUT)
GPIO.setup(pinArray[3], GPIO.OUT)
GPIO.setup(pinArray[4], GPIO.OUT)

def dec2bin():
	reset()                                                                		## Turn off all LEDs Before Begin
	dec = int(input("Enter Decimal (0 <= Number <= 31): "))                		## user input as int

	if dec in range(32):                                                   		## check rage between 0 - 31
	   bin_dec = bin(dec)[2:].zfill(5)                                     		## conert to binary and crete fixed five digit lenth binary number
	   print("Binary Number : " + bin_dec)                                 		## Print binary number

	   bin_chunks = [bin_dec[i:i+1] for i in range(0, len(bin_dec), 1)]    		## get binary each bit value to string bin_chunk array

	   led5 = int(bin_chunks[0])                                                    ## convert string values to int values
	   led4 = int(bin_chunks[1])
	   led3 = int(bin_chunks[2])
	   led2 = int(bin_chunks[3])
	   led1 = int(bin_chunks[4])

	   GPIO.output(pinArray[0],led1)                                                 ## Turn on LEDs Acoring to binary values
	   GPIO.output(pinArray[1],led2)
	   GPIO.output(pinArray[2],led3)
	   GPIO.output(pinArray[3],led4)
	   GPIO.output(pinArray[4],led5)

	   menu()                                                                        ## return to menu

	else:
	   print("You have to enter key (0 <= key <= 31)")                          	 ## get out of range WARNING message
	   dec2bin()                                                                	 ## return

def user2bin():
	reset()
	dec = int(input("Enter Decimal (0 <= Number <= 31): "))

	if dec in range(32):
	   bin_dec = bin(dec)[2:].zfill(5)
	   print("Binary Number : " + bin_dec)

	   bin_chunks = [bin_dec[i:i+1] for i in range(0, len(bin_dec), 1)]

	   led5 = int(bin_chunks[0])
	   led4 = int(bin_chunks[1])
	   led3 = int(bin_chunks[2])
	   led2 = int(bin_chunks[3])
	   led1 = int(bin_chunks[4])

	   GPIO.output(pinArray[0],led1)  						  ## Turn on LEDs
	   GPIO.output(pinArray[1],led2)
	   GPIO.output(pinArray[2],led3)
	   GPIO.output(pinArray[3],led4)
	   GPIO.output(pinArray[4],led5)

	   menu()									  ## return to menu

	else:
	   print("You have to enter key (0 <= key <= 31)")                                ## get out of range WARNING message

	   for i in range(5):                                                             ## Blink five times LEDs
		   GPIO.output(pinArray[0],True)  					  ## Turn on LEDs
		   GPIO.output(pinArray[1],True)
		   GPIO.output(pinArray[2],True)
		   GPIO.output(pinArray[3],True)
		   GPIO.output(pinArray[4],True)

		   time.sleep(0.5)

		   GPIO.output(pinArray[0],False)  					  ## Turn on LEDs
		   GPIO.output(pinArray[1],False)
		   GPIO.output(pinArray[2],False)
		   GPIO.output(pinArray[3],False)
		   GPIO.output(pinArray[4],False)

		   time.sleep(0.5)

	   user2bin()

def reset():                                                                              ## rest the LEDs (Turn off all)
	for x in pinArray:
		GPIO.output(x,False)

def toRight():                                                                            ## Sweeping light movement from right to left
	print("Press Ctrl-C to terminate the Run")
	reset()
	try:
		while True:
			for x in pinArray:
				GPIO.output(x,True)
				time.sleep(0.5)
				GPIO.output(x,False)
				time.sleep(0.5)

	except KeyboardInterrupt:                                                         ## If user enter Ctrl-C to terminate the Run and return to menu
            menu()
            pass

def toLeft():                                                                             ## Sweeping light movement from left to right
	print("Press Ctrl-C to terminate the Run")
	reset()
	try:
		while True:
			for x in reversed(pinArray):
				GPIO.output(x,True)
				time.sleep(0.5)
				GPIO.output(x,False)
				time.sleep(0.5)

	except KeyboardInterrupt:							  ## If user enter Ctrl-C to terminate the Run and return to menu
            menu()
            pass

def sweep():                                                                              ## Continuous sweeping light movement
	print("Press Ctrl-C to terminate the Run")
	reset()
	try:
		while True:
			for x in pinArray:						  ## Right to left
				GPIO.output(x,True)
				time.sleep(0.5)
				GPIO.output(x,False)
				time.sleep(0.5)

			for x in reversed(pinArray):					  ## Left to Right
				GPIO.output(x,True)
				time.sleep(0.5)
				GPIO.output(x,False)
				time.sleep(0.5)

	except KeyboardInterrupt:						          ## If user enter Ctrl-C to terminate the Run and return to menu
            menu()
            pass

def menu():										  ## menu
    print ("""
    1.Sequential count in Binary
    2.Sweeping light movement from right to left
    3.Sweeping light movement from left to right
    4.Continuous sweeping light movement
    5.User input Decimal to Binary translation
    6.Exit
		Enter your choice (1-6):
    """)

    ans=input("What would you like to do? ")                                 	          ## get user input
    if ans=="1":
    	dec2bin()
    if ans=="2":
    	toRight()
    if ans=="3":
    	toLeft()
    if ans=="4":
    	sweep()
    if ans=="5":
    	user2bin()
    if ans=="6":
    	print("\n Goodbye")
    	reset()
    	exit()										  ## reset and exit the code
    if ans !="":
    	print("\n Not Valid Choice Try again")

menu();
