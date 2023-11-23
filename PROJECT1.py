#Ülesanne 7
S=str(input("Пол")).lower
if S=="мужской":
    H=float(input("Какой у вас рост?"))
    if H<169:
        print("Маленький рост")
    if 170<H<185:
        print("Средний рост")
    if H>186:
        print("Высокий рост")
if S=="женский":
    G=float(input("Какой у вас рост?"))
    if G<160:
        print("Маленький рост")
    if 160<G<175:
        print("Средний рост")
    if G>175:
        print("Высокий рост")
else: print("ERROR")

#Ülesanne 6
H=float(input("Какой у вас рост?"))
if H<169:
    print("Маленький рост")
if 170<H<185:
    print("Средний рост")
if H>186:
    print("Высокий рост")


#Ülesanne 5
T=float(input("Какая температура в комнате? "))
if T>18:
    print("Предпочтительная комнатная температура")
else: print("Холодно")





#Ülesanne 4
E=float(input("Введите цену:"))
if E>700:
    print("цена со скидкой"+E-E/100*30)
else: print(E+"скидка не предусмотрена")




#Ülesanne 3
A=float(input("Длина первой стены"))
B=float(input("Длина второй стены"))
print(A*B+"метров квадратных")
W=str(input("Хотите ли вы сделать ремонт?" )).lower
if W=="да":
    Q=float(input("Цена одного квадратного метра: "))
    print(A*B*Q+"-cтоимость замены пола")

#Ülesanne 2
a=str(input("Mis sinu nimi on? "))
b=str(input("Mis tema nimi on? "))
print(a+"JA"+b+"on täna pinginaabrid")




#Ülesanne 1
E=input(str("Eesnimi: "))
if E=="Juku":
    V=int(input("Vanus: "))
    if V<6:
        print("tasuta")
    if 6<V<14:
        print("lastepilet")
    if 15<V<65:
        print("täispilet")
    if V>65:
        print("sooduspilet")
    if V<0 and V>100:
        print("Viga andmetega")
else: print("в кино только с Juku")