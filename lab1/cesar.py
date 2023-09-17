import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            # Verificar si el caracter es mayúscula o minúscula
            if caracter.isupper():
                codigo = ord('A')
            else:
                codigo = ord('a')
            
            # Aplicar el cifrado de César al caracter
            texto_cifrado += chr((ord(caracter) - codigo + corrimiento) % 26 + codigo)
        else:
            # Mantener caracteres que no son letras sin cambios
            texto_cifrado += caracter
    
    return texto_cifrado

if len(sys.argv) != 3:
    print("Uso: python cifrado_cesar.py <texto_a_cifrar> <corrimiento>")
    sys.exit(1)

texto_a_cifrar = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto_a_cifrar, corrimiento)
print(texto_cifrado)
