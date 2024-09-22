def contar_a(string):
    contador = string.lower().count('a')
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")


texto = input("Informe uma string: ")
contar_a(texto)
