# from PIL import Image
# def getText(img):
#     img = img.convert("L")  # 转为灰度图片
#     charlist = ''
#     for h in range(0, img.size[1]):
#         for w in range(0, img.size[0]):
#             gray = img.getpixel((w, h))  # 返回像素值，介于0-255之间256个
#             pos = gray / 256
#             charlist = charlist + codelist[int((count - 1) * pos)]  # 这里count-1是因为字符串索引是从0开始
#         charlist = charlist + '\r\n'  # 不同系统对应的换行符不一样\n-windows \r-Linux
#     return charlist
# def getImage():
#     # 取得图像
#     file = open(r"D:\123\ll.jpg", 'rb')
#     img = Image.open(file)
#     return img
# def trantxt():
#     # 输出到文本中去
#     outfile = open('tmp.txt', 'w')
#     outfile.write(getText(img))
#     outfile.close()
# if __name__ == '__main__':
#     img = getImage()
#     width, height = img.size[0], img.size[1]  # 0-width，1-height
#     codelist = """qwertyuiop[]asdfghjkl;'zxcvbnm,./`~!@#$%^&<()*+{}:"?> |"""
#     count = len(codelist)
#     scale = width / height  # 宽度与高度的比例，为了维护图像比例不要失真
#     img = img.resize((int(width * 0.2), int(width * 0.1 / scale)))  # 这里的0.1可以改成你喜欢的比例
#     trantxt()


import matplotlib.pyplot as plt
show_heigth = 100
show_width = 120
#这两个数字是调出来的

ascii_char = list("♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡.")
#生成一个ascii字符列表
char_len = len(ascii_char)

pic = plt.imread(r"D:\123\123.png", 'rb')
#使用plt.imread方法来读取图像，对于彩图，返回size = heigth*width*3的图像
#matplotlib 中色彩排列是R G B
#opencv的cv2中色彩排列是B G R

pic_heigth,pic_width,_ = pic.shape
#获取图像的高、宽

gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
#RGB转灰度图的公式 gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

#思路就是根据灰度值，映射到相应的ascii_char
for i in range(show_heigth):
    #根据比例映射到对应的像素
    y = int(i * pic_heigth / show_heigth)
    text = ""
    for j in range(show_width):
        x = int(j * pic_width / show_width)
        text += ascii_char[int(gray[y][x] / 256 * char_len)]
    print(text)
