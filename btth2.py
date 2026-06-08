atm_vault_balance = 50000000
user_account_balance = 10000000
def get_valid_amount(message):
    while True:
        val_input = input(message)
        temp = val_input.replace(".", "", 1)
        if temp.isdigit():
            val = float(val_input)
            if val > 0:
                return val
        print("Số tiền không hợp lệ.")
def display_balances():
    print("SỐ DƯ TÀI KHOẢN")
    print(f"Tài khoản của bạn: {user_account_balance:,.0f} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,.0f} VND")
def deposit_money(amount):
    global user_account_balance, atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount
    return True
def check_withdrawal_rules(amount):
    if amount % 50000 != 0:
        return "INVALID_MULTIPLE", 0
        
    fee = 1100
    total_deduction = amount + fee
    
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS", total_deduction
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH", total_deduction
    return "OK", total_deduction
def execute_withdrawal(total_deduction, amount_to_dispense):
    global user_account_balance, atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,.0f} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,.0f} VND.")
def display_menu():
    print("SMART ATM")
    print("1. Xem số dư")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("4. Kết thúc giao dịch")

def main():
    while True:
        display_menu()
        choice = input("Vui lòng chọn giao dịch (1-4): ")
        if choice == "1":
            display_balances()
        elif choice == "2":
            print("NẠP TIỀN")
            amount = get_valid_amount("Nhập số tiền muốn nạp: ")
            if deposit_money(amount):
                print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,.0f} VND.")
        elif choice == "3":
            print("RÚT TIỀN")
            amount = get_valid_amount("Nhập số tiền cần rút: ")
            status, total_deduction = check_withdrawal_rules(amount)
            if status == "INVALID_MULTIPLE":
                print("Số tiền rút phải là bội số của 50,000.")
            elif status == "INSUFFICIENT_FUNDS":
                print("Giao dịch thất bại: Số dư tài khoản không đủ để thực hiện (bao gồm phí).")
            elif status == "ATM_OUT_OF_CASH":
                print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
            elif status == "OK":
                execute_withdrawal(total_deduction, amount)
                
        elif choice == "4":
            print("Thoát chương trình!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")
main()