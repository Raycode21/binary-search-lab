class Binary_search(object):
    def __init__(self,size,step):
        self.size = size
        self.step = step
        #methods to create lists
        if self.size in self.toTwenty():
           self.number_list = toTwenty()

        elif self.size in self.toForty():
            self.number_list = toForty()

        elif self.size in self.toOneThousand():
           self.number_list = self.toOneThousand()

           self.length = len(self.number_list)
            #getter method to return self as list
    def __getitem__(self, index):
        return self.number_list[index]

    def toTwenty(self):
        return [n for n in range(1, 21)]
    def toForty(self):
        return [n for n in range(2, 41, 2)]
    def toOneThousand(self):
        return [n for n in range(10, 1001, 10)]
              #binary search
    def search(self, number):
        first_index = 0
        last_index = len(number_list)-1
        count = 0
        index = -1
        found = False
    if number == self.number_list[first_index]:
       index = first_index
       found = True
    if number == self.number_list[last_index]:
       index = last_index
       found = True
    while first_index <= last_index and found == False:
          count += 1
          midpoint= (first_index + last_index)//2
    if number == self.number_list[midpoint]:
       found = True
    return {'count':count, 'index':midpoint}
    if midpoint < number:
            first_index = midpoint + 1
    elif midpoint > number:
            last_index = midpoint -1
    return {'count':0,'index':index}
