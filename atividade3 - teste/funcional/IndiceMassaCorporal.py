'''Implementar um classificador de Índice de Massa Corporal(IMC) 
(Peso dividido pela altura ao quadrado, medida usada para classificar faixas de peso
corporal) e sua suíte de testes: identificação de classes de equivalência,
cobertura de todas as fronteiras internas com
valores-limite, generalização da função de classificação para
uma tabela de faixas diferente, e construção de uma tabela
de decisão própria com redução por don't care'''


def calcular_imc(peso, altura):
    #erro para ex2 
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero")
    
    imc = peso / (altura ** 2)
    return imc

'''
#ex1
def categorizar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif 18.5 <= imc < 25:
        return "peso normal"
    elif 25 <= imc < 30:
        return "sobrepeso"
    else:  # imc >= 30
        return "obesidade"
'''

'''
#ex1
def classificar_pessoa(peso, altura):
    imc = calcular_imc(peso, altura)
    categoria = categorizar_imc(imc)
    return {
        'imc': round(imc, 2),
        'categoria': categoria
    }
'''

'''
#ex3
def classificar_vento ( velocidade ) :
    if velocidade < 20:
        return "calmo"
    if velocidade < 40:
        return "moderado"
    if velocidade < 60:
        return "forte"
    return "tempestade"
'''

# EX3: Função genérica para classificar por faixas
def classificar_por_feixas(valor, faixas):
    for limite_superior, rotulo in faixas:
        if valor < limite_superior:
            return rotulo
    return None


# Reescrever categorizar_imc usando a função genérica
def categorizar_imc(imc):
    faixas_imc = [
        (18.5, "abaixo do peso"),
        (25, "peso normal"),
        (30, "sobrepeso"),
        (float('inf'), "obesidade")
    ]
    return classificar_por_feixas(imc, faixas_imc)


def classificar_pessoa(peso, altura):
    imc = calcular_imc(peso, altura)
    categoria = categorizar_imc(imc)
    return {
        'imc': round(imc, 2),
        'categoria': categoria
    }

# Reescrever classificar_vento usando a função genérica
def classificar_vento(velocidade):
    faixas_vento = [
        (20, "calmo"),
        (40, "moderado"),
        (60, "forte"),
        (float('inf'), "tempestade")
    ]
    return classificar_por_feixas(velocidade, faixas_vento)

#ex4

''''
Uma loja libera frete grátis quando três condições se cumprem ao mesmo
tempo: valor da compra ≥ R$200, cliente com assinatura premium, e peso
do pedido ≤ 30kg. Fora dessas condições, o frete é cobrado.

a) Implemente tem_frete_gratis(valor_compra,
cliente_premium, peso), monte a tabela de decisão completa (3
condições binárias, 8 regras) e escreva um teste parametrizado
cobrindo as 8 regras, com ids "R1" a "R8".

b) Reduza a tabela por don’t care e escreva a versão reduzida,
justificando cada condição que deixou de importar em cada regra.

'''
def tem_frete_gratis(valor_compra, cliente_premium, peso):
    return valor_compra >= 200 and cliente_premium and peso <= 30

'''
a)
TABELA DE DECISÃO

CONDIÇÃO               |R1 R2 R3 R4 R5 R6 R7 R8
COMPRA >=200           |S  S. S. S. N. N. N. N  
ASSINATURA PREMIUM     |S  S. N. N. S. S. N. N
PESO PEDIDO <=30KG     |S. N. S. N. S. N  S  N
LIBERA FRETE 00,0.     |X 
NAO LIBERA FRETE 0,00. |.  X. X. X  X. X. X. X


b)

CONDIÇÃO               |R1 R2 R3 R4 
COMPRA >=200           |S  S. S. N.  
ASSINATURA PREMIUM     |S  S. N. X.
PESO PEDIDO <=30KG     |S. N. X. X.
LIBERA FRETE 00,0.     |X 
NAO LIBERA FRETE 0,00. |.  X. X. X  

para ter frete gratis todas as 3 condições precisam ser verdadeiras, ou seja, na primeira tabela: 
1-se a primeira condição "N", nada mais importa, por isso removi de R6 a diante e coloquei "X" abaixo do R5 onde a primeira condição é "N" 
2-se a primeira condição for "S", passamos a analisar a segunda, dessa forma, se ela for "N", não importa se a de baixo for sim ou não, será não, por isso coloquei "X" abaixo da segunda condição R4 e da R3  (o que fez com que R4 e R3 ficassem iguais, ou seja, removi uma delas)


'''
