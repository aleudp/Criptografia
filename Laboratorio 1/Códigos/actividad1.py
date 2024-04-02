import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ''
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                inicio = ord('A')
            else:
                inicio = ord('a')
            codificado = (ord(caracter) - inicio + corrimiento) % 26 + inicio
            texto_cifrado += chr(codificado)
        else:
            texto_cifrado += caracter
    return texto_cifrado

if len(sys.argv) != 3:
    print("Uso: python3 cifrado.py <texto> <corrimiento>")
    sys.exit(1)

texto = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto, corrimiento)
print(texto_cifrado)
