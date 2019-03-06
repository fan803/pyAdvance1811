#-*- coding:utf-8 -*-
from PIL import Image
import argparse
#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')
#获取参数
args = parser.parse_args()
File = args.file

#ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char = list("MNHQ$OC?7>!:–;. ")

#将像素转换为ascii码
def get_char(r,g,b,alpha = 256):
    if alpha == 0:             #alpha=0,表示透明于是用‘’填充
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)#装换为灰度
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]  #将像素颜色映射为对应的ascii码

if __name__=='__main__':
    im = Image.open(File)#打开图片文件
    WIDTH = int(im.width/6)
    HEIGHT = int(im.height/15)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)#以低质量调整图片，使效果更明显
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pixel = im.getpixel((j,i))#获取像素点颜色信息，RGBA或者RGB
            if(len(pixel) == 4):
                txt += get_char(pixel[0],pixel[1],pixel[2],pixel[3])#为适应python3与python2之间的小改动
            else:
                txt += get_char(pixel[0],pixel[1],pixel[2])
        txt += '\n'
    print(txt)
    with open('output-test.txt','w') as f:#输出文件
            f.write(txt)
