# coding = UFT-8
# primeiro código
print("Toni")
print("------------------------------------")
a = input("Escreva seu nome: ")
print("Seu nome é: %s" % a)
print("------------------------------------")
a = input("Escreva seu nome: ")
b = input("Escreva sua idade: ")
print("")
print("O seu nome é: ", a, " e a sua idade é: ", b)
print("-----------------------------------")
c = input("Digite um número: ")
print("O número digitado foi: ", c)
print("-----------------------------------")
print("Digite 3 números: ")
d = float(input("Número 1: "))
e = float(input("Número 2: "))
f = float(input("número 3: "))
soma = d + e + f
print("Soma: ", soma)
print("-----------------------------------")
media = (d + e + f) / 3
print("Média: ", media)
print("-----------------------------------")
g = int(input("Digite umammedida em metros: "))
cent = g * 100
print("Medida em centímetros: ", cent)
print("-----------------------------------")
h = float(input("digite um número: "))
cubo = h ** 3
quad = h ** 2
print(h, " ao quadrado é ", quad, h, " ao cubo é ", cubo)
print("-----------------------------------")
j = float(input("digite um número: "))
k = float(input("digite outro número: "))
div = j / k
int = j // k
print("divisão: ", div, "divisão inteira: ", int)
print("-----------------------------------")
l = float(input("digite largura: "))
m = float(input("digite altura: "))
area = l * m
print("Área: ", area)
print("-----------------------------------")
q = float(input("digite dias: "))
n = float(input("digite hora: "))
o = float(input("digite minutos: "))
p = float(input("digite segundos: "))
seg = (q * 86400) + (n * 3600) + (o * 60) + p
print("Total em segundos: ", seg)
print("-----------------------------------")
r = float(input("Informe um valor: ", ))
perc = r * 0.10
desc = r - perc
print("Valor: ", r, "Com desconto: ", desc)
print("-----------------------------------")
