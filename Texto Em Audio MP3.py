# Desenvolvedor Brevetecno
# Python 3
# 2019

from gtts import gTTS


while True:
    print('='*50)
    print('Um audio MP3 será salvo com uma síntese de voz falando o que você escreveu.')

    print('='*50)
    texto = str(input('Dizer: ')) # Este texto será convertido em voz, necessita de Internet para a conversão.
    nome = str(input('Nome do arquivo: ')) # Nome do arquivo que será salvo em MP3
    print('='*50)
    
    # Irá falar Olá Mundo no idioma Português do Brasil
    audio = gTTS(text='Olá, Mundo', lang='pt-BR', slow = False)

    # Irá ser salvo no local do arquivo Python
    audio.save('{}.mp3'.format(nome))
