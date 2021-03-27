# Faster than Merge but cannot handle duplicate, maybe can add that feature hence Lecture Slides never teach 

newlist = [10,5,8,12,15,6,3,9,16]
low = 0
high = len(newlist)-1


def quickSort(newlist):
    low = 0
    high = len(newlist)-1
    quickSortHelper(low, high, newlist)

def quickSortHelper(low, high, newlist):
    if (high>low):
        j = partition(low, high, newlist)
        quickSortHelper(low, j-1, newlist)
        quickSortHelper(j+1, high, newlist) 

def partition(low, high, newlist):
    pivot = newlist[low]
    i = low + 1
    j = high
    done = False

    while done == False: 

        while pivot > newlist[i] and i<j:
            i += 1
        
        while pivot <= newlist[j] and j>=i:
            j -= 1
        
        if j > i:
            newlist[i], newlist[j] = newlist[j], newlist[i]
        else:
            done = True 
    
    newlist[low], newlist[j] = newlist[j], newlist[low]
    return j

quickSort(newlist)
print(newlist)
