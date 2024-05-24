class Data:

    '''
    class of given data

    parameters
    ----------
    data = given data
    size = length of data

    method
    ----------

    read_data = input given data to class
    find_total = calculate total sum of data
    find_average = calculate average of data


    '''
    def read_data(self, data): #define read_data method
      self.data = data
      self.size = len(data)

    def find_total(self): #define find_total method
      total = sum(self.data)
      return total

    def find_average(self): #define find_average method
      average = sum(self.data)/self.size
      return average

    pass