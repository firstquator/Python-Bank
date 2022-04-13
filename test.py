from bank import Bank

while(True):
    print("======Bank Menu======")
    print("1. 계좌 계설")
    print("2. 입금 하기")
    print("3. 출금 하기")
    print("4. 전체 조회")
    print("5. 계좌 이체")
    print("6. 프로그램 종료")
    print("=====================")
    
    bank1 = Bank()

    btn = input("입력: ")
    while not btn.isdigit() or (int(btn) < 0 or int(btn) > 6) :
      print("1 ~ 6 사이 숫자를 입력해주세요.")
      btn = input("입력: ")
    
    if(btn == '6'):
      break
    elif(btn == '1'):
      bank1.create_account()
    elif(btn == '2'):
      bank1.deposit()
    elif(btn == '3'):
      bank1.withdraw()
    elif(btn == '4'):
      bank1.inquiry()

while(True):
    print("======Bank Menu======")
    print("1. 계좌 계설")
    print("2. 입금 하기")
    print("3. 출금 하기")
    print("4. 전체 조회")
    print("5. 계좌 이체")
    print("6. 프로그램 종료")
    print("=====================")
    
    bank2 = Bank()

    btn = input("입력: ")
    while not btn.isdigit() or (int(btn) < 0 or int(btn) > 6) :
      print("1 ~ 6 사이 숫자를 입력해주세요.")
      btn = input("입력: ")
    
    if(btn == '6'):
      break
    elif(btn == '1'):
      bank2.create_account()
    elif(btn == '2'):
      bank2.deposit()
    elif(btn == '3'):
      bank2.withdraw()
    elif(btn == '4'):
      bank2.inquiry()