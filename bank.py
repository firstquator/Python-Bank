from curses.ascii import isdigit
from math import floor
from re import search

class Bank():
  def __init__(self):
    self.users = []

  # ================= 계좌생성 method =================
  def create_account(self):
    print("======계좌개설======\n")
    account = input("계좌번호 : ")
    name = input("이름 : ")
    money = input("예금 : ")

    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")

    # Error : 잘못된 name 형식 전달
    while search('/d', name):
      print("잘못된 형식의 이름을 전달했습니다 : 이름 내 숫자가 포함되어 있습니다.\n")
      name = input("이름 : ")

    # Error : 잘못된 deposit 형식 전달
    while not money.isdigit() or floor(int(money)) < 0:
      print("입금하신 금액이 올바르지 않습니다 : 음수 입력\n")
      money = int(input("예금 : "))

    user = {"Account" : account,
            "Name" : name,
            "Balance": floor(int(money))
            }

    self.users.append(user)

    print("##계좌개설을 완료하였습니다##")


  # =================== 입금 method ===================
  def deposit(self):
    print("======입금 하기======")
    account = input("입금하실 계좌번호를 입력해주세요 : ")

    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")

    user = (user for user in self.users if user['Account'] == account)

    # Error : users dict 내 찾는 user가 없는 경우
    if user == None:
      print("해당 계좌번호를 가진 사용자가 없습니다.")
      return-1
    
    print(f'계좌번호 : {user["Account"]}원')
    print(f'이름 : {user["Name"]}원')
    print(f'잔액 : {user["Balance"]}원')

    money = input("입금하실 금액을 입력해주세요 : ")

    # Error : 잘못된 money 입력
    while not money.isdigit() or floor(int(money)) < 0:
      print("입금하신 금액이 올바르지 않습니다.\n")
      money = input("예금 : ")
    
    user["Balance"] += floor(int(money))
    
    # Display
    print(f'##계좌잔고: {user["Balance"]} 원##')
    print("##입금이 완료되었습니다##")
    print("================")


  # =================== 출금 method ===================
  def withdraw(self):
    print("======출금 하기======")
    account = input("출금하실 계좌번호를 입력해주세요 : ")
    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")
    
    user = (user for user in self.users if user['Account'] == account)

    # Error : users dict 내 찾는 user가 없는 경우
    if user == None:
      print("해당 계좌번호를 가진 사용자가 없습니다.")
      return-1
    
    print(f'계좌번호 : {user["Account"]}')
    print(f'이름 : {user["Name"]}')
    print(f'잔액 : {user["Balance"]}')

    money = input("출금하실 금액을 입력해주세요 : ")

    # Error : 잘못된 money 입력
    while not money.isdigit() or floor(int(money)) < 0:
      print("입금하신 금액이 올바르지 않습니다 : 음수 입력\n")
      money = input("예금 : ")

    
    # Error : 계좌 내 금액보다 더 많은 돈을 출금했을 경우
    while user["Balance"] - floor(int(money)) < 0:
      print("계좌 내 금액보다 큰 값의 금액을 입력하셨습니다.")
      money = input("출금하실 잔액을 입력해주세요 : ")

    
    
    
    
