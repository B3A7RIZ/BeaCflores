a=float(input("Dame calificacion 1: "))
b=float(input("Dame calificacion 2: "))
c=float(input("Dame calificacion 3: "))
d=float(input("Dame calificacion 4: "))
e=float(input("Dame calificacion 5: "))
print("Promedio general: ",(a+b+c+d+e)/5)
p=(a+b+c+d+e)/5
if(p<7):
   print("Alumno reprobado")
if(p>=7) and (p<=8):
   print("Alumno suficiente")
if(p>8) and (p<=9):
   print("Alumno notable")
if(p>9) and (p<=10): 
   print("Alumno exelente")
if(p>10):
   print("revaso el limite")
