def calc_weighted_avg(data, w):
    '''
    Function to calculate the weighted average of a list

    Parameters
    ----------
    data : list
        The sample data

    w : list
        The sample weights

    Returns
    -------
    avg : float
        The weighted average
    '''

    num = 0 #define while parameter
    avg = 0 #define weighted data average
    while num < len(data): #code for calculate average data weighted
      avg += (data[num] * w[num])
      num += 1

    return avg #return average value