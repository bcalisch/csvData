import pymysql
import pymysql.cursors

#Create function that takes a dictionary and makes a list from it.
def getKeys(columns):
    theList = []
    for item in columns:
        for key in item:
            theList.append(item[key])
    return theList

#connect to DB
def getConnection():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='baseball',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection
def getColumns(tableName):
    connection = getConnection()
    columns =[]
    try:
        with connection.cursor() as cursor:
            sql = "select column_name from information_schema.columns where"
            sql += " table_name = %s"
            cursor.execute(sql,(tableName,))
            result = cursor.fetchall()
            columns = getKeys(result)
    finally:
        connection.close()
        return columns

def prettyList(theList):
    theString = ""
    theCount = 0
    if len(theList) > 0:
        theString += "'"+theList[theCount]+"'"
        theCount += 1
        while theCount < len(theList) -1:
            theString += ", '"+ theList[theCount]+"'"
            theCount += 1
    return theString

def insertRecord(sql):
    connection = getConnection()
    try:
        with connection.cursor() as cursor:
        #Try to insert the records in the insert
            cursor.execute(sql);
            connection.commit()
    except Exception as  e:
        print(sql)
        print(e)
    finally:
        connection.close()

def getValue(tableName, fieldName, value):
    """Send back appropriate value given table name and value"""
    theType = ''
    if value == '':
        return 'NULL'
    else:
        connection = getConnection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE "
                sql += "table_name = %s AND COLUMN_NAME = %s;"
                cursor.execute(sql,(tableName, fieldName))
                result = cursor.fetchone()
                theType = result.get('DATA_TYPE')
        finally:
            connection.close()
        if theType > '':
            if  theType == 'varchar':
                return "'"+value+"'"
            elif theType == 'datetime' or theType == 'date':
                return "STR_TO_DATE('"+value+"', '%m/%d/%Y %r')"
        return value

