#Import blinkstick module
from blinkstick import blinkstick
import time
import argparse
import random
import signal, os


shutdown=False

def main(args=None):
	for bstick in blinkstick.find_all():
	    #Set the color red on the 12th LED of R channel
	    #for entry in range(255):
	    # set_color(self, channel=0, index=0, red=0, green=0, blue=0, name=None, hex=None): 
		bstick.set_color(channel=0, index=0, red=255, green=0, blue=0, name=None, hex=None)
		time.sleep(0.25)
	
def cooler():
	for bstick in blinkstick.find_all():
	    #Set the color red on the 12th LED of R channel
	    #for entry in range(255):
	    # set_color(self, channel=0, index=0, red=0, green=0, blue=0, name=None, hex=None):
	    for step in range (50):
		    [r, g, b] = bstick.get_color()
		    #print("cur color R{} G{} B{}".format(r,g,b)) 
		    bstick.set_color(channel=0, index=0, red=max(r-1, 0), green=0, blue=min(b+1, 255), name=None, hex=None)

def hotter():
	for bstick in blinkstick.find_all():
	    #Set the color red on the 12th LED of R channel
	    #for entry in range(255):
	    # set_color(self, channel=0, index=0, red=0, green=0, blue=0, name=None, hex=None):
	    for step in range (50):
		    [r, g, b] = bstick.get_color()
		    # print("cur color R{} G{} B{}".format(r,g,b)) 
		    bstick.set_color(channel=0, index=0, red=min(r+1, 255), green=0, blue=max(b-1,0), name=None, hex=None)

def heat_pulse(t=10):
	setup_shutdown_signal()
	r = 0
	b = 0
	while not shutdown:
		for bstick in blinkstick.find_all():
		    #Set the color red on the 12th LED of R channel
		    #for entry in range(255):
		    # set_color(self, channel=0, index=0, red=0, green=0, blue=0, name=None, hex=None):
		    [r, g, b] = bstick.get_color()
		    while r < 255:
		    	hotter()
		    	[r, g, b] = bstick.get_color()
		    while b < 255:
		    	cooler()
		    	[r, g, b] = bstick.get_color()

def set_color():
	parser = argparse.ArgumentParser()
	parser.add_argument("r")
	parser.add_argument("g")
	parser.add_argument("b")
	args = parser.parse_args()
	r = int(args.r)
	g = int(args.g)
	b = int(args.b)
	print(args)
	for bstick in blinkstick.find_all():
	    #Set the color red on the 12th LED of R channel
	    #for entry in range(255):
	    # set_color(self, channel=0, index=0, red=0, green=0, blue=0, name=None, hex=None):
		bstick.set_color(channel=0, index=0, red=r, green=g, blue=b, name=None, hex=None)

def police():
	setup_shutdown_signal()
	r = 255
	b = 0
	g = 0
	count = 0
	while not shutdown:
		for bstick in blinkstick.find_all():
			r = 255 * (count % 2)
			b = 255 * ((count+1) % 2)
			bstick.set_color(channel=0, index=0, red=r, green=g, blue=b, name=None, hex=None)
		time.sleep(.10)
		count += 1
		if count == 101:
			count = 0

def rando_rainbow():
	setup_shutdown_signal()
	while not shutdown:
		for bstick in blinkstick.find_all():
			r = random.randrange(255)
			b = random.randrange(255)
			g = random.randrange(255)
			bstick.set_color(channel=0, index=0, red=r, green=g, blue=b, name=None, hex=None)
		time.sleep(.10)

def shut_off_bsticks():
	for bstick in blinkstick.find_all():
		bstick.turn_off()

def shutdown_handler(signum, frame):
    print("Shutting down...")
    global shutdown
    shutdown = True
    shut_off_bsticks()
    exit()


def setup_shutdown_signal():
	signal.signal(signal.SIGINT, shutdown_handler)


if __name__ == "__main__":
    main()