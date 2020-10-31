import base64

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("CRIPTOGRAFIA BASE64 EM PYTHON")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

comando = input("Comandos disponíveis: \n Encriptografar (ENCODE) \n Descriptografar (DECODE). \n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n\n Comando selecionado: ")
comando = comando.lower()

if comando == "encode":
    codigo = input("Insira o código a ser criptografado: ").encode('utf-8')
    codigo_encode = base64.b64encode(codigo)
    print("A mensagem criptografada é:", codigo_encode)
elif comando == "decode":
    codigo = input("Insira o código a ser descriptografado: ")
    codigo_decode = base64.b64decode(codigo)
    print("A mensagem descriptografada é:", codigo_decode)
else:
    print("-> Comando não válido! <-")