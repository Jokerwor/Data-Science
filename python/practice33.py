n = int(input("Enter the number: "))

def patt_ern(n):
    if n == 0: 
        return
    print("*" * n)  
    patt_ern(n - 1)  

patt_ern(n) 