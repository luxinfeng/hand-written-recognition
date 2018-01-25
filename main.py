import os
import OperatePicture as OP
import OperateDatabase as OD 
import PictureAlgorithm as PA 
import csv
import codecs

#Essential variable 基础变量
#Standard size 标准大小
N = 100
#Gray threshold 灰度阈值
color = 100 / 255 
n = 10

#读取原csv文件
#fp = open ("Database.csv",'w')
#codecs.encode('Database.csv', encoding='utf-8', errors='strict')
reader = list(csv.reader(open('Database.csv',encoding = 'utf-8')))
#清除读取后的第一个空行
del reader[0]
#读取num目录下的所有文件名
fileNames = os.listdir(r"./num/")
#对比fileNames与reader，得到新增的图片newFileNames
newFileNames = OD.NewFiles(fileNames,reader)
print('New picture are : ',newFileNames)
#得到newFileNames对应的矩阵
pic = OP.GetTrainPicture(newFileNames)
OD.SaveToCSV(pic ,newFileNames)
#将原数据库矩阵与新数据库矩阵合并
pic = OD.Combination(reader ,pic)


#得到待识别图片
testFiles = os.listdir(r"./test/")
testPic = OP.GetTestPicture(testFiles)
#计算每一个待识别图片的可能分类
result = PA.CalculateResult(testPic,pic)
for i,item in enumerate(result) :
	print(testFiles[i])
	for i in range(n):
		print('第'+str(i+1)+'个向量为'+str(item[i+n])+',距离为'+str(item[i]))
