#Ülesanne 14




#Ülesanne 13

sex=input("Укажите свой пол").lower
if sex=="мужчина":
    yo=int(input("Укажите свой возраст"))
    if 16<yo<18:
        print("Ждем вас в команде")
    else:print("Извините, вы нам не подходите")
else: print("Извините, вы нам не подходите")




#Ülesanne 12

price=float(input("Введите цену продукта"))
if 10<price<20:
    print("Final price"+price-price/100*10)
if price>20:
    print("Final price"+price-price/100*20)




#Ülesanne 11
from datetime import date

sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: ")))
praegu=date.today().year #2023

if (praegu-sp.year)%10==0:#sp>date(2000,1,1):
    print("Juubel")
else:
    print("------")

#Ülesanne 10
a=float(input("Введите первое число"))
b=float(input("Введите второе число"))
t=input("Tegevust:")
      if t in ['+','-','/','*']:
                if t=='+':
                    v=a+b
                elif t=='-':
                    v=a-b
                elif t=='*':
                    v=a*b
                elif t=='/':
                    if b==0:
                        v="DIV/0"
                    else:
                        v=a/b
                print("{0}{1}{2}={3}").format(a,t,b,v)
      else: print("ERROR")

       


#Ülesanne 9

LA=float(input("Введите первую сторону квадрата"))
Б=float(input("Введите вторую сторону квадрата"))
В=float(input("Введите третюю сторону квадрата"))
Г=float(input("Введите четвертую сторону квадрата"))
if LA==Б==В==Г:
    print("Квадрат")
else: print("Все что угодно кроме квадрата")

#Ülesanne 8
K=str(input("Вы хотите купить молоко?"))
if K=="ja":
    J=80
else: J=0
Ö=str(input("Вы хотите купить хлеб?"))
if Ö=="ja":
    L=J+30
else: L=J
Ü=str(input("Вы хотите купить булку?"))
if Ü=="ja":
    Kokku=L+35
else: Kokku=L







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
d=str(input("Mis sinu nimi on? "))
u=str(input("Mis tema nimi on? "))
print(d+"JA"+u+"on täna pinginaabrid")




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