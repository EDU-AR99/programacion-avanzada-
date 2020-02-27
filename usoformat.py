def main():
  intBase = 14
  intAltura = 10
  AreaTriangulo=(intBase*intAltura)/2
  txt = "Area: {2:0.2f} ( {0} por {1} entre dos )"
  print(txt.format(intBase, intAltura, AreaTriangulo))

  #se hace una operacion multiplicacion dividida entre dos la cual se hace en la variable llamada AreaTriangulo, la base y altura se decidio que fuera de tipo entero.