print("Program to check weather,the number is prime or not ?? \n")

number=int(input("Enter a number: \n"))
temp=number

if number>1:
    for i in range(2,number):#search range is form 2 to number-1
        if(number %i)==0:
            var=number//i
            print(f"The enter number :{temp},is not a prime number \n")
            print(f"As{i} times {var} is {temp}")
            break
        else:
            print(f"Enter number:{temp} is a prime number")
else:
    print(f"Enter number:{temp}, is not a prime number")