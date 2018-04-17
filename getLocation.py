import os,time
import pyautogui as pag


#get mouse'location once by 1 sec
def returnLocation():
    while(1):
        # print("location:")
        x,y = pag.position()
        posStr = "Position:"+str(x).rjust(4)+','+str(y).rjust(4)
        print(posStr)
        time.sleep(1)
        # return x,y


if __name__ == '__main__':
    returnLocation()