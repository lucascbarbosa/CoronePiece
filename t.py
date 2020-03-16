from datetime import datetime as dt

tdate = dt.now()

print("Created at {:d}:{:02d}".format(tdate.hour, tdate.minute))