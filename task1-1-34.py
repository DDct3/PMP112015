#сума чисел до n, піднесених до квадрату
n=abs(int(input("Number=")))
S=0 #початкове значення суми
for k in range(n+1):
    S=S+k**2
print("Сума=",S)
pass
