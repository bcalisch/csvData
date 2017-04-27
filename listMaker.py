import abc
import csv
from dbutil import *

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
        if self.prettyColumns == '' or self.columns == [] or self.CSV == []:
            self.insertStatement = 'INVALID'
            return
        beginSQL = "insert into "+self.tableName+ " "
        for row in self.CSV:
            columnSQL = "("
            valueSQL = "("
            for item, value in row.items():
                theValue = ''
                if item in self.columns:
                    theValue = getValue(self.tableName,item,value)
                    if columnSQL == "(":
                        columnSQL +="`"+item+"`"
                        valueSQL += theValue
                    else:
                        columnSQL += ", `"+ item+"`"
                        valueSQL += ', '+ theValue
            columnSQL += ") VALUES "
            valueSQL += ")"
            sql = beginSQL + columnSQL + valueSQL
            #print(sql)
            insertRecord(sql)

    def printFile(self):
        print(self.fileName)

    def makeList(self):
        """Using listFromCSV make dictionary with field and value"""
        theList = []
        try:
            reader = csv.DictReader(open(self.fileName))
            for row in reader:
                theList.append(row)
            self.CSV = theList
            self.columns = getColumns(self.tableName)
            self.prettyColumns= prettyList(self.columns)
        finally:
            return


