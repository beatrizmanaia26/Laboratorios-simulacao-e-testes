'''Implementar um pequeno sistema de notas e escrever a
suíte de testes completa: convenções de nomenclatura,
asserções, exceções, fixtures, testes parametrizados e boas
práticas, tudo aplicado sobre o mesmo sistema.'''

#exercício 1

'''def validar_nota(nota):
    if nota >= 0 and nota <= 10:
        return True
    return False'''


def validar_nota(nota):
    if not isinstance(nota, (int, float)):
        return False
    return 0 <= nota <= 10

'''def calcular_media(notas):
    media=0;
    for nota in notas;
       soma+=notas;
    return soma / len(notas)'''

def calcular_media(notas):
    if not notas:  
        raise ValueError("lista de notas vazia")
    return sum(notas) / len(notas)

#exercício3 e 4
def obter_situacao(media):
    if media >= 7:  
        return "Aprovado"
    elif media >= 5:  
        return "Recuperacao"
    else:
        return "Reprovado"
