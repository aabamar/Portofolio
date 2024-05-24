def calculate_t_statistics(n, avg1, avg2, sd, alpha = 0.05):
    '''
    Function to clean the phone number

    Parameters
    ----------
    n : int
        Number of customer for each group
    avg1 : float
        Average spending for group 1
    avg2 : float
        Average spending for group 2
    sd : float
        Pooled standard deviation
    alpha : float
        alpha

    Returns
    -------
    t_statistics : float
        t-statistics
    '''
    # calculate t score with two-sample t-test formula
    t = (avg1-avg2) / (sd*(((1/n)+(1/n))**0.5))

    return t