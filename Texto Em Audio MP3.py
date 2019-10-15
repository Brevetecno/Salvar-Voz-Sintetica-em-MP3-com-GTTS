# Desenvolvedor Brevetecno
# Python 3
# 2019

from gtts import gTTS

while True:
    loop = True
    idioma = 'pt-br'

    print('='*50)
    print('Digite um texto que será transformado em voz.')

    print('='*50)
    texto = str(input('Texto: ')) # Este texto será convertido em voz, necessita de Internet para a conversão.
    
 
    
    while loop:
        print('Salvar no idioma Português ou Inglês?')
        print('(1) - Português')
        print('(2) - Inglês')
        resposta = int(input('Resposta: '))
        
        if (resposta != 1) and (resposta != 2):
            loop = True
        else:
            if resposta == 1:
                idioma = 'pt-br'
            else:
                idioma = 'en-us'
                
            loop = False
    
    nome = str(input('Nome do arquivo convertido: ')) # Nome do arquivo que será salvo em MP3
    print('='*50)
    
    print('Tentando converter texto em voz. Aguarde...')
    
    # Irá falar Olá Mundo no idioma Português do Brasil
    audio = gTTS(text=texto, lang=idioma, slow = False)

    # Irá ser salvo no local do arquivo Python
    audio.save('{}.mp3'.format(nome))
