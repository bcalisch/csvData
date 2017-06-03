import calendar
def translateDate(theDate):
    year = str(theDate.year)
    theMonth = calendar.month_name[theDate.month].upper()[:3]
    theDay = str(theDate.day)
    return year+'-'+theMonth+'-'+theDay
