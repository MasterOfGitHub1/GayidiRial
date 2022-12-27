import requests
from datetime import datetime as date
import matplotlib.pyplot as plt

weekdays_cte = ["دوشنبه","سه شنبه","چهارشنبه","پنج شنبه","جمعه","شنبه","یکشنبه"]

today = requests.get("https://bonbast-api.deta.dev/latest").json()
yesterday = requests.get("https://bonbast-api.deta.dev/archive/").json()
days = []
days.append(today)
days.append(yesterday)
d = yesterday["date"].split("-")
for i in range(5):
  days.append(requests.get("https://bonbast-api.deta.dev/archive?date="+d[0]+"-"+d[1]+"-"+str(int(d[2])-i-1)).json())
print(days)
  
usd = []
weekdays = []
weekdays.append(weekdays_cte[date.today().weekday()])
usd.append(days[0]["usd"]["sell"])
for i in range(6):
  dd = days[i+1]["date"].split("-")
  weekdays.append(weekdays_cte[date(int(dd[0]),int(dd[1]),int(dd[2])).weekday()])
  usd.append(days[i+1]["usd"]["sell"])
print(weekdays)
print(usd)
plt.plot(usd, weekdays)
  
# naming the x axis
plt.xlabel('قیمت دلار')
# naming the y axis
plt.ylabel('روز هفته')
  
# giving a title to my graph
plt.title('پروژه گاییدن ریال')
  
# function to show the plot
plt.savefig('foo.png')
