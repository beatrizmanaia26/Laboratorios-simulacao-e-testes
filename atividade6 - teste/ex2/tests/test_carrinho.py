
from carrinho import total_com_desconto


def test_total_com_desconto_maior_que_zero():
    assert total_com_desconto([10, 20, 30, 40, 50]) > 0

'''
Suíte inicial: um teste, assert total_com_desconto([10, 20, 30,
40, 50]) > 0.


a)Meça a cobertura de ramos e o MS. O que os dois números dizem sobre
a suíte?


1-Cobertura de ramos(python3 -m pytest -v --cov=src --cov-branch --cov-report=term-missing)

RESULT:
=========================== tests coverage ================================
______________ coverage: platform darwin, python 3.14.6-final-0 _______________

Name              Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------
src/carrinho.py       7      0      4      0   100%
-------------------------------------------------------------
TOTAL                 7      0      4      0   100%
============================== 1 passed in 0.03s ===========================


2-MS (python3 -m mutmut run e python3 -m mutmut export-cicd-stats):

result:⠼ Generating mutants
    done in 28ms (0 files mutated, 0 ignored, 1 unmodified)
    Warning: 6 non-Python file(s) changed since the last full run: .coverage, atividade1 - testes/funcional/__pycache__/sistemaNotas.cpython-314.pyc, atividade1 - testes/teste/__pycache__/test_sistemaNotas.cpython-314-pytest-9.1.1.pyc, pyproject.toml, src/__pycache__/carrinho.cpython-314.pyc, tests/__pycache__/test_carrinho.cpython-314-pytest-9.1.1.pyc
    These cannot be tracked for behavioral changes, so cached results were kept.
    If the changes affect your tests, delete the mutants/ directory or set on_dependency_change = "rerun".
⠇ Listing all tests 
⠼ Running clean tests
    done
⠋ Running forced fail test
    done
Running mutation testing
⠧ 16/16  🎉 4 🫥 0  ⏰ 0  🤔 0  🙁 12  🔇 0  🧙 0
0.00 mutations/second


-O que os dois números dizem

- 100% de cobertura de ramos: o teste executa os dois lados do if e o fim do for. Todo o código é executado.
- 25% de MS: a suíte detecta só 4 dos 16 defeitos introduzidos. O assert > 0 aceita qualquer valor positivo, então trocas como = no lugar de +=, 0.9 por 1.9 ou mudanças no round passam sem ser notadas.

Conclusão: a cobertura mede se o código roda. O MS mede se o teste verifica o resultado. Aqui o código roda inteiro, mas o resultado quase não é conferido.

- Gerados: 16
- Mortos: 4
- Vivos: 12
- MS = 4 / 16 = 25%

Os vivos são os mutantes 2, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15 e 16.




b) Troque só o assert pelo valor exato, sem mudar a entrada. Quantos
vivos restam?


'''

def test_total_com_desconto_valor_exato():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0


def test_total_com_desconto_com_decimais():
    assert total_com_desconto([11.11, 11.11, 11.11, 11.11]) == 43.33

'''
roda:python3 -m pytest -v

result:
tests/test_carrinho.py::test_total_com_desconto_maior_que_zero PASSED   [ 50%]
tests/test_carrinho.py::test_total_com_desconto_valor_exato PASSED      [100%]

============================== 2 passed in 0.02s ========================


roda:rm -rf mutants
python3 -m mutmut run

result:⠼ Generating mutants
    done in 50ms (1 files mutated, 0 ignored, 0 unmodified)
⠏ Running stats     
    done
⠦ Running clean tests
    done
⠹ Running forced fail test
    done
Running mutation testing
⠏ 16/16  🎉 13 🫥 0  ⏰ 0  🤔 0  🙁 3  🔇 0  🧙 0
266.76 mutations/second


roda:python3 -m mutmut export-cicd-stats e ```bash
python3 -m mutmut results
result:
carrinho.x_total_com_desconto__mutmut_1: no tests
    carrinho.x_total_com_desconto__mutmut_2: no tests
    carrinho.x_total_com_desconto__mutmut_3: no tests
    carrinho.x_total_com_desconto__mutmut_4: no tests
    carrinho.x_total_com_desconto__mutmut_5: no tests
    carrinho.x_total_com_desconto__mutmut_6: no tests
    carrinho.x_total_com_desconto__mutmut_7: no tests
    carrinho.x_total_com_desconto__mutmut_8: no tests
    carrinho.x_total_com_desconto__mutmut_9: no tests
    carrinho.x_total_com_desconto__mutmut_10: no tests
    carrinho.x_total_com_desconto__mutmut_11: no tests
    carrinho.x_total_com_desconto__mutmut_12: no tests
    carrinho.x_total_com_desconto__mutmut_13: no tests
    carrinho.x_total_com_desconto__mutmut_14: no tests
    carrinho.x_total_com_desconto__mutmut_15: no tests
    carrinho.x_total_com_desconto__mutmut_16: no tests
-

RESPOSTA:A mudança para o valor exato mata 13 dos 16 mutantes, e restam __3 vivos__.



c)Para cada vivo que restou, diga qual condição falhou: alcançar, infectar,
propagar ou revelar

`mutmut show` mostra o diff de cada um:

- 13: `round(total, 2)` → `round(total, None)`
- 15: `round(total, 2)` → `round(total, )`
- 16: `round(total, 2)` → `round(total, 3)`

  Os três vivos (13, 15 e 16) trocam o argumento do `round`. Eles __alcançam__ a linha de `return` e __infectam__ o estado, porque o `round` recebe um valor diferente. Mas a falha __não se propaga__ até a saída, e por isso __não é revelada__ pelo teste.

Mutante 13: `round(total, None)

- Alcançar: sim, o `return` é executado.
- Infectar: sim, o argumento de precisão muda de 2 para `None`.
- Propagar: não. `round(141.0, None)` devolve `141`, que é igual a `141.0`.
- Revelar: não. O `assert == 141.0` passa.

Mutante 15: `round(total,)

- Alcançar e infectar: sim, o argumento de precisão é removido.
- Propagar: não. `round(141.0)` devolve `141`, igual a `141.0`.
- Revelar: não.

Mutante 16: `round(total, 3)

- Alcançar e infectar: sim, a precisão passa de 2 para 3.
- Propagar: não. `round(141.0, 3)` devolve `141.0`, igual ao original.
- Revelar: não.





d)Acrescente as entradas que faltam até o MS chegar a 100%. Que tipo de
preço foi preciso?


Rodar os comandos e registrar o MS

python3 -m pytest -v

RESULT:

tests/test_carrinho.py::test_total_com_desconto_maior_que_zero PASSED   [ 33%]
tests/test_carrinho.py::test_total_com_desconto_valor_exato PASSED      [ 66%]
tests/test_carrinho.py::test_total_com_desconto_com_decimais PASSED     [100%]

============================== 3 passed in 0.01s ==============================

RODAR:
rm -rf mutants
python3 -m mutmut run

RESULT:
beatrizmanaia@MacBook-Pro-de-Beatriz ex2 % python3 -m mutmut run
⠼ Generating mutants
    done in 65ms (1 files mutated, 0 ignored, 0 unmodified)
⠋ Running stats     
    done
⠇ Running clean tests
    done
⠼ Running forced fail test
    done
Running mutation testing
⠙ 16/16  🎉 16 🫥 0  ⏰ 0  🤔 0  🙁 0  🔇 0  🧙 0
194.87 mutations/second

RODAR:

python3 -m mutmut export-cicd-stats
python3 -m mutmut results


RESPOSTA:"killed": 16`, "survived": 0 e "total": 16, ou seja, MS de 100%

> Foi preciso um preço com casas decimais que não ficam exatos depois de multiplicar por 0.9. Usei `[11.11, 11.11, 11.11, 11.11]`, que dá `43.33`.
>
> Os inteiros da entrada anterior (10, 20, 30, 40, 50) geram um total exato (141.0), e qualquer precisão de `round` devolve o mesmo valor. Por isso os mutantes 13 (`round(total, None)`), 15 (`round(total, )`) e 16 (`round(total, 3)`) sobreviviam.
>
> Com 11.11, cada mutante dá um resultado diferente do original: 13 e 15 dão `43`, e 16 dá `43.329`. O `== 43.33` mata os três, e o MS chega a 100% (16 de 16).

Depois de colar a resposta no arquivo, dentro da string do d), rode `python3 -m pytest -v` para confirmar que os 3 testes continuam passando.

'''