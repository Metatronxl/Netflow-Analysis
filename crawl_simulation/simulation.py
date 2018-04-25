import time

import pyautogui as pag

'''

MacOS模拟点击各类应用的demo
用于完成实验室的shabi抓包任务
可以参考文档:http://blog.topspeedsnail.com/archives/5373

tips: 我就是来了一个shabi实验室
'''



def simulationFunc():

    loc1_x,loc1_y = 1146,1079
    loc2_x,loc2_y = 1142,1013 #find neteasy appicon
    loc3_x,loc3_y = 550,501 # find download music
    loc4_x,loc4_y = 784,526 # find wukong(song)
    loc5_x,loc5_y = 1157,901 # exit location

    pag.moveTo(loc1_x,loc1_y,duration=0.25)
    pag.moveTo(loc2_x,loc2_y,duration=0.25)
    pag.click(loc2_x,loc2_y,button='left')
    time.sleep(2)
    pag.moveTo(loc3_x,loc3_y)
    pag.click(loc3_x,loc3_y,button='left')
    pag.moveTo(loc4_x,loc4_y)
    # pag.click(loc4_x,loc4_y,button='left')
    pag.doubleClick(loc4_x,loc4_y,button='left')
    time.sleep(2)
    pag.moveTo(loc1_x,loc1_y,duration=0.25)
    pag.moveTo(loc2_x,loc2_y,duration=0.25)
    pag.click(loc2_x,loc2_y,button='right')
    pag.moveTo(loc5_x,loc5_y)
    pag.click(loc5_x,loc5_y,button='left')


if __name__ == '__main__':
    simulationFunc()
