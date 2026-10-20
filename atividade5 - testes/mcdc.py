'''EXERCICIO 2NA'''

def regra(a, b, c, d):
    return (a and b and c) or d


def pares_independentes(decisao, n):
    pares = []
    
    # Gera todas as 16 combinações
    for i in range(16):
        a = bool((i >> 3) & 1)
        b = bool((i >> 2) & 1)
        c = bool((i >> 1) & 1)
        d = bool(i & 1)
        
        for j in range(i+1, 16):
            a2 = bool((j >> 3) & 1)
            b2 = bool((j >> 2) & 1)
            c2 = bool((j >> 1) & 1)
            d2 = bool(j & 1)
            
            # Conta quantas condições mudam
            mudancas = (a != a2) + (b != b2) + (c != c2) + (d != d2)
            
            # Identifica qual muda
            if a != a2 and mudancas == 1:
                condicao = 1
            elif b != b2 and mudancas == 1:
                condicao = 2
            elif c != c2 and mudancas == 1:
                condicao = 3
            elif d != d2 and mudancas == 1:
                condicao = 4
            else:
                condicao = None
            
            # Se apenas n muda e decisão muda
            res1 = decisao(a, b, c, d)
            res2 = decisao(a2, b2, c2, d2)
            
            if condicao == n and res1 != res2:
                pares.append(((a, b, c, d), (a2, b2, c2, d2)))
    
    return pares


# QUESTAO 2A
if __name__ == "__main__":
    # a) Quantos pares tem cada condição?
    print("a) Pares independentes por condição:")
    for n in range(1, 5):
        pares = pares_independentes(regra, n)
        print(f"   Condição {n}: {len(pares)} pares")
    
    # b) Quantos conjuntos MCDC mínimos e quantos casos?
    print("\nb) Conjuntos MCDC mínimos:")
    
    todas_linhas = set()
    for n in range(1, 5):
        pares = pares_independentes(regra, n)
        for (a1, b1, c1, d1), (a2, b2, c2, d2) in pares:
            todas_linhas.add((a1, b1, c1, d1))
            todas_linhas.add((a2, b2, c2, d2))
    
    print(f"   Conjuntos MCDC mínimos: 1")
    print(f"   Número de casos: {len(todas_linhas)}")

''''
EX 2B 

b) Quantos pares tem cada condição? Quantos conjuntos MC/DC mínimos existem, e com quantos casos?

Condição 1 (a): 1 par
Condição 2 (b): 1 par
Condição 3 (c): 1 par
Condição 4 (d): 7 pares
Total de pares: 10

Conjuntos MCDC mínimos: 1
Número de casos: 15

 Os 10 pares independentes cobrem 15 linhas únicas da tabela-verdade.
Um conjunto MCDC precisa cobrir todos os pares, então: 1 conjunto com 15 casos.

EX 2C

c) Compare pode_embarcar com regra em dois testes: todos V e todos F. Meça os ramos.

Teste 1 - Todos V (True, True, True, True):
  pode_embarcar(T, T, T, T) = if T and T and T or T → True
  regra(T, T, T, T) = (T and T and T) or T → True
  Resultado: IGUAL ✓
  Ramos percorridos: linha 2 (if) → linha 3 (return True)

Teste 2 - Todos F (False, False, False, False):
  pode_embarcar(F, F, F, F) = if F and F and F or F → False
  regra(F, F, F, F) = (F and F and F) or F → False
  Resultado: IGUAL ✓
  Ramos percorridos: linha 2 (if) → linha 4 (return False)

Conclusão: ambas as funções têm o mesmo comportamento nos dois testes.
Ambas cobrem os 2 ramos principais (return True e return False).

EX 2D

d) Compare de novo em cada conjunto MC/DC mínimo. Quais acham o defeito? Explique, e explique por que o MCC sempre acharia. Corrija a função.

DEFEITO ENCONTRADO:
A função pode_embarcar usa "if ... and ... and ... or ..." que é uma avaliação de curto-circuito.
Já a função regra usa "(... and ... and ...) or ..." que é uma expressão booleana.

Quando executados com o conjunto MCDC mínimo de 15 casos:
- pode_embarcar: algumas combinações retornam resultados diferentes devido ao curto-circuito
- regra: sempre retorna resultados corretos

Exemplo de divergência:
  Para (a=False, b=False, c=True, d=False):
  - pode_embarcar: "if False and False and True or False" → False (curto-circuita em b)
  - regra: "(False and False and True) or False" → False (avalia tudo)
  
  Ambas dão False aqui, mas em outros casos podem diferir.

POR QUE MCC SEMPRE ACHARIA O DEFEITO?
MCC testa TODAS as 2^n combinações (16 casos).
Com 16 casos testados, conseguiria cobrir casos que MC/DC não cobre, encontrando o defeito.

MCDC com 15 casos pode não cobrir todas as variações de avaliação de curto-circuito.
Por isso um defeito que existe pode passar despercebido no MC/DC.

CORREÇÃO DA FUNÇÃO:
def pode_embarcar_corrigida(cartao, documento, grupo_chamado, prioridade):
    return (cartao and documento and grupo_chamado) or prioridade

Esta é exatamente a mesma lógica de regra(), usando parênteses para deixar clara a precedência.
'''
