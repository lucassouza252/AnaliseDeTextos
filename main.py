text = input("Digite seu nome e uma frase: ")

chingamentos = ['porra', 'porr', 'merds', 'merda', 'merd', 'puta que pariu', 'pqp', 'puts que pariu', 'puta q pariu',
                'carai', 'caralho', 'caraio', 'desgraca', 'desgraça', 'disgraca', 'disgraça', 'viado', 'puta', 'putona',
                'putinha', 'viadão', 'viadao', 'viadinho']

sobrenomesComuns = ['santos', 'souza', 'oliveira', 'carvalho']

nomesComuns = ['lucas', 'joao', 'joão', 'pedro', 'maria', 'francisco', 'francisca', 'jose', 'josé', 'zé', 'ze']

text = text.lower()

def temChingamento(texto):
    for ching in chingamentos:
        if ching in texto:
            return True
    return False


def temNomeComun(texto):
    for nome in nomesComuns:
        if nome in texto:
            return True
    return False


def temSobrenomeComun(texto):
    for sobre in sobrenomesComuns:
        if sobre in texto:
            return True
    return False

def tratamento(texto):
    if temChingamento(texto):
        print("Vou lavar sua boca com Sabão!!")
    else:
        if temNomeComun(texto):
            print("Encontrado Nome Comun!!")
        if temSobrenomeComun(texto):
            print("Encontrado Sobrenome Comun!!")


tratamento(text)