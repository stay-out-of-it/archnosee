from datetime import datetime

iterations = 10**8

'''
#------------------------
count = 0 # initiate count variable
now = datetime.now() # time at start of program

while True:
	count += 1
	if count >= iterations:
		break

print('running time while 1 %s, %s ' % (str (count), str(datetime.now() - now)))

#------------------------
count = 0 # reset count to 0
now = datetime.now() # start time

while count < iterations:
	count += 1

print('running time while 2 %s, %s ' % (str (count), str(datetime.now() - now)))
'''
#-------------------------
c = 0 # this is a dummy variable set to zero - that the for loop has something to do
now = datetime.now()

for count in range(0, iterations+1):
	c += 1

print('running time for loop %s, %s ' % (str (count), str(datetime.now() - now)))


#-------------------------
c = 0 # this is a dummy variable set to zero - that the for loop has something to do
now = datetime.now()

c = [1 for count in range(0, iterations+1)]
c = sum(c)
print('running time for loop , %s ' % ( str(datetime.now() - now)))
