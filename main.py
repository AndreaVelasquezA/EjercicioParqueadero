def definitiva (a, b, c):
    n1=a*0.3
    n2=b*0.3
    n3=c*0.4
    nf=n1+n2+n3
    
    if nf<2:
        print("no peude hablitar; su nota es de: ", nf)
    elif 3>nf>=2:
        print("usted reprobó con una nota de: ", nf)
    elif 4.5>nf>=3:
        print("aprobó con una nota de: ", nf)
    else:
        print("felicitaciones, obvtuvo una nota excelente: ",nf)
    return nf
    
for i in range(5):
    n1=float(input("digite la nota de 30 del estudiante"))
    n2=float(input("digite la segunda nota de 30 del estudiante"))
    n3=float(input("digite la nota de 40 del estudiante"))
    nf=definitiva(n1,n2,n3)
    