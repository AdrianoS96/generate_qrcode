# https://pypi.org/project/qrcode/
# pip install qrcode[pil]
import qrcode 
data = 'https://www.youtube.com/'
qr = qrcode.QRCode(version = 1, box_size = 10, border = 1) 
qr.make(data) 
  
qr.make(fit = True) 
img = qr.make_image(fill_color = 'red', back_color = 'white') 
  
img.save('qrColor.png')


# Versão: Este parâmetro é um número inteiro de 1 a 40 que controla o tamanho do QR Code (o menor, versão 1, é uma matriz 21 × 21).
# error_correction:   Este parâmetro controla a correção de erros usada para o QR Code. Existem as seguintes quatro constantes disponíveis para isso:
# qrcode.constants.ERROR_CORRECT_L : Cerca de 7% ou menos erros podem ser corrigidos.
# qrcode.constants.ERROR_CORRECT_M (padrão) : Cerca de 15% ou menos erros podem ser corrigidos.
# qrcode.constants.ERROR_CORRECT_Q : Cerca de 25% ou menos erros podem ser corrigidos.
# qrcode.constants.ERROR_CORRECT_H : Cerca de 30% ou menos erros podem ser corrigidos.
# box_size: Este parâmetro controla quantos pixels cada “caixa” do código QR tem.
# border: O parâmetro border controla quantas caixas de espessura a borda deve ter (o padrão é 4, que é o mínimo na especificação).
# add_data(): este método é usado para adicionar dados ao objeto QRCode. Leva os dados a serem codificados como um parâmetro.
# make(): Este método com (fit = True) garante que toda a dimensão do QR Code seja utilizada, mesmo que nossos dados de entrada possam caber em menos caixas.
# make_image(): Este método é usado para converter o objeto QRCode em um arquivo de imagem. Leva os fill_color e back_color parâmetros opcionais para definir a cor de # primeiro plano e plano de fundo.
