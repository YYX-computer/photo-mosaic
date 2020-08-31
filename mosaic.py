from PIL import Image
def _mosaic(img):
    s = img.size
    img = img.resize((10,10))
    img = img.resize(s)
    return img
def mosaic(img,fx,fy,tx,ty):
    c = img.crop((fx,fy,tx,ty))
    c = _mosaic(c)
    img.paste(c,(fx,fy,tx,ty))
    return img
if(__name__ == '__main__'):
    while(1):
        flag = False
        name = input('请输入文件名:')
        try:
            img = Image.open(name)
            flag = True
        except:
            print('无法读取文件')
        if(flag):
            break
    fx,fy,tx,ty = None,None,None,None
    while(1):
        flag = False
        name = input('请输入需要打马赛克的区域(x1,y1,x2,y2):')
        try:
            name = [int(i) for i in name.split(',')]
            if(len(name) != 4):
                raise ValueError
            fx,fy,tx,ty = name
            flag = True
        except:
            print('错误的格式')
        if(flag):
            break
    img = mosaic(img,fx,fy,tx,ty)
    while(1):
        cmd = input('处理完成,按1存储文件,按2显示文件,按3退出:')
        if(cmd == '1'):
            path = input('请输入存储路径:')
            try:
                img.save(path)
                exit()
            except:
                print('无法存储文件')
        elif(cmd == '2'):
            img.show()
        elif(cmd == '3'):
            exit()
        else:
            print('未知的命令:%s'%cmd)