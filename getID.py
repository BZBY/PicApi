import os
filePath = r'./'
# for i,j,k in os.walk(filePath):
#     print(i,j,k)
#os.walk可以用于遍历指定文件下所有的子目录、非目录子文件。
startFile = os.listdir(filePath)
for i in startFile:
    if i.find("Pic_") == 0:
        pics = os.listdir(i+r"/")
        print(pics)
        for ii in pics:
            with open("img.txt",'a',encoding='utf-8') as f:
                strs  = 'https://raw.githubusercontent.com/BZBY/PicApi/main/'+i+r"/"+ii
                f.write(strs)
                f.write("\n")