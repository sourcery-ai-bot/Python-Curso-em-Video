def aumentar(preço=0, taxa=0, formato=False):
    '''
    :param preço: Preço digitado pelo usuário.
    :param taxa: Taxa aplicada para aumentar o preço do usuário.
    :param formato: Formatação em R$ se True e sem Formatação se False
    :return: Resultado do preço com a taxa aplicada.
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')