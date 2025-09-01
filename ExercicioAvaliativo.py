# Primeiro, instale a biblioteca caso ainda não tenha:
# pip install qrcode[pil]

import qrcode

# Texto ou URL que você quer transformar em QR code
dados = input("Digite o texto ou URL para gerar o QR code: ")

# Criação do QR code
qr = qrcode.QRCode(
    version=1,  # tamanho do QR code (1 é o menor)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # nível de correção de erro
    box_size=10,  # tamanho de cada quadradinho
    border=4,  # borda do QR code
)

qr.add_data(dados)
qr.make(fit=True)

# Gerando a imagem
imagem = qr.make_image(fill_color="black", back_color="white")

# Salvando a imagem
arquivo_saida = "meu_qrcode.png"
imagem.save(arquivo_saida)

print(f"QR code gerado e salvo como {arquivo_saida}")
