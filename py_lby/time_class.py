
class Time:
	'''Represents the time of day.

	attributes: hour, minute, second
	'''

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(t):
	'''
        print time. format: hour:minute:second
        '''
	print( 'time is %.2d:%2d:%2d' % (t.hour,t.minute, t.second))
	
print_time(time)
time2 = Time()
time2.hour = 13
time2.minute = 26
time2.second = 3
print(time2)
print_time(time2)

def is_after(t1,t2):
    t1num = int(str(t1.hour)+str(t1.minute)+str(t1.second))
    t2num = int(str(t2.hour)+str(t2.minute)+str(t2.second))
    while t1num>t2num:
            return True
    return False

print( is_after(time,time2))
print( is_after(time2,time))
