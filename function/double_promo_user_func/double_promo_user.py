def find_double_promo(user_ID, promo_A_status, promo_B_status):
    '''
    Find user ID that has double promo

    Parameters
    ----------
    user_ID: list
        List of user ID

    promo_A_status: list
        List of user ID that get promo A.
        1 = get promo
        0 = did not get promo

    promo_B_status: list
        List of user ID that get promo B.
        1 = get promo
        0 = did not get promo

    Returns
    -------
    double_ID: list
        List of user that get double promo.
        If None, return []
    '''

    num = 0 #define while parameter
    double_promo_user = [] #define double_promo_user

    '''
    the condition of 'if' expression is if the value of promo_A_status and promo_B_status is the same and also their value is 1, their count as double_promo_user

    '''
    while num < len(user_ID):
      if promo_A_status[num] == promo_B_status[num] and promo_A_status[num] == 1:
        double_promo_user.append(user_ID[num])

      num+=1
    return double_promo_user #return double_promo_user variable

