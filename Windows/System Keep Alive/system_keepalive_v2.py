def hujambo():
    print('''
##################################################
# Tool    : System Keepalive (Windows)           #
# Version : 2.0                                  #
# Coded with Python 3.7.4                        #
# Source  : https://github.com/pr2h/             #
##################################################
    ''')

# Description:
# This script keeps your system "alive" by not letting it go to either sleep or lock mode
# This is especially useful if you don't have the privilege to change the lock/ sleep settings in the computer

import pyautogui
import time

if __name__=='__main__':
        # Displaying tool banner
        hujambo()

        pyautogui.FAILSAFE = False
        # Time between clicks
        sleep_time = 10

        # x and y Initialization
        x = 0
        y = 0

        # Start menu coordinates
        print("[*] By default the start menu coordinates are at (0, 800). Change it as per your requirement (screen size) in code")
        start_x = 0
        start_y = 800

        # Infinite Loop
        while True:
                # Current mouse position
                x, y = pyautogui.position()
                time.sleep(sleep_time)

                i = 0
                # Checking if mouse has been moved
                if pyautogui.position()[0] == x and pyautogui.position()[1] == y:
                        # Mouse has not been moved/ idle
                        i+=1
                        print("[*] Clicked " + str(i) + " time(s)")
                        # Click on Start menu
                        pyautogui.click(start_x, start_y)
                        
                else:
                        # Mouse has been moved
                        pass
