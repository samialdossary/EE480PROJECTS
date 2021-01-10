#!/bin/sh

#start of the code 

while :
 do
echo 1 | sudo tee /sys/class/leds/led0/brightness
echo 0 | sudo tee /sys/class/leds/led1/brightness
	sleep 1
echo 0 | sudo tee /sys/class/leds/led0/brightness
echo 1 | sudo tee /sys/class/leds/led1/brightness
done

