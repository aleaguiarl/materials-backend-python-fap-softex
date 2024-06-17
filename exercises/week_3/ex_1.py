# Faça um programa que peça as 4 notas bimestais e mostre a média.

print("+------------------------- CALCULADORA DE MÉDIA -------------------------+")
nota1 = float(input("Insira quatro notas bimestrais: \n"))
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

media = (nota1 + nota2 + nota3 + nota4) / 4 

print(f"\n+--- NOTAS ---+ \n{nota1} | {nota2} | {nota3} | {nota4}")
print(f"\nA média das notas bimestrais é igual a {media:.2f}")