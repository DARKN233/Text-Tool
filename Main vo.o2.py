import shutil #引入shutil模块进行文件的一些操作
import os #引入os模块进行文件的一些操作
import time #引入time 模块记录时间




def TextDeleted (path):#文件删除字符
    filelist=os.listdir(path)#用os.listdir读取文件，形成一个列表
    #print(path)#显示路径
    # print(filelist)
    for oldname in filelist:#用for循环列表
        OldName=path+'\\'+oldname#rename是目录的重命名，所以需要变成文件的路径
        newname=oldname.replace(deleted,'')#用replace删除需要删除的字符
        NewName=path+"\\"+newname
        os.rename(OldName,NewName)#这里是将修改后的名字替换
    print('重命名成功:删除字符')
    filelist2= os.listdir(path)  # 用os.listdir读取文件，形成一个列表
    print('修改后结果',filelist2)
    path=''#将输入的清空以便下次使用
    inp=''
    choose=''
    return


def TextAppend(path):#文件开头添加字符
    filelist = os.listdir(path)  # 用os.listdir读取文件，形成一个列表
    print('当前文件地址是',path)
    # print('文件列表',filelist)
    for oldname in filelist:  # 用for循环列表
        OldName = path + '\\' + oldname
        newname=Append+oldname#用字符串可以拼接的特性来进行命名
        NewName = path + "\\" + newname
        os.rename(OldName, NewName)  # 这里是将修改后的名字替换
    print('重命名成功:开头增加字符')
    filelist2 = os.listdir(path)  # 用os.listdir读取文件，形成一个列表
    print('修改后结果',filelist2)
    path=''
    inp=''
    choose=''
    return


def TextSubstitution(path):#文字的修改和开头增加(简单的文件重命名)
    filelist = os.listdir(path)  # 用os.listdir读取文件，形成一个列表
    print(path)
    # print(filelist)
    for oldname in filelist:  # 用for循环列表
        OldName = path + '\\' + oldname
        newname = Append+oldname#增加开头字符
        Newname = newname.replace(deleted, '')  # 用replace删除需要删除的字符
        NewName = path + "\\" + Newname
        os.rename(OldName, NewName)  # 这里是将修改后的名字替换
    filelist2 = os.listdir(path)  # 用os.listdir读取文件，形成一个列表
    print('修改后结果', filelist2)
    print('文件数量',len(filelist2))
    path = ''
    inp = ''
    choose = ''
    return


def FolderDeleted(path):#文件或者文件夹的删除
    judge = len(os.listdir(path))#读取所在文件夹下文件数量
    if judge == 0 :#如果没有文件删除文件夹
        judge2 = input('该文件夹为空文件夹，是否删除该文件夹? \n  是/否  \n')
        if judge2 in ['是']:
            os.rmdir(path)#用了os模块里的rmdir函数来删除文件夹(注意：要是文件夹李有文件会报错)
        else:
            print('未删除')
    elif judge != 0 :#如果有文件，删除指定文件
        FlieList = os.listdir(path)
        print('文件数为',len(FlieList))#显示当前文件夹的文件数量
        judge2 = input('该文件夹的内容为%s, \n 是否删除文件夹以及下面所有内容?   1.是/2.否' %(FlieList))#是否删除文件夹和里面的文件
        if judge2 in ['是','1','1.']:
            shutil.rmtree(path)#用了shutil模块里面的rmtree函数来删除
        elif judge2 in ['否','2','2.']:
            print('删除哪一个文件',FlieList)#显示当前文件夹的文件
            Delete = input('请输入要删除的文件(此时不支持删除文件夹):   ')
            path2= path+'\\'+Delete
            os.remove(path2)#用os模块里的remove函数来执行文件的删除
        print('该文件夹剩余文件为',os.listdir(path))#显示删除后的文件夹文件
        print('剩余文件数为',len(os.listdir(path)))#显示删除后的文件夹文件剩余数
        path = ''
        inp = ''
        choose = ''
        path2 = ''
        return



def NumberDeleted(path):#文件中数字删除
    filelist = os.listdir(path)#获取当前地址的文件列表
    print('当前目录下文件列表为',filelist)
    print('请输入要删除的数字区间')
    Deleted_Start = int(input('从'))#删除的数字从哪里开始
    Deleted_End = int(input('到'))#删除的树数字哪里结束
    judge = input('所要删除的带括号吗?   \n  1.带/2.不带')
    judge2 = input('请选择括号的种类(没有就回车):   1.（）/2.[]/3.{}')
    if judge in ['1','1.','带'] and judge2 in ['1','1.','()']:#下面的几个也是一样
        for Num in range(Deleted_Start, Deleted_End + 1):#range是会循环开始数字不会循环结束的数字的，要把转化成整数类型的结束数字加一
            DeletedNum = '('+ str(Num) + ')'#加入括号
            print("DeletedNum",DeletedNum)
            print('循环体内的文件列表',filelist)
            for file in filelist:
                Oldname = file
                Newname = file.replace(DeletedNum, '')#去除需要删除的部分
                # print(Newname)
                os.chdir(path)#将改名操作的运行目录改到需要的目录
                os.rename(Oldname,Newname)#改名操作
            print('数字去除成功')
            filelist = os.listdir(path)  # 获取当前地址的文件列表,循环体内的列表不断更新
            print('修改后结果',filelist)
            if Num == Deleted_End:
                break
            else:
                continue
            filelist = ''
            DeletedNum = ''
            path = ''
            inp = ''
            choose = ''
            return

    elif judge2 in ['2.','2','[]','[',']'] and judge in ['1','1.','带']:
        filelist = os.listdir(path)  # 获取当前地址的文件列表
        print('当前目录下文件列表为', filelist)
        print('请输入要删除的数字区间')
        Deleted_Start = int(input('从'))  # 删除的数字从哪里开始
        Deleted_End = int(input('到'))  # 删除的树数字哪里结束
        judge = input('所要删除的带括号吗?   \n  1.带/2.不带')
        judge2 = input('请选择括号的种类(没有就回车):   1.（）/2.[]/3.{}')
        if judge in ['1', '1.', '带'] and judge2 in ['1', '1.', '()']:  # 下面的几个也是一样
            for Num in range(Deleted_Start, Deleted_End + 1):  # range是会循环开始数字不会循环结束的数字的，要把转化成整数类型的结束数字加一
                DeletedNum = '[' + str(Num) + ']'  # 加入括号
                print("DeletedNum", DeletedNum)
                print('循环体内的文件列表', filelist)
                for file in filelist:
                    Oldname = file
                    Newname = file.replace(DeletedNum, '')  # 去除需要删除的部分
                    # print(Newname)
                    os.chdir(path)  # 将改名操作的运行目录改到需要的目录
                    os.rename(Oldname, Newname)  # 改名操作
                print('数字去除成功')
                filelist = os.listdir(path)  # 获取当前地址的文件列表,循环体内的列表不断更新
                print('修改后结果', filelist)
                if Num == Deleted_End:
                    break
                else:
                    continue
                filelist = ''
                DeletedNum = ''
                path = ''
                inp = ''
                choose = ''
                return

    elif judge in ['3','3.','{}','{','}'] and judge in ['1','1.','带']:
        filelist = os.listdir(path)  # 获取当前地址的文件列表
        print('当前目录下文件列表为', filelist)
        print('请输入要删除的数字区间')
        Deleted_Start = int(input('从'))  # 删除的数字从哪里开始
        Deleted_End = int(input('到'))  # 删除的树数字哪里结束
        judge = input('所要删除的带括号吗?   \n  1.带/2.不带')
        judge2 = input('请选择括号的种类(没有就回车):   1.（）/2.[]/3.{}')
        if judge in ['1', '1.', '带'] and judge2 in ['1', '1.', '()']:  # 下面的几个也是一样
            for Num in range(Deleted_Start, Deleted_End + 1):  # range是会循环开始数字不会循环结束的数字的，要把转化成整数类型的结束数字加一
                DeletedNum = '{' + str(Num) + '}'  # 加入括号
                print("DeletedNum", DeletedNum)
                print('循环体内的文件列表', filelist)
                for file in filelist:
                    Oldname = file
                    Newname = file.replace(DeletedNum, '')  # 去除需要删除的部分
                    # print(Newname)
                    os.chdir(path)  # 将改名操作的运行目录改到需要的目录
                    os.rename(Oldname, Newname)  # 改名操作
                print('数字去除成功')
                filelist = os.listdir(path)  # 获取当前地址的文件列表,循环体内的列表不断更新
                print('修改后结果', filelist)
                if Num == Deleted_End:
                    break
                else:
                    continue
                filelist = ''
                DeletedNum = ''
                path = ''
                inp = ''
                choose = ''
                return

    elif judge in ['2','2.','不带'] and judge2 in ['']:
        filelist = os.listdir(path)  # 获取当前地址的文件列表
        print('当前目录下文件列表为', filelist)
        print('请输入要删除的数字区间')
        Deleted_Start = int(input('从'))  # 删除的数字从哪里开始
        Deleted_End = int(input('到'))  # 删除的树数字哪里结束
        judge = input('所要删除的带括号吗?   \n  1.带/2.不带')
        judge2 = input('请选择括号的种类(没有就回车):   1.（）/2.[]/3.{}')
        if judge in ['1', '1.', '带'] and judge2 in ['1', '1.', '()']:  # 下面的几个也是一样
            for Num in range(Deleted_Start, Deleted_End + 1):  # range是会循环开始数字不会循环结束的数字的，要把转化成整数类型的结束数字加一
                DeletedNum =  str(Num)
                print("DeletedNum", DeletedNum)
                print('循环体内的文件列表', filelist)
                for file in filelist:
                    Oldname = file
                    Newname = file.replace(DeletedNum, '')  # 去除需要删除的部分
                    # print(Newname)
                    os.chdir(path)  # 将改名操作的运行目录改到需要的目录
                    os.rename(Oldname, Newname)  # 改名操作
                print('数字去除成功')
                filelist = os.listdir(path)  # 获取当前地址的文件列表,循环体内的列表不断更新
                print('修改后结果', filelist)
                if Num == Deleted_End:
                    break
                else:
                    continue
                filelist = ''
                DeletedNum = ''
                path = ''
                inp = ''
                choose = ''
                return


#def




# def NumberDeleted(path):#文件中数字删除
#     filelist = os.listdir(path)#获取当前地址的文件列表
#     print('当前目录下文件列表为',filelist)
#     print('请输入要删除的数字区间')
#     Deleted_Start = int(input('从'))#删除的数字从哪里开始
#     Deleted_End = int(input('到'))#删除的树数字哪里结束
#     judge = input('所要删除的带括号吗?   \n  1.带/2.不带')
#     judge2 = input('请选择括号的种类(没有就回车):   1.（）/2.[]/3.{}')
#     if judge in ['1','1.','带'] and judge2 in ['1','1.','()']:#下面的几个也是一样
#         for Num in range(Deleted_Start, Deleted_End + 1):#range是会循环开始数字不会循环结束的数字的，要把转化成整数类型的结束数字加一
#             DeletedNum = '('+ str(Num) + ')'#加入括号
#             print("DeletedNum",DeletedNum)
#             print('循环体内的文件列表',filelist)
#             for file in filelist:
#                 Oldname = file
#                 Newname = file.replace(DeletedNum, '')#去除需要删除的部分
#                 # print(Newname)
#                 os.chdir(path)#将改名操作的运行目录改到需要的目录
#                 os.rename(Oldname,Newname)#改名操作
#             print('数字去除成功')
#             filelist = os.listdir(path)  # 获取当前地址的文件列表,循环体内的列表不断更新
#             print('修改后结果',filelist)
#             if Num == Deleted_End:
#                 break
#             else:
#                 continue
#             filelist = ''
#             DeletedNum = ''
#             path = ''
#             inp = ''
#             choose = ''
#             return





































# 测试用
# path = 'C:\\Users\\111\\Desktop\\TEXTEWR'
# Append = 'E'
# deleted ='P'
# TextSubstitution(path)
# TextDeleted(path)
# TextAppend(path)
# FolderDeleted(path)
# NumberDeleted(path)










while True:
    print('使用说明')
    print('确认操作可以随意输入 \n 文件路径是文件夹路径')
    inp=input('确认操作:')#确认操作
    path=input('请输入路径:  ')#确认路径
    print('当前文件夹下的文件为',os.listdir(path))
    print('当前文件夹的文件数量为',len(os.listdir(path)))
    if inp != '' and path != '':
        choose=input('选择进行的操作： \n 1.删/2.增/3.修改/4.删除文件夹或者指定文件/5.删除文件名里面的数字     \n     ')#功能选择
        if choose in ['删','1','1.']:
            Time_begin = time.time()#计时开始
            deleted = input('需要删除的内容:   ')  # 要删除的内容
            TextDeleted(path)
            Time_end = time.time()#计时结束
            print('花费了',Time_end - Time_begin,'秒')
            confirm = input('还要继续使用吗？     1.是/2.否')
            if confirm in ['1','1.','是']:
                print('----------------------------------')
                continue
            elif confirm in ['2','2.','否']:
                break
            else:
                print('ERROR')
        elif choose in ['增','2','2.']:
            Time_begin = time.time()
            Append = input('需要开头增加的内容:   ')
            TextAppend(path)
            Time_end = time.time()
            print('花费了', Time_end - Time_begin, '秒')
            confirm = input('还要继续使用吗？     1.是/2.否')
            if confirm in ['1','1.','是']:
                print('----------------------------------')
                continue
            elif confirm in ['2','2.','否']:
                break
            else:
                print('ERROR')

        elif choose in ['3','3.','修改','修','改']:

            deleted = input('需要删除的内容:   ')  # 要删除的内容
            print('要删除的内容为',deleted)
            Append = input('需要开头增加的内容:   ')
            print('要添加的内容为',Append)
            Time_begin = time.time()
            TextSubstitution(path)
            Time_end = time.time()
            print('花费了', Time_end - Time_begin, '秒')
            confirm = input('还要继续使用吗？     1.是/2.否')
            if confirm in ['1','1.','是']:
                print('----------------------------------')
                continue
            elif confirm in ['2','2.','否']:
                break
            else:
                print('ERROR')

        elif choose in ['4','4.','删','删除','除']:
            Time_begin = time.time()
            FolderDeleted(path)
            Time_end = time.time()
            print('花费了', Time_end - Time_begin, '秒')
            break
        elif choose in ['5','5.',]:
            # print('此功能暂时不可用，正在努力修复bug中......')
            # confirm = input('是否返回?   1.是/2.否')
            # if confirm in ['1','1.','是']:
            #     continue
            # else:
            #     break
            Time_begin = time.time()
            NumberDeleted(path)
            Time_end = time.time()
            print('花费了', Time_end - Time_begin, '秒')
            confirm = input('还要继续使用吗？     1.是/2.否')
            if confirm in ['1','1.','是']:
                print('----------------------------------')
                continue
            elif confirm in ['2','2.','否']:
                break
            else:
                print('ERROR')
        elif inp in ['About','about']:
            print('Xenolies')
input()