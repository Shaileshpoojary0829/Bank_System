class Bank:
  def __init__(self):
      self.accounts = {}  # to store username and account details
      self.logged_in_user = None

  def add_account(self, username, password, initial_balance):
      self.accounts[username] = {'password': password, 'balance': initial_balance}

  def login(self, username, password):
      if username in self.accounts:
          if self.accounts[username]['password'] == password:
              self.logged_in_user = username
              print(f'\nLogin Successfull!!\nWelcome, {username}!')
              self.show_operations_menu()
          else:
              print('Invalid password')
      else:
          print(f'Username {username} not found. Please register first.')

  def register(self):
      username = input('Enter username: ')
      if username in self.accounts:
          print('Username already exists. Please choose another username.')
          return

      password = input('Enter password: ')
      while True:
          try:
              initial_balance = float(input('Enter initial balance: ₹'))
              break
          except ValueError:
              print('Invalid input. Please enter a valid number.')

      self.add_account(username, password, initial_balance)
      print(f'Account created successfully for {username} with an initial balance of ₹{initial_balance:.2f}')

  def show_balance(self):
      if self.logged_in_user:
          print(f'Balance: ₹{self.accounts[self.logged_in_user]["balance"]:.2f}')
      else:
          print('You are not logged in.')

  def deposit(self, amount):
      if amount > 0:
          if self.logged_in_user:
              self.accounts[self.logged_in_user]['balance'] += amount
              print(f'Deposit of ₹{amount:.2f} was successful.')
              self.show_balance()
      else:
          print('Deposit amount must be positive.')

  def withdraw(self, amount):
      if amount > 0:
          if self.logged_in_user:
              if self.accounts[self.logged_in_user]['balance'] >= amount:
                  self.accounts[self.logged_in_user]['balance'] -= amount
                  print(f'Withdrawal of ₹{amount:.2f} was successful.')
                  self.show_balance()
              else:
                  print('Insufficient funds.')
      else:
          print('Withdrawal amount must be positive.')

  def logout(self):
      self.logged_in_user = None
      print('Logged out successfully')

  def show_operations_menu(self):
      while True:
          print("\n===== Operations Menu =====")
          print("1. Deposit")
          print("2. Withdraw")
          print("3. Check Balance")
          print("4. Logout")
          choice = input("Enter your choice: ")

          if choice == '1':
              while True:
                  try:
                      amount = float(input('Enter amount to deposit: ₹'))
                      break
                  except ValueError:
                      print('Invalid input. Please enter a valid number.')
              self.deposit(amount)
          elif choice == '2':
              while True:
                  try:
                      amount = float(input('Enter amount to withdraw: ₹'))
                      break
                  except ValueError:
                      print('Invalid input. Please enter a valid number.')
              self.withdraw(amount)
          elif choice == '3':
              self.show_balance()
          elif choice == '4':
              self.logout()
              break
          else:
              print('Invalid choice. Please enter a valid option.')


if __name__ == "__main__":
  bank = Bank()

  while True:
      print("\n===== Main Menu =====")
      print("1. Register")
      print("2. Login")
      print("3. Exit")
      choice = input("Enter your choice: ")

      if choice == '1':
          bank.register()
      elif choice == '2':
          username = input('Enter username: ')
          password = input('Enter password: ')
          bank.login(username, password)
      elif choice == '3':
          print('Thank you for using our bank. Goodbye!!')
          break
      else:
          print('Invalid choice. Please enter a valid option.')