seznam = [12, 5, 8, 21, 3, 16, 9, 14]
#1. naloga
vsota = 0
for i in range(8):
    vsota = vsota + seznam[i]
print("vsota: ", vsota)
#2. naloga
vsota = 0
for i in range (8):
    vsota = vsota + seznam[i]
print("povp. vrednost: ", vsota/8)
#3. naloga
najvecje = 0
for i in range (8):
    if seznam[i]>najvecje:
        najvecje = seznam[i]
print("najvecja vrednost: ", najvecje)
#4. naloga
najmanjse = 100
for i in range(8):
    if seznam[i]<najmanjse:
        najmanjse = seznam[i]
print("najmenjse stevilo: ", najmanjse)
#5. naloga
vs = 0
for i in range (8):
    if seznam[i]%2 ==0:
        vs +=1
print("stevilo sodih: ", vs)
#6. naloga
v = 0
for i in range (8):
    if seznam[i]%2 != 0:
        v +=1
print("stevilo lihih: ", vs)
#7. naloga
print("stevila vecja od 10:")
for i in range(8):
    if seznam[i]>10:
        print(seznam[i], " ", end = "")
#8. naloga
seznam.sort()
print(seznam)
#9. naloga
a = input("vnesi stevilko: ")
seznam.append(a)
print(seznam)
#10. naloga
b = input("vnesi stevilo za odstranitev: ")
najdeno = false
for i in range (9):
    if seznam[i] == b:
        seznam.remove(b)
        najdeno = true
        break
if najdeno==false:
    print("ni bilo števila v seznamu.")
else:
    print("stevilo je bilo izbrisano iz seznama.")


