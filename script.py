from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
d = MonkeyRunner.waitForConnection()
bp0 = MonkeyRunner.loadImageFromFile("./bp0.png")
bp0_2 = MonkeyRunner.loadImageFromFile("./bp0-2.png")

REF_W = 1920.0
REF_H = 1080.0

ADJUST_W = 1280.0 / REF_W
ADJUST_H = 768.0 / REF_H

OFFSET_W = -20

def run():
        while True:
                go_to_check_list()
                prepare_attack()
                if check_0bp() == False:
                    continue
                skip()
                fight2()

def go_to_check_list():
        d.touch(550 * ADJUST_W, 1000 * ADJUST_H, "DOWN_AND_UP") # mission summary
        MonkeyRunner.sleep(1)
        d.touch(550 * ADJUST_W, 1000 * ADJUST_H, "DOWN_AND_UP") # mission summary
        MonkeyRunner.sleep(3)

        d.touch(550 * ADJUST_W, 300 * ADJUST_H, "DOWN_AND_UP")  # mission-in
        MonkeyRunner.sleep(1)
        d.touch(550 * ADJUST_W, 300 * ADJUST_H, "DOWN_AND_UP")  # mission-in
        MonkeyRunner.sleep(3)

        d.touch(1300 * ADJUST_W, 150 * ADJUST_H, "DOWN_AND_UP") # check list
        MonkeyRunner.sleep(1)
        d.touch(1300 * ADJUST_W, 150 * ADJUST_H, "DOWN_AND_UP") # check list
        MonkeyRunner.sleep(3)

def prepare_attack():
        d.touch(1600 * ADJUST_W, 450 * ADJUST_H, "DOWN_AND_UP") # attack-in-prepare
        MonkeyRunner.sleep(5)

def check_0bp():
        # d.takeSnapshot().getSubImage((380,200,50,200)).sameAs(bp0, 0.5):
        if d.takeSnapshot().getSubImage((270,100,50,200)).sameAs(bp0_2, 0.7):
                d.touch(1400 * ADJUST_W, 800 * ADJUST_H, "DOWN_AND_UP") # attack-start
                MonkeyRunner.sleep(10)
                return True
        else:
                return False

def skip():
        global d
        MonkeyRunner.sleep(1)
        d.touch(1400 * ADJUST_W, 800 * ADJUST_H, "DOWN_AND_UP") # attack-start
        MonkeyRunner.sleep(2)
                
def fight():
        global d
        touch_bottom() # invoke hero
        toggle()
        touch_bottom() # invoke skill
        MonkeyRunner.sleep(4) # wait fo skill complete
        toggle()
        max_hero_level()
        toggle_speed()
        MonkeyRunner.sleep(20) # wait for end

def fight2():
        global d
        for _ in range(20):
                for _ in range(10):
                        touch_bottom()
                        MonkeyRunner.sleep(0.05)
                toggle()                
                MonkeyRunner.sleep(0.25) # wait fo skill complete
        toggle_speed()
        MonkeyRunner.sleep(15) # wait for end
        skip()

def toggle():
        global d
        d.touch(1350 * ADJUST_W, 1000 * ADJUST_H, "DOWN_AND_UP") # change to hero
        MonkeyRunner.sleep(0.5) 

def toggle_speed():
        d.touch(1700 * ADJUST_W, 700 * ADJUST_H, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.1)
        d.touch(1700 * ADJUST_W, 700 * ADJUST_H, "DOWN_AND_UP")

def max_hero_level():
        global d
        for _ in range(30):
                touch_bottom()
                MonkeyRunner.sleep(0.3) 

def touch_bottom():
        global d
        d.touch(250 * ADJUST_W + OFFSET_W, 900 * ADJUST_H, "DOWN_AND_UP") # 1st hero
        d.touch(450 * ADJUST_W + OFFSET_W, 900 * ADJUST_H, "DOWN_AND_UP") # 2ed hero
        d.touch(650 * ADJUST_W + OFFSET_W, 900 * ADJUST_H, "DOWN_AND_UP") # 3rd hero
        d.touch(850 * ADJUST_W + OFFSET_W, 900 * ADJUST_H, "DOWN_AND_UP") # 4ur hero
        d.touch(1050 * ADJUST_W+ OFFSET_W, 900 * ADJUST_H, "DOWN_AND_UP") # 5th hero

if __name__ == '__main__':
        run()
