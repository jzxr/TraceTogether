#Ref: 
#https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/search/InterpolationSearch.java
#https://www.geeksforgeeks.org/interpolation-search/

#For uniform distrubtion list.
#Worst Case O(n)
#Avearge Case O(log(log(n)))

#When element to be search si closer to data[hi]
# mid value ideally is higher opposite if element is closer to data[lo]

#Formula for mid:
# Let's assume that the elements of the array are linearly distributed. 

# General equation of line : y = m*x + c.
# y is the value in the array and x is its index.

# Now putting value of lo,hi and x in the equation
# arr[hi] = m*hi+c ----(1)
# arr[lo] = m*lo+c ----(2)
# x = m*pos + c     ----(3)

# m = (arr[hi] - arr[lo] )/ (hi - lo)

# subtracting eqxn (2) from (3)
# x - arr[lo] = m * (pos - lo)
# lo + (x - arr[lo])/m = pos
# pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])

class interpolationSearch:

    def __init__(self, sortedData, value):
        self.data = sortedData
        self.value = value

    def search(self):
        lo = 0
        mid = 0
        hi = len(self.data) - 1

        while (self.data[lo] <= self.value and self.data[hi] >= self.value):

            mid = lo + ((self.value - self.data[lo]) *(hi - lo)) / (self.data[hi] - self.data[lo])
            mid = int(mid)

            if(self.data[mid] < self.value):
                lo = mid + 1
            elif (self.data[mid] > self.value):
                hi = mid - 1
            else:
                return mid

        if (self.data[lo]==self.value):
            return lo

        return None

# data = [10, 20, 25, 35, 50, 70, 85, 100, 110, 120, 125]
# test = interpolationSearch(data,25)
# print(test.search())