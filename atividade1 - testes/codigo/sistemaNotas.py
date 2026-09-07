'''Implementar um pequeno sistema de notas e escrever a
suíte de testes completa: convenções de nomenclatura,
asserções, exceções, fixtures, testes parametrizados e boas
práticas, tudo aplicado sobre o mesmo sistema.'''

'''def validar_nota(nota):
    if nota >= 0 and nota <= 10:
        return True
    return False'''


def validar_nota(nota):
    return 0 <= nota <= 10

'''def calcular_media(notas):
    media=0;
    for nota in notas;
       soma+=notas;
    return soma / len(notas)'''

def calcular_media(notas):
    return sum(notas) / len(notas)