vetPrice = []
vetG = []
vetRT = []
vetGp = [0,0,0,0,0]
otimo = 0
classeCortada = 0
i =0
print("Insira os preços das arvores:")
while i < 5:
    print("P",i+2,":")
    vetPrice.append(float(input()))
    i = i+1
    
print("Insira os valores da matriz G:")
i=0
while i < 5:
    print("G",i+1,":")
    vetG.append(float(input()))
    i = i+1

i=0
while i < 5:
    if i ==0:
        vetGp[i] = 0 + (1/vetG[i])
    else:
        vetGp[i] =vetGp[i-1] +(1/vetG[i])
    i = i+1
  
i=0  
quantidade = float(input("Qual é o número total de árvores na floresta? "))
while i < 5:
    vetRT.append(vetPrice[i]/(vetGp[i]))
    if vetRT[i] > otimo:
        otimo = vetRT[i]
        classeCortada = i+2
    print("RT",i+2,":",vetRT[i])
    i=i+1
    


resp8 = quantidade / vetGp[classeCortada - 3]

print("5- A classe a ser removida é:",otimo)
print("5- O retorno ótimo e sustentável é:",otimo * quantidade)
print("8- A quantidade de árvores removidas da floresta em cada colheita, em uma política de retorno sustentável ótimo é:",resp8)
    
