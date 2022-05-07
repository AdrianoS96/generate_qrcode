#https://acervolima.com/gerar-codigo-qr-usando-qrcode-em-python/#:~:text=Python%20tem%20uma%20biblioteca%20%E2%80%9C%20qrcode,pode%20ser%20instalado%20usando%20pip.&text=Abordagem%3A,M%C3%B3dulo%20de%20importa%C3%A7%C3%A3o
# pip  install qrcode
import qrcode

code = qrcode.make('https://www.youtube.com/') # seleciona o link ou o texto que será colocado no qrcode
code.save('qrcode.jpeg') #salva e gera a imagem com o qr code no formato .png ou .jpeg