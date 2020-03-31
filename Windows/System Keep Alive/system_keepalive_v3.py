def hujambo():
    print('''
##################################################
# Tool    : System Keepalive (Windows)           #
# Version : 3.0                                  #
# Coded with Python 3.7.4                        #
# Source  : https://github.com/pr2h/             #
##################################################
    ''')

# Description:
# This script keeps your system "alive" by not letting it go to either sleep or lock mode
# This is especially useful if you don't have the privilege to change the lock/ sleep settings in the computer

import pyautogui
import time
from random import *

if __name__=='__main__':
        # Displaying tool banner
        hujambo()

        pyautogui.FAILSAFE = False
        # Time between clicks
        sleep_time = 60

        # x and y Initialization
        x = 0
        y = 0

        # Start menu coordinates
        print("[*] By default the start menu coordinates are at (0, 800). Change it as per your requirement (screen size) in code")
        start_x = 0
        start_y = 800

        i = 0

        # Infinite Loop
        while True:
            try:
                # Current mouse position
                x, y = pyautogui.position()
                time.sleep(sleep_time)
                
                # Checking if mouse has been moved
                if pyautogui.position()[0] == x and pyautogui.position()[1] == y:
                        # Mouse has not been moved/ idle
                        i+=1
                        print("[*] Clicked " + str(i) + " time(s)")
                        # Click on Start menu
                        pyautogui.click(start_x, start_y)

                        random_x = pyautogui.position()[0]
                        random_y = pyautogui.position()[1]

                        # Moves the mouse pointer
                        for kk in range(1,500):
                            if pyautogui.position()[0] == random_x and pyautogui.position()[1] == random_y:
                                random_x = randint(0,500)
                                random_y = randint(0,500)
                                pyautogui.moveTo(random_x,random_y)
                            else:
                                # Mouse has been moved
                                break
                        
                else:
                        # Mouse has been moved
                        pass
            except:
                time.sleep(10)
