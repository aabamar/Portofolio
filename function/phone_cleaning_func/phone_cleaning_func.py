
def clean_phone_number(phone_list):
    '''
    Function to clean the phone number

    Parameters
    ----------
    phone_list : list
        The raw sample of phone data

    Returns
    -------
    phone_clean : list
        The clean sample of phone data
    '''
    
    phone_clean = [] #define phone_clean list variable

    for phone_number in phone_list: #code for determine the data had 11 number or not, for filtering invalid number
      if len(phone_number) < 11: #code for define invalid number in the data
        phone_number = 'Invalid Number'
        phone_clean.append('Invalid Number')
      else: #code for clean valid data and insert data into phone_clean list with additional '62'
        phone_number = phone_number.replace(" ", "").replace("-", "").replace("+", "")
        phone_clean.append(int('62' + phone_number[-11:]))

    return phone_clean #return phone_clean variable