from dbutil import *

connection = getConnection()
connection.close()
tableName = "Adiag"
sql = "INSERT [dbo].[ADIAG] ([Casenum], [Priority], [ID], [Date], [Acct], [ICD9], [Description], [Expired], [CertifiedFrom], [CertifiedTo], [NumberVisits], [Visitsleft], [NumberWeeks], [WeeksLeft], [ICD10], [Description10], [Snomed], [DescriptionS], [LastModified], [Source], [NeedsICD10Attn], [Unspecified], [NoTen]) VALUES (N'0', 1, 3501, CAST(0xC72F0B00 AS Date), NULL, N'839.00', N'Cervical subluxation, unspecified', CAST(0x22300B00 AS Date), NULL, CAST(0xA0B20B00 AS Date), 1000, 1000, 500, 500, N'S13.101A  ', N'Dislocation of unspecified cervical vertebrae, init encntr', N'209037002      ', N'Closed dislocation cervical spine (disorder)                                                                                                                                                        ', NULL, NULL, NULL, 1, NULL)"
query = """if exists(
SELECT		OBJECT_NAME(OBJECT_ID) AS TABLENAME 
    FROM     SYS.IDENTITY_COLUMNS 
    WHERE OBJECT_NAME(OBJECT_ID) = {0})
    begin
		set identity_insert {0} on
		{1}
		set identity_insert {0} off
    end else
    begin
		{1}
    end"""


print(query.format(tableName, sql))