palavra = input("Digite a palavra que você queira verificar se é um palindromo")
palavra = palavra.lower().replace(" ","")
listaDaPalavra = list(reversed(palavra))
palavraInvertida = "".join(listaDaPalavra)
print("A palvra ao contrario fica", palavraInvertida)
if palavraInvertida == palavra:
    print("logo a palavra", palavra,"é sim um palindromo")
else:
    print("como a palavra", palavra,"invertida não fica igual logo ela não é um palindromo")
