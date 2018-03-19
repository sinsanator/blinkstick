from blinkstick import blinkstick


def main(args=None):
	for bstick in blinkstick.find_all():
	    bstick.turn_off()
	    print (bstick.get_serial() + " turned off")

if __name__ == "__main__":
    main()