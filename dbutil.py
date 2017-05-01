#import pymysql
#import pymysql.cursors
import pymssql
#import pymssql.cursors

#Create function that takes a dictionary and makes a list from it.
def getKeys(columns):
    theList = []
    #print(columns)
    theDict = {}
    for item in columns:
        #theDict = {item['COLUMN_NAME']:item['Data_type']}
        theDict[item['COLUMN_NAME']] = item['Data_type']
        #theList.append(dict)
        #print('This thing: '+item['COLUMN_NAME'] + ': '+ item['Data_type'])
       #for key in item:
            #print(key)
         #   theList.append(dict(item[key]))
    return theDict

#connect to DB
def getConnection():
    connection = pymssql.connect(server='Delphi6vm\TGISQLEX',
                                 user='tgia8',
                                 password='tgi95a8!',
                                 database='Autumn8')

    #Use this for MYSQL
    """pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='baseball',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
                                """
    return connection
def getColumns(tableName):
    connection = getConnection()
    columns =[]
    verboseCol = []
    try:
        #with connection.cursor() as cursor:
        with connection.cursor(as_dict=True) as cursor:
            sql = "select COLUMN_NAME, Data_type from information_schema.columns where"
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

def insertRecord(tableName, sql):
    connection = getConnection()
    try:
        sql = addIdentityCheck(tableName,sql)
        with connection.cursor() as cursor:
        #Try to insert the records in the insert
            cursor.execute(sql)
            connection.commit()
            
    except Exception as  e:
        print(sql)
        print(e)
    finally:
        connection.close()

def getValue(theType, value):
    """Send back appropriate value given table name and value"""
    #print(theType + ': '+ value)
    #theType = ''
    #print(theType)
    if value == '':
        return 'NULL'
    else:
        """connection = getConnection()
        try:
            with connection.cursor(as_dict = True) as cursor:
                sql = "SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE "
                sql += "table_name = %s AND COLUMN_NAME = %s;"
                cursor.execute(sql,(tableName, fieldName))
                result = cursor.fetchone()
                theType = result.get('DATA_TYPE')
        finally:
            connection.close()"""
        if theType > '':
            if  theType == 'varchar' or theType == 'char' or theType =='nvarchar':
                return "'"+value.strip().replace("'", '')+"'"
            elif theType == 'datetime' or theType == 'date':
                return "'"+value.strip()+"'"
                #return "STR_TO_DATE('"+value+"', '% m/%d/%Y %r')"
            elif theType == 'bit':
                if value == 'true':
                    #print('yes its true')
                    return '1'
                else:
                    return '0'
            elif theType =='time':
                return "'"+value+"'"
        return value.strip()
def addIdentityCheck(tableName,sql):
    """adds check for identity and puts in code correctly"""
    query = """if exists(SELECT      OBJECT_NAME(OBJECT_ID) AS TABLENAME 
                FROM     SYS.IDENTITY_COLUMNS 
                WHERE OBJECT_NAME(OBJECT_ID) = '{0}')
                begin
                    set identity_insert [{0}] on;
                    {1}
                    set identity_insert [{0}] off;
                end else
                begin
                    {1}
                end"""
    return query.format(tableName, sql)

