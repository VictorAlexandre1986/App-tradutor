import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract
from translate import Translator
import pyttsx3;

class App:
    def __init__(self):
        
        pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    def capturando_texto(self):
        #Capturando o texto da imagem
        texto=pytesseract.image_to_string(Image.open('teste.png'))
        return texto

    def traduzindo(self,texto):
        #Definindo a configuração do tradutor
        tradutor = Translator(from_lang="english",to_lang="pt-br" )

        #Traduzindo
        traduzido = tradutor.translate(texto)

        return traduzido
    
    def sintetizando_voz(self,traduzido):
        engine = pyttsx3.init();
        #define a velocidade da fala palavras por minuto
        engine.setProperty("rate" , 200);

        #obtendo uma lista de vozes instalado no pc
        voices = engine.getProperty('voices')

        #definindo o tipo de voz
        engine.setProperty('voice', voices[0].id);

        #Retorna se o software está falando ou nao
        print(engine.isBusy());

        #O volume vai de 0.0 ate 1.0
        engine.setProperty("volume",0.5)

        #Texto a ser falado
        engine.say(traduzido);

        engine.runAndWait() ;

if __name__=='__main__':
    app=App()
    app.texto=app.capturando_texto()
    app.texto=app.traduzindo(app.texto)
    app.sintetizando_voz(app.texto)
    