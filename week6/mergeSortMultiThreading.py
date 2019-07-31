import sys
import threading

maximumSize = 20
threadCount = 0
threadsArr = []

# function passed on to thread when thread is started
def merge_sort(A, threadCount):
    # Because we are limiting the size of the array to 20 and we are limiting
    # the number of threads to four, we want to sort 4 equal intervals of our
    # array (one in each thread). 0-4 (first-last), 5-9 (first-last), 10-14 (first-last),
    # 15-19 (first-last)
    first = threadCount * (int(maximumSize/4))
    last = (threadCount + 1) * (int(maximumSize/4))- 1
    # pass in the Array (we will be modifiying it), first and last of interval
    merge_sort2(A, first, last)

def merge_sort2(A, first, last):
    # if the array larger than 1 element then
	if first < last:
        # calculate the middle index of that array
		middle = (first + last)//2
        # pass the Array, first and middle index of the interval
        # and in doing so split the interval into two sub intervals (left and right)
		merge_sort2(A, first, middle) # sort left subinterval
		merge_sort2(A, middle + 1, last) # sort the right subinterval
		merge(A, first, middle, last) # then merge those two sorted subintervals

def merge(A, first, middle, last):
    # split the Array into left and right subintervals
	L = A[first:middle+1]
	R = A[middle+1:last+1]
	L.append(sys.maxsize) # appends number to mark the ending of left subinterval
	R.append(sys.maxsize) # appends number to mark ending of right subinterval
	i = j = 0

    # idea is to start with a base case, which is when the elements are broken
    # down into lists with single elements, then you compare the left and right lists.
    # loop through the number of elements in the interval
	for k in range (first, last+1):
        # if value in the left interval is smaller than value in right interval then
        # A[k] will be replaced with that value and we move on to the next left
        # interval value
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1

        # otherwise A[k] will be replaced with the right interval value and we move
        # on to the next right interval value
		else:
			A[k] = R[j]
			j += 1

# code to setup and call merge sort functions
A = [5, 1, 100, 4, 3, 200, 0 , 15, 300, 4, 5, 8, 40, 32, 25, 50, 9, 79, 27, 10]

# for loop that initiates each thread, 4 threads are chosed because of the number of
# cores my processor contains
for i in range(4):
    # merge_sort and merge_sort arguments get passed to new thread
    thread = threading.Thread(target = merge_sort, args = (A, threadCount))
    thread.start()
    print(thread)
    # append the threadsArr list so that we can stop and join them once they're
    # done with their tasks
    threadsArr.append(thread)
    # thread keeps track of the thread we are currently on
    threadCount = threadCount + 1
    #print('pringting thread:', threadsArr)

# .join means that your main thread waits until the given thread finishes
# continuing to execute. This gets done after threads are started
for j in threadsArr:
    j.join()

# merging the 4 threads
# interval(0, 4, 9)
merge(A, 0, int(((maximumSize/2) - 1)/2), int((maximumSize/2) - 1 ))
# interval(10, 14, 19)
merge(A, int(maximumSize/2), int((maximumSize/2) + ((maximumSize - 1 - (maximumSize/2))/2)), int(maximumSize - 1))
# interval(0, 9, 19) 
merge(A, 0, int((maximumSize - 1)/ 2), int(maximumSize - 1))
print(A)
