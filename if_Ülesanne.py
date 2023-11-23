print("Tere! Olen sinu uus sõber - Python!")
nimi=str(input("Введите свое имя: "))
print(nimi+", oi kui ilus nimi!")
v=print(input(nimi+" Kas leian Sinu keha indeksi? 0-ei, 1-jah"))
if v==1:
    pikkus=int(input("kui pik sa oled?"))
    mass=float(input("kui palju Te kaalute?"))
    indeks=mass/(0.01*pikkus**2)
    print("Sinu keha indeks on:"+indeks)
    if indeks< 16:
        print("Tervisele ohtlik alakaal")
    if 16<indeks<19:
        print("Alakaal")
    if 19<indeks<25:
        print("Normaalkaal")
    if 25<indeks<30:
        print("Ülekaal")
    if 30<indeks<35:
        print("Rasvumine")
    if 35<indeks<40:
        print("Tugev rasvumine")
    if 40<indeks:
        print("Tervisele ohtlik rasvumine")
else:print("Kahju! See on väga kasulik info!")
print("")