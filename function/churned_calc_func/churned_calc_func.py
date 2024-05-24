'''
- Given a userID and its subscription status, this is a function to determine the number of churned (unsubscribed user) on a specific month
'''
def calculate_churned(user_data, month):
  '''
  Function to determine the number of churned (unsubscribed user) on a specific month

  Parameters
  ----------
  user_data : list
    contains the userId and subscribe until ...
  month : string
    contains month to determine the churned user

  Returns
  --------
  churned : int
      contains the number of churned user before month
  '''

  churned = 0 # output variable

  # reference variable to convert month into int/number
  month_dict = {'January' : 1,
                'February' : 2,
                'March' : 3,
                'April' : 4,
                'May': 5,
                'June': 6,
                'July': 7,
                'August': 8,
                'September':9,
                'October': 10,
                'November': 11,
                'December': 12
                }
  num_month = month_dict[month] # convert month variable into int with reference variable

  # code for calculate churned user in user_data
  for username, subscribe in user_data:
    num_subscribe = month_dict[subscribe] # convert user subscribe variable from user_data into int with reference variable

    if num_subscribe < num_month:
      churned += 1

  return churned # return churned variable