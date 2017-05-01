import abc
import csv
from dbutil import *
import dbutil

class makeList(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, fileName, tableName):
        """Set FileName"""

    @abc.abstractmethod
    def printFile(self):
        """Prints out the file name"""
    @abc.abstractmethod
    def makeList(self):
        """Print out list from CSV FileName
            Return list"""
    @abc.abstractmethod
    def insertRecords(self):
        """Inserts records in CSV if they exist in columns"""


class listFromCSV(makeList):
    """Make a list from a CSV File"""
    def __init__(self, fileName, tableName):
        """Sets file name"""
        self.fileName = fileName
        self.tableName = tableName
        self.CSV = []
        self.columns = []
        self.prettyColumns = ''
        self.insertStatement = ''
        self.makeList()

    def insertRecords(self):
        """Assuming everything has been set, make insert statment
        using the CSV and COLUMNS """
        if  self.columns == {} or self.CSV == []:
            self.insertStatement = 'INVALID'
            return
        sql  = ''
        theCount = 0
        beginSQL = "insert into Autumn8.dbo.["+self.tableName+ "] "
        for row in self.CSV:
            columnSQL = "("
            valueSQL = "("
            for item, value in row.items():
                theValue = ''
                if item in self.columns.keys():
                    theValue = getValue(self.columns[item], value)
                    if columnSQL == "(":
                        #columnSQL = ", `"+ item+"`"
                        columnSQL +="["+item+"]"
                        valueSQL += theValue
                    else:
                        columnSQL += ", ["+ item+"]"
                        #columnSQL += ", `"+ item+"`"
                        valueSQL += ', '+ theValue
            columnSQL += ") VALUES "
            valueSQL += ")"
            sql += beginSQL + columnSQL + valueSQL+ '\n'

            if theCount > 2500:
                theCount = 0
                sql = ''
                print('Just did 2,500 for '+self.tableName)
            theCount +=1
        if sql > '':
            insertRecord(self.tableName, sql)
            #print(sql)
        

    def printFile(self):
        print(self.fileName)

    def makeList(self):
        """Using listFromCSV make dictionary with field and value"""
        theList = []
        try:
            reader = csv.DictReader(open(self.fileName))
            for row in reader:
                theList.append(row)
               # print(row)
            self.CSV = theList
            #print(self.tableName)
            self.columns = getColumns(self.tableName)
            #self.prettyColumns= prettyList(self.columns)
            #print(self.prettyColumns)
        finally:
            return


