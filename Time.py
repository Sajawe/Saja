import datetime
TodayDate = datetime.datetime.now()
Hours = TodayDate.strftime("%H")
Minutes = TodayDate.strftime("%m")
Seconds = TodayDate.strftime("%S")
Formatted = Hours +" hours, " + Minutes +" minutes and " + Seconds +" seconds"
print(Formatted)