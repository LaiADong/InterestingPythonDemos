from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#ascii_char = list(chr(x) for x in range(32, 126))
# 将256灰度映射到70个字符上
def get_char(PixelVal):
    #print(type(PixelVal))
    gray = 0
    if type(PixelVal) == int:
        gray = PixelVal
    elif type(PixelVal) == tuple:
        if PixelVal[3] == 0:
            return ' '
        gray = int(0.2126 * PixelVal[0] + 0.7152 * PixelVal[1] + 0.0722 * PixelVal[2])
    else:
        return ' '
    length = len(ascii_char)
    

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]



if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):

            #print(im.getpixel((j,i)))
            txt += get_char(im.getpixel((j,i)))
        txt += '\n'

   # print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)

