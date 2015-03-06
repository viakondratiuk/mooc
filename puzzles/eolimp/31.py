import datetime

dates = []
intervals = int(input())
for i in range(intervals):
    dates.append(input())

fridays = 0
for d in dates:
    years = list(map(int, d.split()))
    for year in range(years[0], years[1] + 1):
        for month in range(1, 13):
            if datetime.datetime(year, month, 13).weekday() == 4:
                fridays +=1
                
print(fridays)