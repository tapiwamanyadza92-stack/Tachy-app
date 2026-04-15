import os

# ======================
# LOGIN DETAILS
# ======================
USERNAME = "admin"
PASSWORD = "1234"

# ======================
# FILES
# ======================
STOCK_FILE = "stock.txt"
SALES_FILE = "sales.txt"


# ======================
# STOCK FUNCTIONS
# ======================
def load_stock():
    stock = {}
    if os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, "r") as f:
            for line in f:
                item, qty = line.strip().split(",")
                stock[item] = int(qty)
    return stock


def save_stock(stock):
    with open(STOCK_FILE, "w") as f:
        for item, qty in stock.items():
            f.write(f"{item},{qty}\n")


# ======================
# SALES FUNCTIONS
# ======================
def save_sale(item, qty, total):
    with open(SALES_FILE, "a") as f:
        f.write(f"{item},{qty},{total}\n")


def load_sales():
    sales = []
    if os.path.exists(SALES_FILE):
        with open(SALES_FILE, "r") as f:
            for line in f:
                item, qty, total = line.strip().split(",")
                sales.append((item, int(qty), float(total)))
    return sales


# ======================
# APP START
# ======================
print("\n================================")
print("        🏪 TACHY APP        ")
print("================================")

username = input("Username: ")
password = input("Password: ")

if username == USERNAME and password == PASSWORD:
    print("\nLogin successful ✅")

    stock = load_stock()

    while True:
        print("\n========== MENU ==========")
        print("1. Add Stock 📦")
        print("2. View Stock 📊")
        print("3. Sell Item 💰")
        print("4. Sales Report 📈")
        print("5. Logout 🚪")

        choice = input("Choose option: ")

        # ================= ADD STOCK =================
        if choice == "1":
            item = input("Enter item name: ")
            qty = int(input("Enter quantity: "))

            if item in stock:
                stock[item] += qty
            else:
                stock[item] = qty

            save_stock(stock)
            print("Stock added ✅")

        # ================= VIEW STOCK =================
        elif choice == "2":
            print("\n===== STOCK LIST =====")
            if not stock:
                print("No stock available")
            else:
                for item, qty in stock.items():
                    print(f"{item}: {qty}")

        # ================= SELL ITEM =================
        elif choice == "3":
            item = input("Enter item to sell: ")

            if item not in stock:
                print("Item not found ❌")
                continue

            qty = int(input("Enter quantity: "))

            if qty > stock[item]:
                print("Not enough stock ❌")
            else:
                price = float(input("Enter price per item: "))
                total = qty * price

                stock[item] -= qty
                save_stock(stock)
                save_sale(item, qty, total)

                print(f"Sold successfully 💰 Total: {total}")

        # ================= REPORT =================
        elif choice == "4":
            sales = load_sales()

            if not sales:
                print("No sales yet 📭")
            else:
                total_money = 0
                total_items = 0

                print("\n===== SALES REPORT =====")

                for item, qty, total in sales:
                    print(f"{item} | Qty: {qty} | Total: {total}")
                    total_money += total
                    total_items += qty

                print("\n===== SUMMARY =====")
                print(f"Total Items Sold: {total_items}")
                print(f"Total Money Made: {total_money}")

        # ================= LOGOUT =================
        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid option ❌")

else:
    print("Wrong username or password ❌")
