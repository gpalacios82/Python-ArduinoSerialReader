def recorta(cad1,cad2,cadorigen):
    p1 = cadorigen.find(cad1)
    p2 = cadorigen.find(cad2)
    cadena = cadorigen[p1 + cad1.__len__():p2]
    return cadena