import emoji
def lista_emoji():
    emoji_list = {
        ":red_heart:" : "❤️",
        ":thumbs_up:" : "👍 ",
        ":thinking_face:" : "🤔 ",
        ":partying_face:" : "🥳 ",
    }
print("Lista de emojis disponíveis:")
print(lista_emoji)
frase = str(input("Digite uma frase e ela será emojizada:"))
def codificar_emoji(frase_codificada):
    frase_emojizada = emoji.emojize(frase)
    return frase_emojizada
frase_emojizada = codificar_emoji(frase)
print(f"Frase emojizada: {frase_emojizada}")
