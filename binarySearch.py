class binarySearch(object):

    def __init__(self,size,step):
        self.size = size
        self.step = step

        #methods to create lists
        if self.size in self.toTwenty():
            self.number_list = self.toTwenty()

        elif self.size in self.toForty():
            self.number_list = self.toForty()

        elif self.size in self.toOneThousand():
            self.number_list = self.toOneThousand()

        self.length = len(self.number_list)

            #getter method to return self as list
    def __getitem__(self, index):
        return self.number_list[index]
#methods defined that will return list using list comprehension
    def toTwenty(self):
        return [n for n in range(1, 21)]
    def toForty(self):
        return [n for n in range(2, 41, 2)]
    def toOneThousand(self):
        return [n for n in range(10, 1001, 10)]
              #binary search methods
              #checks if the number is at the beginning or end of list
    def search(self, number):
        first_index = 0
        last_index = len(self.number_list)-1
        count = 0
        index = -1
        found = False
        if number == self.number_list[first_index]:
            index = first_index
            found = True
        if number == self.number_list[last_index]:
            index = last_index
            found = True
         #divides the list into two checks if the midpoint matches our number
        while first_index <= last_index and not found:
            count += 1
            midpoint = (first_index + last_index)//2
        if number == self.number_list[midpoint]:
            found = True
        print ({'count':count, 'index':midpoint})

        if midpoint < number:
            first_index = midpoint + 1
        elif midpoint > number:
            last_index = midpoint -1
        print ({'count':0, 'index':index})
