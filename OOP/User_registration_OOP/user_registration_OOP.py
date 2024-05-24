from typing import List
class UserData:
    """
    A class to manage user data and counts.

    Attributes:
    - user_data (list): A list to store user data.
    - all_user (int): Total count of all users.
    - active_user (int): Count of active users.

    Methods:
    - summarize(): Prints a summary of total and active users.
    """
    user_data: List[dict] = []
    all_user: int = 0
    active_user: int = 0

    def summarize(self) -> None:
        """
        Prints a summary of total and active users.
        """
        print(f'Data summary\n------------')
        print(f'Number of all user    : {self.all_user}\nNumber of active user : {self.active_user}')

class RegistrationData(UserData):
    """
    A class to manage user registration by adding and deactivating users.
    Inherits from UserData to track user data and counts.

    Methods:
    - add_user(name: str, gender: str): Adds a new user with the provided name and gender.
    - deactivate_user(user_id: int): Deactivates a user by changing their status to 'inactive'.
    """

    def add_user(self, name: str, gender: str) -> None:
        """
        Adds a new user with the provided name and gender.
        Increments the total and active user counts.
        """
        user_id = len(UserData.user_data) + 1
        new_user_data = {'name': name, 'gender': gender, 'status': 'active'}
        UserData.all_user += 1
        UserData.active_user += 1
        UserData.user_data.append({'user_id': user_id, 'data': new_user_data})

    def deactivate_user(self, user_id: int) -> None:
        """
        Deactivates a user by changing their status to 'inactive'.
        Decrements the count of active users.
        """
        for user in UserData.user_data:
            if user['user_id'] == user_id:
                user['data']['status'] = 'inactive'
                UserData.active_user -= 1