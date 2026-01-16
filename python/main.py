import time

from arduino.app_utils import App

def loop():
    print("Hello, my name is Thana Udomsripaiboon")
    time.sleep(1)

App.run(user_loop=loop)
