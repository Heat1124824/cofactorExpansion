def factorial(n):
    if n == 0: #終止條件: 當n被減到0時，則結束計算
        return 1
    else:
        return n * factorial(n - 1) #呼叫自己，每呼叫自己一次，n就會減1

number = 5
print("Factorial of", number, "is", factorial(number)) #輸出: Factorial of 5 is 120
