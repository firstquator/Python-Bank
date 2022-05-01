from re import search
from datetime import datetime

def display_user_info(user: dict, sep: str):
  count = 0
  for key in user:
    if(count != 3):
      print(f'{key} : {user[key]} {sep}', end = '')
    else:
      print(f'{key} : {user[key]} 원', end = '')
    count += 1

    if(count == 4): 
      break
  print('\n', end = '')

def check_duplication(accounts: list, account: str) -> bool:
  if account in accounts:
    return True
  else:
    return False

def find_user_index(accounts: list, account: str) -> int:
  try:
    user_index = accounts.index(account)
  except ValueError:
    user_index = None
      
  # Error : users dict 내 찾는 user가 없는 경우
  if user_index == None:
    print("해당 계좌번호를 가진 사용자가 없습니다.")
    return -1
  
  return user_index

def create_history(message: str) -> str:
  return datetime.today().strftime("%Y/%m/%d %H:%M:%S \t") + message

class Bank():
  bank_list = ['카카오뱅크', 'NH농협', 'KB국민', '우리은행', '신한은행', '하나은행', '부산은행', '새마을금고', 'SC제일']

  def __init__(self):
    self.users = []
    self.accounts = []

  # ================= 계좌생성 method =================
  def create_account(self):
    print("======계좌개설======")
    index = 1
    for bank_name in Bank.bank_list:
      print(f"{index} : {bank_name}", end = " ")
      index += 1
    print("\n")

    bank_index = input("개설하실 은행이름 번호를 입력하세요 : ")
    # Error : 잘못된 bank_index 형식 전달
    while not bank_index.isdigit():
      print("올바른 은행번호를 입력해주세요. - 숫자 입력")
      bank_index = input("개설하실 은행이름 번호를 입력하세요 : ")
    # Error : 범위를 벗어난 bank_index 형식 전달
    while int(bank_index) < 0 or int(bank_index) > len(Bank.bank_list):
      print("올바른 은행번호를 입력해주세요. - 범위 내 번호 입력")
      bank_index = input("개설하실 은행이름 번호를 입력하세요 : ")
    
    bank_name = Bank.bank_list[int(bank_index) - 1]
    account = input("계좌번호 : ")
    name = input("이름 : ")
    money = input("예금 : ")

    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")

    # Error : 중복된 계좌번호
    while check_duplication(self.accounts, account):
      print("이미 있는 계좌번호입니다.")
      account = input("계좌번호 : ")

    # Error : 잘못된 name 형식 전달
    while search('[0-9]', name):
      print("잘못된 형식의 이름을 전달했습니다 : 이름 내 숫자가 포함되어 있습니다.\n")
      name = input("이름 : ")

    # Error : 잘못된 deposit 형식 전달
    while not money.isdigit() or int(money) < 0:
      print("입금하신 금액이 올바르지 않습니다 : 음수 입력\n")
      money = int(input("예금 : "))

    # 사용 내역 저장 리스트 생성
    history = []
    user = {
      "은행명" : bank_name,
      "계좌번호" : account,
      "이름" : name,
      "잔액": int(money),
      "사용내역" : history 
    }

    mes = create_history(f'+{money}원 입금\t 잔액 : {user["잔액"]}원')
    user["사용내역"].append(mes)

    self.accounts.append(account)
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

    user_index = find_user_index(self.accounts, account)
    if user_index < 0:
      return

    user = self.users[user_index]

    # 현재 사용자 정보 보여주기
    display_user_info(user, '\n')

    money = input("입금하실 금액을 입력해주세요 : ")
    # Error : 잘못된 money 입력
    while not money.isdigit() or int(money) < 0:
      print("입금하신 금액이 올바르지 않습니다.\n")
      money = input("예금 : ")
    
    user["잔액"] += int(money)

    mes = create_history(f'+{money}원 입금\t 잔액 : {user["잔액"]}원')
    user["사용내역"].append(mes)

    # Display
    print(f'##계좌잔고: {user["잔액"]} 원##')
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
    
    user_index = find_user_index(self.accounts, account)
    if user_index < 0:
      return

    user = self.users[user_index]

    # 현재 사용자 정보 보여주기
    display_user_info(user, '\n')

    money = input("출금하실 금액을 입력해주세요 : ")
    # Error : 잘못된 money 입력
    while not money.isdigit() or int(money) < 0:
      print("입금하신 금액이 올바르지 않습니다 : 음수 입력\n")
      money = input("예금 : ")

    
    # Error : 계좌 내 금액보다 더 많은 돈을 출금했을 경우
    while user["잔액"] - int(money) < 0:
      print("계좌 내 금액보다 큰 값의 금액을 입력하셨습니다.")
      money = input("출금하실 잔액을 입력해주세요 : ")

    user["잔액"] -= int(money)
    mes = create_history(f'-{money}원 출금\t 잔액 : {user["잔액"]}원')
    user["사용내역"].append(mes)

    # Display
    print(f'##계좌잔고: {user["잔액"]} 원##')
    print("##출금이 완료되었습니다##")
    print("================")


  # =================== 조회 method ===================  
  def inquiry(self):
    print("======전체 조회======")
    for user in self.users:
      display_user_info(user, '/ ')
    print("====================")

  # =============== 사용내역 조회 method ===============  
  def view_history(self):
    print("====사용내역 조회====")
    account = input("조회하실 계좌번호를 입력해주세요 : ")

    # Error : 잘못된 account 형식 전달
    while not account.isdigit():
      print("잘못된 형식의 계좌번호입니다.")
      account = input("계좌번호 : ")
    
    user_index = find_user_index(self.accounts, account)
    if user_index < 0:
      return

    user = self.users[user_index]

    # 현재 사용자 정보 보여주기
    display_user_info(user, '\n')

    for mes in list(reversed(user["사용내역"])):
      print(mes)