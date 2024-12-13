#metodo sem funcoes
# palavra = input("Digite a palavra que você queira verificar se é um palindromo")
# palavra = palavra.lower().replace(" ","")
# listaDaPalavra = list(reversed(palavra))
# palavraInvertida = "".join(listaDaPalavra)
# print("A palavra ao contrario fica", palavraInvertida)
# if palavraInvertida == palavra:
#     print(f"logo a palavra {palavra} é sim um palindromo")
# else:
#     print(f"como a palavra {palavra} invertida não fica igual logo ela não é um palindromo")


#usando função para verificar se é um palindromo
import re
#criando um funcao para verificar se a entrada é valida
def palavraValida(palavra):
     # Aceita letras e espaços, desde que haja pelo menos uma letra
    return re.match(r"^\s*[a-zA-Z]+(?:\s+[a-zA-Z]+)*\s*$", palavra)
#essa funcao verifica se é um palindromo
def verificarPalindromo(palavra):
    if not palavraValida(palavra):
        return None
    palavra = str(palavra).lower().replace(" ","")
    return palavra == palavra[::-1]
    
#criando outra funcao só para a parte de exibir a palavra ao contrario, ja que retornar um boleano na verificação é melhor que retornar print
def exibirPalavraInvertida(palavra):
    if palavraValida(palavra):
        palavraInvertida = "".join(reversed((palavra)))
        print(f"A palavra ao contrario fica {palavraInvertida}")
    else:
        print("Entrada inválida. Por favor, digite apenas letras e espaços.")

##chamando e usando as funções
palavra = input("Digite a palavra que você queira verificar se é um palindromo: ")

exibirPalavraInvertida(palavra)
resultado = verificarPalindromo(palavra)
if resultado is True:
    print(f"logo a palavra {palavra} é sim um palindromo")
elif resultado is False:
    print(f"como a palavra {palavra} invertida não fica igual logo ela não é um palindromo")