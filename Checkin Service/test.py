import calendar
import datetime
import time

def append_timestamp():
    timestamp = calendar.timegm(time.gmtime())
    human_readable = datetime.datetime.fromtimestamp(timestamp).isoformat()
    filename_withtimestamp =  str(human_readable)
    return filename_withtimestamp

print(append_timestamp())