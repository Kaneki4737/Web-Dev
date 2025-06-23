class calc:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mult(self,a,b):
        return a*b
    
    def div(self,a,b):
        return a/b
    
    def square(self,a):
        return a**2
    
    def sqrt(self,a):
        return a**0.5
    
c = calc()

v = int(input("""
Choose operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Square
6. Square root
: """))

if v<1 or v>6:
    print("Please choose the correct option")

else:
    if v==1:
        a = int(input("Choose the first number: "))
        b = int(input("Choose the second number: "))
        print(c.add(a,b))
    
    if v==2:
        a = int(input("Choose the first number: "))
        b = int(input("Choose the second number: "))
        print(c.sub(a,b))
    if v==3:
        a = int(input("Choose the first number: "))
        b = int(input("Choose the second number: "))
        print(c.mult(a,b))
