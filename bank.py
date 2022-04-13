from asyncio.windows_events import NULL


class Bank():
  def __init__(self):
    self.users = []

  def create_account(self, account, name, deposit):
    user = {"Account" : account,
            "Name" : name,
            "Balance": deposit
            }
    self.users.append(user)
  
  def deposit(self, account, money):

    # Error : money 매개변수에 음수값 할당
    if money < 0:
      print("입금하시는 돈이 음수입니다. 양수로 다시 입력해주세요.")

    user = (user for user in self.users if user['Account'] == account)

    # Error : users dict 내 찾는 user가 없는 경우
    if user == None:
      print("해당 계좌번호를 가진 사용자가 없습니다.")
    
    user["Balance"] += money
    



