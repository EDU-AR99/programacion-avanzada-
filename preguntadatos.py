import datetime

def main():

 strDato = input("Dame un dato de tipo string: ")
 _iDato = input("Dame un dato de tipo entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato de tipo float: ")
 fDato =float(_fDato)
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 
 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(anio)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))

