list = []
for i in range(10):
    word=input(f"ESCREVE QUALQUER COISA) {i+1} de 10)\n")
    list.append( word + '\n')
text = open("list.text", "w+")
text.writelines(list)
