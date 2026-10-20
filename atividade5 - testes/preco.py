def preco_final(preco, vip):
    total = preco
    if vip:
        desconto = preco * 0.2
        total = total - desconto
    if total < 50:
        total = 50
    return total


'''EX3

3A - FLUXO DE DADOS

a) Liste as definições e os usos de total e de desconto, com o número da linha e o tipo de uso (c-use ou p-use), e todos os pares du.

DEFINIÇÕES:
Linha 2: total = preco
Linha 4: desconto = preco * 0.2
Linha 5: total = total - desconto
Linha 7: total = 50

USOS:
Linha 5: total (c-use: total * 0.8)
Linha 5: desconto (c-use: - desconto)
Linha 6: total (p-use: if total < 50)
Linha 8: total (c-use: return total)

PARES DU (Definição-Uso):

TOTAL:
(2, 5) - def linha 2 → c-use linha 5 [VIÁVEL: vip=True]
(2, 6) - def linha 2 → p-use linha 6 [VIÁVEL: vip=False]
(2, 8) - def linha 2 → c-use linha 8 [VIÁVEL: vip=False, total >= 50]
(5, 6) - def linha 5 → p-use linha 6 [VIÁVEL: vip=True]
(5, 8) - def linha 5 → c-use linha 8 [VIÁVEL: vip=True, total >= 50]
(7, 8) - def linha 7 → c-use linha 8 [VIÁVEL: total < 50]

DESCONTO:
(4, 5) - def linha 4 → c-use linha 5 [VIÁVEL: vip=True]

PARES NÃO VIÁVEIS:
(2, 7) - L7 redefine total, não usa o valor de L2
(4, 6) - L4 só é alcançado se vip=True, então L5 redefine antes de atingir L6
(4, 8) - L4 só é usado em L5, não chega a L8 diretamente

TOTAL: 7 pares du (6 de total + 1 de desconto)


3B - SUÍTE ATUAL

b) Quais pares a suíte atual não percorre?

Suíte atual: preco_final(60, True) == 50 e preco_final(200, False) == 200

TESTE 1: preco_final(60, True) == 50
Caminho: vip=True, preco=60
- L2: total = 60
- L3: if True (entra)
- L4: desconto = 60 * 0.2 = 12
- L5: total = 60 * 0.8 - 12 = 48 - 12 = 36
- L6: if 36 < 50 (True, entra)
- L7: total = 50
- L8: return 50

Pares percorridos neste teste:
✓ (2, 5) - L2 define total, L5 usa em c-use
✓ (4, 5) - L4 define desconto, L5 usa em c-use
✓ (5, 6) - L5 define total, L6 usa em p-use
✓ (7, 8) - L7 define total, L8 usa em c-use

TESTE 2: preco_final(200, False) == 200
Caminho: vip=False, preco=200
- L2: total = 200
- L3: if False (não entra)
- L6: if 200 < 50 (False, não entra)
- L8: return 200

Pares percorridos neste teste:
✓ (2, 6) - L2 define total, L6 usa em p-use
✓ (2, 8) - L2 define total, L8 usa em c-use

PARES NÃO PERCORRIDOS:
✗ (5, 8) - FALTA! L5 define total, L8 deveria usar (mas L7 redefine antes)

RESUMO DOS 7 PARES:
(2, 5) - ✓ percorrido (Teste 1)
(2, 6) - ✓ percorrido (Teste 2)
(2, 8) - ✓ percorrido (Teste 2)
(4, 5) - ✓ percorrido (Teste 1)
(5, 6) - ✓ percorrido (Teste 1)
(5, 8) - ✗ NÃO percorrido
(7, 8) - ✓ percorrido (Teste 1)

RESPOSTA: 1 par NÃO percorrido: (5, 8)

Por quê?
(5, 8) requer: vip=True, total >= 50 após L5
- No Teste 1 com vip=True: total = 36 (< 50), então L7 redefine e L8 usa L7
- Nunca há um caso onde L5 define um total >= 50 que chegue direto a L8

Exemplo que faltaria: preco_final(300, True) 
→ desconto = 60, total = 300 * 0.8 - 60 = 240 - 60 = 180
→ 180 >= 50, então pula L7 e L8 retorna 180 (usando valor de L5)




3C - ALL-USES

c) Escreva, a partir da especificação, o que falta para completar All-Uses. 
   O que acontece, e por que a suíte atual não viu o defeito?

DEFEITO NA FUNÇÃO:
Linha 5: total = total * 0.8 - desconto

Esta linha está ERRADA. Deveria ser:
total = total - desconto
ou
total = preco * 0.8

O que foi feito de errado:
- Está multiplicando total por 0.8 E depois subtraindo desconto
- Está diminuindo total DUAS VEZES: primeiro por 0.8 (20% off = 80%), depois por desconto novamente

COMO COMPLETAR ALL-USES:
Faltava o par (5, 8): vip=True, total >= 50 após L5

Teste que falta: preco_final(300, True)
Esperado (CORRETO): 300 * 0.8 = 240
Atual (DEFEITO): 300 * 0.8 - 60 = 180

Com este teste:
- L5 definiria total = 180
- L6: if 180 < 50? (False, não entra)
- L8: return 180 (usando valor de L5)

O DEFEITO SERIA VISÍVEL!

POR QUE A SUÍTE ATUAL NÃO VIU O DEFEITO?
Teste 1 com vip=True: preco_final(60, True)
- L5: total = 60 * 0.8 - 12 = 48 - 12 = 36
- L6: if 36 < 50? (True, entra)
- L7: total = 50 (REDEFINE, mascarando o erro!)
- L8: return 50 (esperado: 60 * 0.8 = 48, mas L7 "corrigiu" para 50)

O teste passou porque o mínimo de R$50 "consertou" acidentalmente o resultado!

Teste 2 com vip=False: preco_final(200, False)
- Não entra em L5, então desconto nunca é usado
- Não testa a lógica de aplicar desconto

CONCLUSÃO:
All-Uses requer testar TODOS os pares du, incluindo (5, 8).
Sem o teste preco_final(300, True), o defeito permaneceu escondido.
O par (5, 8) faltante é essencial para detectar a lógica errada em L5.



3D - CORREÇÃO E TESTES

d) Corrija a função e rode a suíte inteira

CORREÇÃO APLICADA:
Linha 5 ANTES (ERRADA):
    total = total * 0.8 - desconto

Linha 5 DEPOIS (CORRIGIDA):
    total = total - desconto

EXPLICAÇÃO:
- A versão errada multiplicava por 0.8 (80%) E depois subtraía o desconto
- Isso resultava em desconto duplo: 20% de multiplicação + 20% de subtração = 40% total
- A correção aplica apenas uma vez: subtrai 20% do preço como desconto

SUÍTE COMPLETA RODADA - TODOS OS 7 PARES DU:
✓ Teste 1 (2,5): preco_final(60, True) → 50 (L2 define, L5 usa)
✓ Teste 2 (2,6): preco_final(200, False) → 200 (L2 define, L6 verifica)
✓ Teste 3 (2,8): preco_final(100, False) → 100 (L2 define, L8 retorna)
✓ Teste 4 (4,5): preco_final(60, True) → 50 (L4 desconto, L5 usa)
✓ Teste 5 (5,6): preco_final(60, True) → 50 (L5 define, L6 verifica < 50)
✓ Teste 6 (5,8): preco_final(300, True) → 240 (L5 define 240, L8 retorna) **ANTES FALTAVA**
✓ Teste 7 (7,8): preco_final(40, False) → 50 (L7 define mínimo, L8 retorna)

✅ RESULTADO: TODOS OS 7 TESTES PASSARAM!
✅ O defeito foi corrigido!
✅ Todos os pares du foram percorridos!

IMPACTO DO PAIR (5,8):
Antes: O teste preco_final(300, True) NÃO EXISTIA
Depois: preco_final(300, True) = 240 (correto!)

Sem este teste, o defeito permaneceria escondido porque:
- Teste 1 (preco_final(60, True)): total < 50, então L7 mascara o erro
- Teste 2 (preco_final(200, False)): não ativa VIP, então nunca usa L5
- O pair (5,8) é CRÍTICO para validar que L5 produz um resultado >= 50 que chegue a L8
'''