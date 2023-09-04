peso = float(input("Hola; introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Peso normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print("Tu índice de masa corporal es de:", imc)
print("Categoría de categoría de masa corporal es:", categoria)



