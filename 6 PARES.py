sentence=input('ESCREVA ALGO')
spp=''
i=1

for inicio in sentence:
    if i%2:
        spp+=inicio
    i+=1

print(f'{spp}')
