import pytest
from isencao import isento

teste_regras = [
    ("R1", True, 150.00, True, 240, True),
    ("R2", True, 150.00, True, 241, True),
    ("R3", False, 150.00, False, 240, True),
    ("R4", False, 149.99, False, 240, False),
    ("R5", False, 0.00, True, 240, True),
    ("R6", False, 0.00, False, 240, False),
    ("R7", False, 150.00, False, 241, False),
    ("R8", False, 0.00, True, 241, False),
]


@pytest.mark.parametrize(
    teste_regras,
    ids=[t[0] for t in teste_regras]  
)
def test_tabela_decisao_reduzida(regra_id, pcd, valor_compra, cadastro_app, minutos, esperado):

    resultado = isento(pcd, valor_compra, cadastro_app, minutos)
    assert resultado == esperado, (
        f"Regra {regra_id} falhou: "
        f"isento(pcd={pcd}, valor_compra={valor_compra}, "
        f"cadastro_app={cadastro_app}, minutos={minutos}) "
        f"retornou {resultado}, esperado {esperado}"
    )