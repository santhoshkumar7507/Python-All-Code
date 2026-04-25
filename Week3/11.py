num = int(input("Enter the number: ")) #121
n = num #121
reverse = 0

while num>0: #121  #12  1
    digits = num%10 #1   #2  1 last digit
    reverse=reverse*10+digits  #1  #12  121
    num=num//10  #12  1 0
print(reverse)

if n == reverse:
    print("palindrome")
else:
    print("Not Palindrome")