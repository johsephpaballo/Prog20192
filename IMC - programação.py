# IMC - Disciplina de programação
'''
alturaFloat = 1.74
pesoFloat = 64.0

imc = pesoFloat/ (alturaFloat**2)

print (imc)

print ("Muito abaixo do peso?", imc < 17.0)
print ("Abaixo do peso normal?", imc >= 17.0 and imc <= 18.5)
print ("Peso dentro do Normal?", imc > 18.5 and imc <= 25.0)
print ("Acima do peso normal?", imc > 25.0 and imc <= 30.0)
print ("Muito acima do peso?", imc > 30.0)

Pause
'''
#IMC CALCULADORA#
print ("programa para calcular IMC")

alturaFloat = input("Digite sua altura em metros: ")
pesoFloat = input ("Digite seu peso em Kg: ")

imc = float(pesoFloat)/(float(alturaFloat)**2)

print(imc)

if imc <17.0:
    print ("Muito abaixo do peso!")
elif  imc >= 17.0 and imc <= 18.5:
    print ("Abaixo do peso normal!")
elif imc > 18.5 and imc <= 25.0:
    print ("Peso dentro do Normal!")
elif imc > 25.0 and imc <= 30.0:
    print ("Acima do peso normal!")
else:
    print ("Muito acima do peso!")