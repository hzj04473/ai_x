from customer import load_customers
# from functions import *
from functions import fn1_insert_customer_info, fn2_print_customers
from functions import fn3_delete_customer, fn4_search_customer
from functions import fn5_save_customer_csv, fn9_save_customer_txt

def main():
    global customer_list
    customer_list = load_customers()  # ch09_customers.txt의 내용을 load

    while True:
        try:
            print("1:입력 | 2:전체출력 | 3:삭제 | 4:이름찾기 | 5:내보내기(CSV) | 9:종료 ", end=" ")
            fn = input('메뉴선택 : ')
        except Exception as e:
            print(e)
        else:
            if fn == '1':
                #입력받은 내용으로 customer 객체를 반환
                customer = fn1_insert_customer_info()  
                customer_list.append(customer)
                pass
            elif fn == '2':
                fn2_print_customers(customer_list)
            elif fn == '3':
                fn3_delete_customer(customer_list)
            elif fn == '4':
                fn4_search_customer(customer_list)
            elif fn == '5':
                fn5_save_customer_csv(customer_list)
            elif fn == '9':
                fn9_save_customer_txt(customer_list)
                break
            else:
                print("잘못 선택하였습니다. 다시 선택해 주세요.")
        finally:
            print("제작자 김진경 메롱 ~~~~",end="\n")


if __name__ == "__main__":
    main()