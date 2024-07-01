import calendar as cal
from datetime import datetime
def find_thanksgiving(year):
    month = cal.monthcalendar(year,11)
    if month[0][cal.THURSDAY] !=0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving

def shopping_days(year):
    # datetimeに変換
    christmas = datetime(year,12,25)
    thanksgiving = datetime(year,11,find_thanksgiving(year))
    
    # 差を計算
    delta = christmas - thanksgiving
    
    return delta.days

print(shopping_days(2024))