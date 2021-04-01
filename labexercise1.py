#diana anak man
#20DDT19F1091

#Question 1a

range(11)
for i in range(11):
    print("The square of ", i, "is : ",i*i)

print("")
print("Process finished with exit code 0")


#Question 1b

limit=11
i=0
sum=0
while i<limit:
    if i%2==0:
        sum=sum+i
    i=i+1
print("The total of even numbers from 0 to 10 is ",sum)
print("")
print("Process finished with exit code 0")

#Question 2

username = input("Please enter your username : ")
password = input("Please enter your password : ")
print(len(password))

if not username.isalpha():
    print("Please use only alphabet characters")

else:
    print("")

if len(password)<5:
    print("Your password need to contain atleast 5 characters")
if not password.isdigit():
    print("Your password must in numeric")
else:
    print("")


#Question 3

car_price=103300
downpayment= int(input("Please enter your downpayment : "))
years=int(input("Please enter your loan period in years : "))

loan_amount=car_price - downpayment
total_interest = (2.7/100)*loan_amount*years
monthly_installment=(loan_amount + total_interest)/(years*12)



print("You need to pay",monthly_installment,"as your monthly installment")

