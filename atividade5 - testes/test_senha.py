import pytest
from senha import forca

"""
EXERCICIO 1 - ITEM C: Teste com parametrize dos 6 caminhos independentes

Caminhos identificados:
- caminho1: 2,3 (senha < 8 retorna "fraca")
- caminho2: 2,4,5,10,12 (senha >= 8, sem dígitos/símbolos, retorna "media")
- caminho3: 2,4,5,6,7,5,10,12 (percorre for com dígito, pontos < 4, retorna "media")
- caminho4: 2,4,5,10,11 (percorre for, pontos >= 4, retorna "forte")
- caminho5: 2,4,5,6,8,5,10,11 (percorre for com símbolo, pontos >= 4, retorna "forte")
- caminho6: 2,4,5,6,8,9,5,12 (percorre for com símbolo, pontos >= 4, retorna "media")

V(G) = 6 caminhos independentes

Cada teste deve ser independente e cobrir um caminho diferente.
"""


@pytest.mark.parametrize(
    "senha,esperado,descricao",
    [
        # CAMINHO 1: 2,3 - Senha com menos de 8 caracteres retorna "fraca"
        ("abc", "fraca", "caminho1: len(senha) < 8, retorna fraca"),
        ("1234567", "fraca", "caminho1: 7 caracteres, retorna fraca"),
        
        # CAMINHO 2: 2,4,5,10,12 - Senha >= 8 com apenas letras, retorna "media"
        ("abcdefgh", "media", "caminho2: 8 letras, sem dígitos/símbolos, pontos=0, retorna media"),
        
        # CAMINHO 3: 2,4,5,6,7,5,10,12 - Com dígito (pontos=1 ou 2 ou 3), retorna "media"
        ("abcde1fg", "media", "caminho3: tem 1 dígito, pontos=1 < 4, retorna media"),
        ("abcde12g", "media", "caminho3: tem 2 dígitos, pontos=2 < 4, retorna media"),
        ("abc12def", "media", "caminho3: tem 2 dígitos, pontos=2 < 4, retorna media"),
        
        # CAMINHO 4: 2,4,5,10,11 - Com dígitos OU símbolos, pontos >= 4, retorna "forte"
        ("abc1234d", "forte", "caminho4: tem 4 dígitos, pontos=4 >= 4, retorna forte"),
        ("a1234def", "forte", "caminho4: tem 4 dígitos, pontos=4 >= 4, retorna forte"),
        
        # CAMINHO 5: 2,4,5,6,8,5,10,11 - Com símbolo especial, pontos >= 4, retorna "forte"
        ("abcde@!#g", "forte", "caminho5: tem 3 símbolos, pontos=6 >= 4, retorna forte"),
        ("abc@!#$gh", "forte", "caminho5: tem 4 símbolos, pontos=8 >= 4, retorna forte"),
        
        # CAMINHO 6: 2,4,5,6,8,9,5,12 - Com símbolo, mas pontos < 4, retorna "media"
        ("abcdefg@", "media", "caminho6: 8 chars, tem 1 símbolo, pontos=2 < 4, retorna media"),
        ("abcdefgh", "media", "caminho6b: 8 chars, sem símbolos/dígitos, pontos=0 < 4, retorna media"),
        
        # CASOS ADICIONAIS para garantir 100% de branch coverage
        ("abc12@#$", "forte", "cobertura adicional: múltiplos dígitos e símbolos"),
        ("abcd12ef", "media", "cobertura adicional: 2 dígitos, pontos=2"),
    ],
)
def test_forca_caminhos_independentes(senha, esperado, descricao):
    resultado = forca(senha)
    assert resultado == esperado, f"Falha: {descricao}. Esperado {esperado}, obteve {resultado}"

class TestForcaBranchCoverage:

    def test_senha_vazia(self):
        assert forca("") == "fraca"
    
    def test_senha_exatamente_8_caracteres_letras(self):
        assert forca("abcdefgh") == "media"
    
    def test_senha_com_um_digito(self):
        assert forca("abcdefg1") == "media"
    
    def test_senha_com_tres_digitos(self):
        assert forca("abcde123") == "media"
    
    def test_senha_com_quatro_digitos(self):
        assert forca("abcd1234") == "forte"
    
    def test_senha_com_um_simbolo(self):
        assert forca("abcdefg@") == "media"
    
    def test_senha_com_dois_simbolos(self):
        assert forca("abcdefg@@") == "forte"
    
    def test_senha_com_digito_e_simbolo(self):
        assert forca("abcdef1@g") == "media"
    
    def test_senha_com_digito_e_dois_simbolos(self):
        assert forca("abcde1@@g") == "forte"
    
    def test_senha_longa_sem_pontos(self):
        assert forca("abcdefghijklmnop") == "media"
    
    def test_senha_multiplos_digitos_simbolos(self):
        assert forca("a1b2c3@!") == "forte"
