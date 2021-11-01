from googletrans import Translator


def translate_text(message):
    translator = Translator()
    result = translator.translate(message, src='en', dest='pt')
    return result.text


if __name__ == '__main__':
    print(translate_text("orange"))
