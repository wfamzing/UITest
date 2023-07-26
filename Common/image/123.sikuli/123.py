
def hov(img,sim=0.7):
            if exists(img):
                hover(img)
                # jpype.shutdownJVM()
                return True
            else:
                return False
def ex(img,sim=0.7):
            if exists(img):
                # jpype.shutdownJVM()
                return True
            else:
                return False

if __name__ == '__main__':
     hov("piplen.png")
     e=ex("piplll.png")
     if e==True:
         print("管廊长度悬浮显示ok")
     else:
         print("管廊长度悬浮显示bug")
     print(e)
     hov("road.png")
     s=ex("piprrr.png")
     if s==True:
         print("管廊路段悬浮显示ok")
     else:
         print("管廊路段悬浮显示bug")
     print(s)