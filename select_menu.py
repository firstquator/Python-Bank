def select_menu():
    print("======Bank======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 계좌이체")
    print("6. 프로그램 중료")
    print("================")
    btn = int(input("입력 : "))

    return btn;

b = select_menu()
print(b)