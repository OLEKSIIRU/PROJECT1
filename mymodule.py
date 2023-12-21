def summa3(arv1: float, arv2: float,arv3: float)->float:
    """Tagastab kolme arvu summa 
     :param float arv1: Esimene arv
     :param float arv2: Teine arv
     :param float arv3: Kolmas arv
     :rtype: float 
    """
    summa=arv1+arv2+arv3
    return summa


#1
def arithmetic(a1: float, a2:float, op:str)->any:
    """Lihtne kalkulaator. 
    + - liitmine
    - -lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv
    :param float b: arv
    :param str<. atitmeetilne tehing
    :rtype: var Nääramata tüüp(float or str)
    """
if op in ["+","-","*","/"]:
    if b==0 and t=="/":
        vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
else:
    vastus ="Tundnstu tehe "

return vastus

#2

def is_year_leap(year:int)->bool:  
    """Liigaasta leidmine 
 Tagastab True, kui liigaasta ja False, kui on tavaline aasta. 
 :param int aasta: aasta number
 :rtype: bool tagastab loogilises formaadis tulemus
 """
    if year % 4 == 0:
        v=True
    else:
        v=False
return v