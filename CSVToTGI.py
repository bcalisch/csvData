from listMaker import *
import os

dir = 'C:\\tgi\\bin\\CSV\\2012 Export\\a8Test'#C:\tgi\Bin\CSV\2012 Export\a8
for root, dirs, filenames in os.walk(dir):
	for f in filenames:
		tableName = f.split('.')[1]
		directory = root+'\\'+f
		print(tableName + ' | ' + root+'\\'+f)
		listObj = listFromCSV(directory, tableName)
		listObj.insertRecords()