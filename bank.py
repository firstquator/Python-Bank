from curses.ascii import isdigit
from re import search

class Bank():
  def __init__(self):
    self.users = []

  def create_account(self, account: str, name: str, deposit: float):
    # Error : 잘못된 account 형식 전달
    if not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      return -1

    # Error : 잘못된 name 형식 전달
    if search('/d', name):
      print("잘못된 형식의 이름을 전달했습니다 : 이름 내 숫자가 포함되어 있습니다.")
      return -1

    # Error : 잘못된 deposit 형식 전달
    if deposit < 0:
      print("입금하신 금액이 올바르지 않습니다 : 음수 입력")
      return -1

    user = {"Account" : account,
            "Name" : name,
            "Balance": deposit
            }

    self.users.append(user)
  
  def deposit(self, account: str, money: float):

    # Error : money 매개변수에 음수값 할당
    if money < 0:
      print("입금하시는 돈이 음수입니다. 양수로 다시 입력해주세요.")
      return -1

    user = (user for user in self.users if user['Account'] == account)

    # Error : users dict 내 찾는 user가 없는 경우
    if user == None:
      print("해당 계좌번호를 가진 사용자가 없습니다.")
      return-1
    
    print(f'계좌번호 : {user["Account"]}')
    print(f'이름 : {user["Name"]}')
    print(f'잔액 : {user["Balance"]}')

    user["Balance"] += money
    
  


