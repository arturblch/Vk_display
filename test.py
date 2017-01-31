from datetime import datetime

def firstZero(num):
    if num < 10 :
        return '0'+str(num)
    else:
        return str(num)




now_time = datetime.now()
print('%s' % firstZero(now_time.hour))
print('%s' % firstZero(now_time.minute))

