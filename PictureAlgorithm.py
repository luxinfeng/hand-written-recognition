import numpy as np
import sys


#Essential variable 基础变量
#Standard size 标准大小
N = 100
#Gray threshold 灰度阈值
color = 100 / 255 
n = 10


'''#读取原csv文件
reader = list(csv.reader(open('Database.csv',encoding = 'utf-8')))
#清除读取后的第一个空行
del reader [0]
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
testPic = OP.GetTrainPicture(testFiles)

#计算每一个待识别图片的可能分类
result = PA.CalculateResult(testPic,pic)
for item in result :
	for i in range(n):
		print('第'+str(i+1)+'个向量为'+str(item[i+n])+',距离为'+str(item[i]))'''


def CalculateDistance(test,train,num,n):
	'''计算每个图片前N个相似图片'''
	#前N个放距离，后N个放数字
	dis = np.zeros(2*n*len(test)).reshape(len(test),2*n)
	for i ,item in enumerate(test):
		#计算出每个训练图片与该待识别图片的距离
		itemDis = np.sqrt(np.sum((item-train)**2, axis=1))
		#对距离进行排序，找出前N个
		sortDis = np.sort(itemDis)
		dis[i,0:n] = sortDis[0:n]
		for j in range(n):
			#找到前几个在原矩阵中的位置
			maxPoint = list(itemDis).index(sortDis[j])
			#找到num对应位置的数字，存入dis中
			dis[i,j+n] = num [maxPoint]
	return dis


def CalculateResult(test,train):
	'''计算待识别图片test的可能分类'''
	#得到每个待识别图片前N相似图片
	testDis = 	CalculateDistance(test[:,0:	N**2],train[:,0:N**2],train[:,N**2],n)
	#将testDis变成列表
	tt = testDis.tolist()
	#输出每一个待识别图片的所有前N个
	#for i in tt: 
	#	for j in i:
	#		print(j)
	return tt 
