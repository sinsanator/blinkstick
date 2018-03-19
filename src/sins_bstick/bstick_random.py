from blinkstick import blinkstick

def main(args=None):
	for bstick in blinkstick.find_all():
	    bstick.set_random_color()
	    print bstick.get_serial() + " " + bstick.get_color(color_format="hex")

if __name__ == "__main__":
    main()