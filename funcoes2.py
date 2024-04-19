def fatorial (n):
    fat= 1
    while (n>0:
           fat=fat*n
           n-=1
    return fat

def fatorial_recursivo(n):
    if (n<=1):
        return 1
    else:
        return n*fatorial_recursivo(n-1)

print(f"O fatorial com função {fatorial(100)}")
print(f"O fatorial com função {fatorial_recursivo(100)}")
