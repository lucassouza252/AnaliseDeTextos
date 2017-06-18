text = input("Digite seu nome e uma frase: ")

chingamentos = ['porra', 'porr', 'merds', 'merda', 'merd', 'puta que pariu', 'pqp', 'puts que pariu', 'puta q pariu',
                'carai', 'caralho', 'caraio', 'desgraca', 'desgraça', 'disgraca', 'disgraça', 'Viado', 'viado',
                'Puta', 'puta', 'Putona', 'putona', 'Putinha', 'putinha', 'Viadão', 'Viadao', 'viadão', 'viadao',
                'Viadinho', 'viadinho', 'Caralho']

sobrenomesComuns = ['Santos', 'santos', 'Souza', 'souza', 'Oliveira', 'oliveira', 'Carvalho', 'carvalho']

nomesComuns = ['Lucas', 'lucas', 'joao', 'joão', 'Pedro', 'pedro', 'Maria', 'maria', 'Francisco', 'Francisca',
               'francisco', 'francisca', 'Jose', 'José', 'jose', 'josé', 'Zé', 'Ze', 'zé', 'ze']


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