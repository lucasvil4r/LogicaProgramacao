x = int(input())
y = int(input())

cont_bom_dia = 0
cont_boa_tarde =  0
cont_boa_noite = 0

i = 0

while i < x:
    print("bom dia")
    cont_bom_dia +=1
    j = 0
    while j < y:
        print("boa tarde")
        cont_boa_tarde +=1
        j +=1
    else:
        i +=1
else:
    print("boa noite")
    cont_boa_noite +=1

print(f'bom dia = {cont_bom_dia}')
print(f"boa tarde = {cont_boa_tarde}")
print(f"boa noite = {cont_boa_noite}")
