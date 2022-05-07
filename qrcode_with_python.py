# pip  install qrcode
import qrcode

code = qrcode.make('https://www.youtube.com/') # seleciona o link ou o texto que será colocado no qrcode
code.save('qrcode.jpeg') #salva e gera a imagem com o qr code no formato .png ou .jpeg