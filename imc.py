import sys

weight = float(sys.argv[1])
height = float(sys.argv[2])

imc = weight/(height/100)**2

print(f'Su IMC es {imc:.2f}')

if imc < 18.5:
    print(f'La clasificación OMS es Bajo Peso')
elif imc < 25:
    print(f'La clasificación OMS es Adecuado')
elif imc < 30:
    print(f'La clasificación OMS es Sobrepeso')
elif imc < 35:
    print(f'La clasificación OMS es Obesidad Grado I')
elif imc < 40:
    print(f'La clasificación OMS es Obesidad Grado II')
else:
    print(f'La clasificación OMS es Obesidad Grado III')