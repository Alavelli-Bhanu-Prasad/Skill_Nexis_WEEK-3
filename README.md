# Skill_Nexis_WEEK-3
1. Bank Account Class

Models a simple bank account that supports depositing money, withdrawing money, and checking the balance — with validation to prevent invalid transactions.

Features:

1)Create an account with an initial balance

2)Deposit — only accepts positive amounts

3)Withdraw — only allows withdrawal if the amount is positive and does not exceed the current balance

4)Display balance — returns the current balance

CLASS OVERVIEEW :

Method	                                  Description

__init__(self, balance=0)   	Initializes the account with an optional starting balance (defaults to 0)

deposit(amt)	                Adds amt to the balance if amt > 0

withdraw(amt)	                Subtracts amt from the balance if 0 < amt <= balance

display_balance()            	Returns the current balance

OUTPUT :-

<img width="1285" height="79" alt="image" src="https://github.com/user-attachments/assets/e07a2c32-85fb-4490-aa74-9500e1ce5999" />

2. Library Management System (OOP)

A menu-driven library system that manages a book collection using two classes — Book and Library — supporting adding, removing, issuing, and returning books.

Features:

1)Add a new book to the library

2)Remove a book by title

3)Issue a book (blocks issuing if it's already issued)

4)Return a book (blocks returning if it was never issued)

5)Display all books along with their current status (Available / Issued)

6)Simple menu-driven interface that loops until the user exits

CLASS OVERVIEEW :

Method                              Description

add_book(title)              Creates a new Book and adds it to the library

remove_book(title)           Removes a book by title, if found

issue_book(title)            Marks a book as issued, if it exists and isn't already issued

return_book(title)           Marks a book as returned, if it exists and was issued

display_books()              Prints every book with its current status

OUTPUT :-

<img width="1292" height="780" alt="Screenshot 2026-07-28 231103" src="https://github.com/user-attachments/assets/da450ea8-b927-4bfa-beac-795192ecdb58" />
<img width="1310" height="753" alt="Screenshot 2026-07-28 231124" src="https://github.com/user-attachments/assets/510ef871-1407-44c7-8f1b-c7eb73ed9c07" />
<img width="1327" height="906" alt="Screenshot 2026-07-28 231140" src="https://github.com/user-attachments/assets/a76a204a-13f0-42df-9dbc-95f82eb0e67c" />

3. Calculator Class with Exception Handling

A calculator that performs the four basic arithmetic operations, using try/except blocks to handle invalid input (e.g. non-numeric values) and division by zero without crashing.

Features:

1)Addition, subtraction, multiplication, and division

2)Division by zero is caught and returns a clear error message instead of crashing

3)Invalid input (e.g. adding a string to a number) is caught with TypeError handling

CLASS OVERVIEEW :

Method	                                 Description

add(a, b)                    	Returns a + b; returns an error message on TypeError

subtract(a, b)	              Returns a - b; returns an error message on TypeError

multiply(a, b)	              Returns a * b; returns an error message on TypeError

divide(a, b)                	Returns a / b; handles both ZeroDivisionError and TypeError

OUTPUT :-

<img width="1491" height="192" alt="Screenshot 2026-07-31 212304" src="https://github.com/user-attachments/assets/6716f108-6aeb-4bc6-82e8-4a5a4af505db" />

Mini Project (W3): "Billing System (OOP-based)"

A billing system that calculates the total cost of purchased products, applies tax, and displays a final itemized bill.

Features:

1)Product class — stores individual item details (name, price, quantity) and calculates the total cost for that item

2)Bill class — manages a collection of products and handles:

3)Adding products to the bill

4)Calculating the subtotal

5)Calculating tax (10%)

6)Displaying the final bill in a clean, tabular format

Class Overview :

Product

Attribute / Method	                         Description

name	                                Name of the product

price	                                Price per unit

quantity	                            Number of units purchased

get_total()                         	Returns price * quantity

Bill

Method	                                     Description

add_product(product)                 	Adds a Product object to the bill

calculate_total()	                    Returns the subtotal of all products

calculate_tax(tax_rate=0.1)          	Returns tax amount (default 10%)

display_bill()	                      Prints the itemized bill along with subtotal, tax, and grand total

OUTPUT :-

<img width="1419" height="332" alt="Screenshot 2026-07-31 212720" src="https://github.com/user-attachments/assets/b1cb347c-c007-4af7-aa32-2823dcbb7dfd" />
