# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = None

def touch(x, y):
        global d
        device.touch(x, y, "DOWN_AND_UP")

def fight():
	global d
	invoke_hero()
	MonkeyRunner.sleep(0.5)	
	call_all_skill()
	MonkeyRunner.sleep(0.5)	
	max_hero_level()

def invoke_hero():
	global d
	d.touch(1350, 1000, "DOWN_AND_UP") # change to hero
	MonkeyRunner.sleep(0.5)	
	touch_bottom()

def call_all_skill():
	global d
	d.touch(1200, 1000, "DOWN_AND_UP") # change to monster 	
	MonkeyRunner.sleep(0.5)
	touch_bottom()		

def max_hero_level():
	global d
	d.touch(1350, 1000, "DOWN_AND_UP") # change to hero
	MonkeyRunner.sleep(0.5)	
	for _ in range(50):
		touch_bottom()
		MonkeyRunner.sleep(0.1)	

def touch_bottom():
	global d
	d.touch(250, 900, "DOWN_AND_UP") # 1st hero
	d.touch(450, 900, "DOWN_AND_UP") # 2ed hero
	d.touch(650, 900, "DOWN_AND_UP") # 3rd hero
	d.touch(850, 900, "DOWN_AND_UP") # 4ur hero
	d.touch(1050, 900, "DOWN_AND_UP") # 5th hero

if __name__ == '__main__':
        global device
        # Connects to the current device, returning a MonkeyDevice object
        device = MonkeyRunner.waitForConnection()

        package = 'jp.co.happyelements.toto'
        activity = 'jp.co.happyelements.unity_plugins.MainActivity'

        runComponent = package + '/' + activity
        device.startActivity(component=runComponent)

        MonkeyRunner.sleep(5)
        X = float(device.getProperty("display.width"))
        Y = float(device.getProperty("display.height"))

        # Presses the Menu button
        # device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(10)
        touch( int(X/2), int(Y/2))

        # Takes a screenshot
        result = device.takeSnapshot()

        # Writes the screenshot to a file
        result.writeToFile('shot1.png','png')

