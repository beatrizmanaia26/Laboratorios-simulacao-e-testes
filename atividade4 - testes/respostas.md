<!-- 
para rodar:

python3 -m venv .venv
source .venv/bin/activate
pip install pytest
-->

ex 1b

CE.           INTERVALO              VALOR                  TIPO
CE01      0 ≤ minutos ≤ 15          0.0                   VÁLIDA
CE02      16 ≤ minutos ≤ 180        12.0                  VÁLIDA
CE03a     181 ≤ minutos ≤ 240       15.0                  VÁLIDA
CE03b     241 ≤ minutos ≤ 300       18.0                  VÁLIDA
CE03c     301 ≤ minutos ≤ 360       21.0                  VÁLIDA
CE03d     361 ≤ minutos ≤ 420       24.0                  VÁLIDA
CE03e     421 ≤ minutos ≤ 480       27.0                  VÁLIDA
CE03f     481 ≤ minutos ≤ 540       30.0                  VÁLIDA
CE03g     541 ≤ minutos ≤ 600       33.0                  VÁLIDA
CE03h     601 ≤ minutos ≤ 660       36.0                  VÁLIDA
CE03i     661 ≤ minutos ≤ 720       39.0                  VÁLIDA
CE04      minutos > 720             60.0                  VÁLIDA
CE05      minutos < 0               ValueError            INVÁLIDA
CE06      minuto ≠ int              TypeError             INVÁLIDA




ex2

Um estagiário implementou a tabela de cobrança como no slide anterior, e o
código já está em produção.
a) Sem executar o código, encontre todas as divergências em relação à
especificação. Para cada uma, dê o menor valor de entrada que a
revela, o valor devolvido, o valor esperado e a correção.

RESPOSTA:
DIVERGÊNCIA 1: Validação de Zero (CRÍTICA)
LINHA PROBLEMÁTICA:
   if minutos <= 0:
       raise ValueError("minutos nao pode ser negativo")

PROBLEMA:
   - Zero é aceito pela especificação (0 a 15 = grátis)
   - Código rejeita 0 como se fosse negativo
   - A condição deveria ser "minutos < 0", não "minutos <= 0"

MENOR VALOR QUE REVELA:
   minutos = 0

VALOR DEVOLVIDO:
   ValueError("minutos nao pode ser negativo")

VALOR ESPERADO:
   0.0 (grátis)

CORREÇÃO:
   if minutos < 0:
       raise ValueError("minutos nao pode ser negativo")

DIVERGÊNCIA 2: Limite Inferior da Faixa 1 (CRÍTICA)
LINHA PROBLEMÁTICA:
   if minutos < 15:
       return 0.00

PROBLEMA:
   - 15 minutos deveria ser grátis (0 a 15 minutos)
   - Código exclui 15, retorna 12.00 em vez de 0.00
   - A condição deveria ser "minutos <= 15", não "minutos < 15"

MENOR VALOR QUE REVELA:
   minutos = 15

VALOR DEVOLVIDO:
   12.0

VALOR ESPERADO:
   0.0

CORREÇÃO:
   if minutos <= 15:
       return 0.00

DIVERGÊNCIA 3:

LINHA PROBLEMÁTICA:
   return 12.00 + 3.00 * ((minutos - 180) // 60)

PROBLEMA:
   - Usa divisão inteira (//) que TRUNCA a fração
   - Especificação: "fração de hora também cobra hora cheia"
   - 181 minutos = 180 + 1 minuto = 1 hora adicional = R$ 15,00
   - Código calcula: (1 // 60) = 0 horas = R$ 12,00 (ERRADO!)
   - 241 minutos = 180 + 61 minutos = 2 horas adicionais = R$ 18,00
   - Código calcula: (61 // 60) = 1 hora = R$ 15,00 (ERRADO!)
   - Deve usar math.ceil() para arredondar frações para cima

MENOR VALOR QUE REVELA:
   minutos = 181

VALOR DEVOLVIDO:
   12.0

VALOR ESPERADO:
   15.0 (12.00 + 3.00 * 1)

CORREÇÃO:
   import math
   return 12.00 + 3.00 * math.ceil((minutos - 180) / 60)

DIVERGÊNCIA 4: 

 LINHA PROBLEMÁTICA:
   if minutos < 720:
       return 12.00 + 3.00 * ((minutos - 180) // 60)
   return 60.00

PROBLEMA:
   - 720 minutos deveria estar na faixa 3 (181 a 720)
   - Código inclui 720 no cálculo de faixa 3 (correto por acaso)
   - MAS: após corrigir divergência 3, 720 retorna 60.00 em vez de 39.00
   - A condição deveria ser "minutos <= 720", não "minutos < 720"

MENOR VALOR QUE REVELA:
   minutos = 720

VALOR DEVOLVIDO:
   60.0 (após corrigir divergência 3)

VALOR ESPERADO:
   39.0 (12.00 + 3.00 * 9 horas)
   
EXPLICAÇÃO DO CÁLCULO:
   720 - 180 = 540 minutos adicionais
   540 / 60 = 9 horas exatas
   12.00 + 3.00 * 9 = 39.00

CORREÇÃO:
   if minutos <= 720:
       return 12.00 + 3.00 * math.ceil((minutos - 180) / 60)
   return 60.00


b) Copie a suíte do Exercício 1 para test_estagiario.py, importando
desta versão, e rode. Ela detecta todas as divergências?

Sim! 100% das divergências são detectadas!


c) Uma suíte com um único representante por classe válida (8, 100, 300 e
1000 minutos) detectaria alguma delas? Explique o resultado.

Uma suíte com apenas representantes não detecta nenhuma das 4 divergências.
Representantes testam a lógica geral do código, verificam se o fluxo básico funciona, mas não testam os limites das condições () erros em < vs <= ficam invisíveis e erros em arredondamento de frações ficam invisíveis

Ou seja, a escolha do representante importa 300 foi "sorte" (múltiplo de 60), se fosse 181, o erro seria revelado!


ex3
a)

Condicoes:
C1: Credencial (PCD ou idoso)? SIM/NAO
C2: Compras >= R$ 150,00? SIM/NAO
C3: Cadastro no app? SIM/NAO
C4: Permanencia <= 240 min? SIM/NAO


 Caso | C1  | C2  | C3  | C4  | Resultado
  1   | SIM | SIM | SIM | SIM | ISENTO
  2   | SIM | SIM | SIM | NAO | ISENTO
  3   | SIM | SIM | NAO | SIM | ISENTO
  4   | SIM | SIM | NAO | NAO | ISENTO
  5   | SIM | NAO | SIM | SIM | ISENTO
  6   | SIM | NAO | SIM | NAO | ISENTO
  7   | SIM | NAO | NAO | SIM | ISENTO
  8   | SIM | NAO | NAO | NAO | ISENTO
  9   | NAO | SIM | SIM | SIM | ISENTO
  10  | NAO | SIM | SIM | NAO | PAGA
  11  | NAO | SIM | NAO | SIM | ISENTO
  12  | NAO | SIM | NAO | NAO | PAGA
  13  | NAO | NAO | SIM | SIM | ISENTO
  14  | NAO | NAO | SIM | NAO | PAGA
  15  | NAO | NAO | NAO | SIM | PAGA
  16  | NAO | NAO | NAO | NAO | PAGA



ex4)
a)
REGRAS QUE ISENTO_ERRADO.PY ERRA:

REGRA R11: pcd=NAO, compras=150.00, cadastro=NAO, permanencia=240
- Esperado: True (ISENTO)
- Obtido: False (PAGA)
- Por quê: Usa minutos < 240 em vez de minutos <= 240

REGRA R13: pcd=NAO, compras=0.00, cadastro=SIM, permanencia=240
- Esperado: True (ISENTO)  
- Obtido: False (PAGA)
- Por quê: Usa minutos < 240 em vez de minutos <= 240

b)
O teste do colega nao testou permanencia = 240 (no limite exato).
So testou permanencia = 100 (abaixo do limite) nos casos ISENTO.

240 eh EXATAMENTE o limite: permanencia <= 240 eh ISENTO, > 240 eh PAGA.

Por isso isento_errado.py passa no teste do colega (100 < 240 eh verdade).
Mas falha com 240 (240 < 240 eh falso).


OS 5 CASOS CORRIGIDOS:

Mude permanencia de 100 para 240 em R1, R3 e R4:

ORIGINAL:
(True, 0.00, False, 100, True),
(False, 200.00, False, 300, False),
(False, 200.00, False, 100, True),
(False, 50.00, True, 100, True),
(False, 50.00, False, 100, False),

CORRIGIDO:
(True, 0.00, False, 240, True),
(False, 200.00, False, 300, False),
(False, 200.00, False, 240, True),
(False, 50.00, True, 240, True),
(False, 50.00, False, 100, False),


RESULTADO:

Com isento.py: 5/5 passam
Com isento_errado.py: 3/5 passam, 2/5 falham (R3 e R4)

R3 falha: (200 >= 150) AND (240 < 240) = False
R4 falha: (cadastro) AND (240 < 240) = False

c)Use o VALOR-LIMITE da condicao, nao um valor qualquer.

O valor-limite eh aquele que separa True de False.

Exemplos:
- Condicao "valor_compra >= 150": use valor_compra = 150 (no limite), nao 200
- Condicao "minutos <= 240": use minutos = 240 (no limite), nao 100

Por quê? Porque erros subtis (como "< 240" em vez de "<= 240") so sao
detectados quando testamos exatamente no limite, nao valores aleatorios.
