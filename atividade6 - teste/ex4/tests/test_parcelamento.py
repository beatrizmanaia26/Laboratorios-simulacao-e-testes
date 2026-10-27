import pytest

from parcelamento import parcela


@pytest.mark.parametrize("n, esperado", [
    (1, 100.00),
    (2, 50.00),
    (11, 10.55),
    (12, 9.83),
], ids=["minimo", "minimo_mais_um", "maximo_menos_um", "maximo"])
def test_parcela_nos_limites_validos(n, esperado):
    assert parcela(100, n) == esperado


@pytest.mark.parametrize("n", [0, 13], ids=["abaixo_minimo", "acima_maximo"])
def test_parcela_fora_dos_limites_lanca_erro(n):
    with pytest.raises(ValueError):
        parcela(100, n)



'''
a) Antes de rodar qualquer ferramenta, derive a suíte por valor-limite
(aula 6) e implemente

'''

'''
 a) Resposta:
 Intervalo válido de n: [1, 12] (n < 1 ou n > 12 gera ValueError).
 Valores-limite pela regra A-1, A, A+1, B-1, B, B+1:
   n = 0  (A-1)  inválido  -> ValueError
   n = 1  (A)    válido    -> 100.00 (valor = 100, juros = 0)
   n = 2  (A+1)  válido    -> 50.00
   n = 11 (B-1)  válido    -> 10.55 (juros = 0.16, total = 116)
   n = 12 (B)    válido    -> 9.83  (juros = 0.18, total = 118)
   n = 13 (B+1)  inválido  -> ValueError
 Esperados calculados à mão antes de rodar a ferramenta.

 Limitação: a fronteira interna entre as faixas de juros (n = 3 e n = 4)
 não está nos seis valores, por isso o mutante n <= 3 -> n <= 4 sobrevive.


b) Meça a cobertura de ramos e o MS dessa suíte

Medição (pytest --cov --cov-branch e mutmut run):
 Cobertura de ramos: 100% (src/parcelamento.py: 4 ramos, 0 parciais, 0 linhas faltando).
 MS: 22 mortos de 27 mutantes gerados = 81% (killed 22, survived 5, total 27).
 Vivos:
   mutantes 6, 7 e 8: mensagem do ValueError. pytest.raises sem match não a verifica.
   mutante 9 (n <= 3 -> n < 3): equivalente, em n = 3 juros = 0.02 * 0 = 0.
   mutante 10 (n <= 3 -> n <= 4): não equivalente, em n = 4 o mutante não aplica juros.
 Os números foram medidos na rodada anterior, com o mesmo código de teste.


c) Analise cada vivo: mate-o ou justifique que é equivalente. Qual o MS
final?

Resposta (análise de cada vivo):
  mutante 6, 7 e 8 (mensagem do ValueError): NÃO é equivalente. A suíte só
    checa o tipo da exceção. Mata-se com match="^parcelas invalidas$" em
    pytest.raises. Não foi adicionado nesta suíte.
  mutante 9 (n <= 3 -> n < 3): EQUIVALENTE. Em n = 3 o original calcula
    juros = 0 e o mutante calcula juros = 0.02 * (3 - 3) = 0.0. Como 1 + 0.0 = 1,
    total e parcela são iguais para qualquer valor. Justificado, não é morto.
  mutante 10 (n <= 3 -> n <= 4): NÃO é equivalente. Em n = 4 o original dá
    juros = 0.02, total = 102.0, parcela = 25.5, e o mutante dá 25.0.
    Mata-se com o caso (4, 25.50) no parametrize. Não foi adicionado.
  MS atual (sem alterar a suíte): 22 mortos / (27 - 1 equivalente) = 22/26 = 85%.
  MS se os mutantes 6, 7, 8 e 10 forem mortos: 26/26 = 100%.
  Os valores acima são cálculo à mão, não uma nova medição.



d) Combine à mão dois mutantes de primeira ordem que sua suíte mata,
num de segunda ordem

  Mutante A (primeira ordem): n < 1 -> n <= 1. Com n = 1, o original é válido
    e retorna 100.00, mas o mutante lança ValueError. O teste de n = 1 falha,
    então A é morto.
  Mutante B (primeira ordem): n > 12 -> n >= 12. Com n = 12, o original é válido
    e retorna 9.83, mas o mutante lança ValueError. O teste de n = 12 falha,
    então B é morto.
  Mutante de segunda ordem (A e B juntos):
    if n <= 1 or n >= 12:
    Combinação feita à mão. Com n = 1 e n = 12, o original retorna valor, mas
    o mutante de segunda ordem lança ValueError. A suíte falha nesses dois
    casos, então o mutante de segunda ordem é morto.
  Efeito de acoplamento: os dois defeitos se manifestam nos mesmos valores de
    entrada e na mesma direção (ambos viram ValueError onde deveria haver
    valor). Não há mascaramento, porque um defeito não cancela o outro.
  Offutt (1992): a hipótese do acoplamento diz que defeitos complexos estão
    acoplados aos simples, então uma suíte que mata os mutantes simples tende a
    matar os de ordem superior. Aqui isso se confirma: a suíte mata o mutante
    de segunda ordem pelos mesmos casos que matam A e B.
  Ressalva: os IDs de mutmut de A e B não foram conferidos (o terminal travou).
    Antes de citá-los, confirme em `python3 -m mutmut results`.



e) A suíte mata o mutante de segunda ordem? Relacione com o efeito de
acoplamento e com Offutt (1992)

  Resposta: sim, a suíte mata o mutante de segunda ordem (if n <= 1 or n >= 12:).
    Os casos que matam A (n = 1) e B (n = 12) também o matam, porque ele
    lança ValueError nos mesmos dois valores em que o original retorna número.
  Acoplamento: o mutante de segunda ordem só é morto se a suíte matar A e B
    juntos. Os dois defeitos se manifestam nos mesmos valores, então a suíte
    que mata os simples também mata o composto. Não há mascaramento.
  Offutt (1992): a hipótese do acoplamento diz que a suíte que mata todos os
    mutantes simples também mata quase todos os de segunda ordem. Aqui isso se
    confirma. Offutt também mostra que, quando o acoplamento não ocorre, o
    mutante composto pode sobreviver mesmo com os simples mortos.
  Ressalva: esta análise é à mão. Para medir, seria preciso combinar os mutantes
    no código e rodar o mutmut, o que não foi feito.




'''