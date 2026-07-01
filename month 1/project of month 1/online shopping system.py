print("""\n===============================
Online Shopping System
===============================\n
MENU

Select from options below:-
1)ADMIN PORTAL
2)SELLER PORTAL
3)CUSTOMER PORTAL
4)EXIT""")

main_menu=int(input("enter option "))                       # option input
while True:                                                 # loop for menu

    if main_menu==1:                                        # if option == 1 then admin menu
        print("""\n===============================
WELCOME TO ADMIN PORTAL!
===============================\n
1)Add and remove sellers
2)View all sellers
3)View all customers
4)View all products
5)View all orders
6)Generate sales reports
7)Search products
8)Display system statistics
9)Exit
""")
        admin=int(input("Enter Your Option "))###########################

    if main_menu==2:
        print("""\n===============================
WELCOME TO SELLER PORTAL!
===============================\n

1)Add new products
2)Update product details
3)Delete products
4)Manage product stock
5)View available products
6)View received orders
7)View sales summary
8)Exit

            """)
        
    if main_menu==3:
        
    if main_menu==4:
        break
