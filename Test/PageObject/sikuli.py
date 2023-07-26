import time
from jpype import *
import jpype
jvmPath = jpype.getDefaultJVMPath()
print(jvmPath)

class Sikuli:
    def __init__(self):
        jvmPath = jpype.getDefaultJVMPath()
        print(jvmPath)
        try:
            jpype.startJVM(jvmPath, "-ea", r"-Djava.class.path=.\Config\sikulixapi-2.0.5.jar")
        except:
            pass
        jpype.java.lang.System.out.println("hello java!")
    def screen(self):
        Screen = jpype.JClass("org.sikuli.script.Screen")
        s = Screen()  # 实例化Screen类
        return s
    def pattern(self):
        Pattern = jpype.JClass('org.sikuli.script.Pattern')
        return Pattern
# def getJVM():
#     jvmPath = jpype.getDefaultJVMPath()
#     print(jvmPath)
#     try:
#         jpype.startJVM(jvmPath, "-ea", r"-Djava.class.path=.\Config\sikulixapi-2.0.5.jar")
#     except:
#         pass
#     jpype.java.lang.System.out.println("hello world")
#     Pattern = JClass('org.sikuli.script.Pattern')
#     Screen = jpype.JClass("org.sikuli.script.Screen")
#     s = Screen()  # 实例化Screen类
#     p = Pattern()
#     return s,p

# class sikuli():
def click(n,img,sim=0.7):
    sikuli = Sikuli()
    s = sikuli.screen()
    p = sikuli.pattern()
    if type(n) == int:
        for i in range(n):
            if s.exists(img):
                s.click(p(img).similar(sim))
                # jpype.shutdownJVM()
                break
            else:
                time.sleep(1)
        else:
            # jpype.shutdownJVM()
            return False
    else:
        print("超时时间类型错误，请输入整数")
    return True

def doubleClick(n,img,sim=0.7):
    sikuli = Sikuli()
    s = sikuli.screen()
    p = sikuli.pattern()
    if type(n) == int:
        for i in range(n):
            if s.exists(img):
                s.doubleClick(p(img).similar(sim))
                # jpype.shutdownJVM()
                break
            else:
                time.sleep(1)
        else:
            # jpype.shutdownJVM()
            print("没有找到合适的图片！")
            return False
    else:
        print("超时时间类型错误，请输入整数")
    return True

def Find(n,img,sim=0.7):
    sikuli = Sikuli()
    s = sikuli.screen()
    p = sikuli.pattern()
    if type(n) == int:
        for i in range(n):
            if s.find(p(img).similar(sim)):
                # s.doubleClick(img)
                # jpype.shutdownJVM()
                break
            else:
                time.sleep(1)
        else:
            # jpype.shutdownJVM()
            print("没有找到合适的图片！")
            return False
    else:
        print("超时时间类型错误，请输入整数")
    return True

def hover(n,img,sim=0.7):
    sikuli = Sikuli()
    s = sikuli.screen()
    p = sikuli.pattern()
    if type(n) == int:
        for i in range(n):
            if s.exists(img):
                s.hover(p(img).similar(sim))
                # jpype.shutdownJVM()
                break
            else:
                time.sleep(1)
        else:
            # jpype.shutdownJVM()
            return False
    else:
        print("超时时间类型错误，请输入整数")
    return True

def exists(n,img,sim=0.7):
    sikuli = Sikuli()
    s = sikuli.screen()
    p = sikuli.pattern()
    if type(n) == int:
        for i in range(n):
            if s.exists(img):
                # return True
                break
            else:
                time.sleep(1)
        else:
            # jpype.shutdownJVM()
            return False
    else:
        print("超时时间类型错误，请输入整数")
    return True


# def exists(n,img, sim=0.7):
#     sikuli = Sikuli()
#     s = sikuli.screen()
#     p = sikuli.pattern()
#     if s.exists(img):
#         # jpype.shutdownJVM()
#         return True
#     else:
#         return False
# def ocr():
#     s = getJVM()
#     str = s.find(r"D:\wf\EmergUItest\Common\image\test.png").text()
#     # jpype.shutdownJVM()
#     print(str)

# if __name__ == '__main__':
     # ocr()