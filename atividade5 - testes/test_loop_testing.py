import pytest
from senha import forca

"""
EXERCICIO 1 - ITEM D: TESTE DE LAÇOS (LOOP TESTING)

Análise do laço: for c in senha (linha 5)
Categorias de voltas possíveis:
  - 0 voltas: laço não executa (senha com menos de 8 caracteres)
  - 1 volta: laço executa 1 vez
  - 2 voltas: laço executa 2 vezes
  - N voltas: laço executa N vezes (múltiplas voltas)
  - Limite mínimo: 8 caracteres (len >= 8)
  - Limite máximo: sem limite definido no código
"""

@pytest.mark.parametrize(
    "senha,num_voltas,descricao",
    [
        # 0 VOLTAS: Laço não executa (len < 8)
        ("abc", 0, "0 voltas: len=3 < 8, laço não executa, retorna fraca"),
        ("1234567", 0, "0 voltas: len=7 < 8, laço não executa, retorna fraca"),
        ("", 0, "0 voltas: senha vazia, len=0 < 8, retorna fraca"),
        
        # 1 VOLTA: Laço executa exatamente 1 vez
        ("abcdefg1", 1, "1 volta: len=8, laço testa 1 caractere (dígito), pontos=1"),
        ("abcdefg@", 1, "1 volta: len=8, laço testa 1 caractere (símbolo), pontos=2"),
        ("abcdefgh", 1, "1 volta: len=8, laço testa 1 caractere (letra), pontos=0"),
        
        # 2 VOLTAS: Laço executa exatamente 2 vezes
        ("abcdefg12", 2, "2 voltas: len=9, laço testa 2 dígitos, pontos=2"),
        ("abcdefg1@", 2, "2 voltas: len=9, laço testa 1 dígito + 1 símbolo, pontos=3"),
        ("abcdefg@@", 2, "2 voltas: len=9, laço testa 2 símbolos, pontos=4, retorna forte"),
        
        # N VOLTAS: Laço executa múltiplas vezes
        ("abcdef1234", 4, "4 voltas: len=10, laço testa 4 dígitos, pontos=4, retorna forte"),
        ("abcde12@#$", 5, "5 voltas: len=11, laço testa 2 dígitos + 3 símbolos, pontos=8"),
        ("a1b2c3d4e5", 10, "10 voltas: len=10, laço testa 5 dígitos, pontos=5"),
        
        # CASO LIMITE: Mínimo de voltas possíveis (len = 8)
        ("12345678", 8, "Limite mínimo: 8 voltas, len=8, 8 dígitos, pontos=8"),
        
        # CASO TÍPICO: Senha válida com múltiplas voltas
        ("senha1234", 9, "Caso típico: len=9, senha com 4 dígitos, pontos=4"),
        ("pass@word", 9, "Caso típico: len=9, senha com 1 símbolo, pontos=2"),
    ],
)
def test_forca_loop_testing(senha, num_voltas, descricao):
    """Teste de Laços (Loop Testing) para a função forca."""
    resultado = forca(senha)
    assert resultado in ["fraca", "media", "forte"], f"Resultado inválido: {resultado}"
    assert len(senha) >= 8 or resultado == "fraca", f"Falha: {descricao}"


class TestLoopBehavior:

    def test_loop_zero_voltas(self):
        assert forca("abc") == "fraca"
        assert forca("") == "fraca"
        assert forca("1234567") == "fraca"
    
    def test_loop_uma_volta(self):
        assert forca("abcdefg1") == "media"  # 1 dígito = 1 ponto
        assert forca("abcdefg@") == "media"  # 1 símbolo = 2 pontos
        assert forca("abcdefgh") == "media"  # 1 letra = 0 pontos
    
    def test_loop_duas_voltas(self):
        assert forca("abcdefg12") == "media"   # 2 dígitos = 2 pontos
        assert forca("abcdefg@@") == "forte"   # 2 símbolos = 4 pontos
        assert forca("abcdefg1@") == "media"   # 1 dígito + 1 símbolo = 3 pontos
    
    def test_loop_tres_voltas(self):
        assert forca("abcdefg123") == "media"  # 3 dígitos = 3 pontos
        assert forca("abcdefg1@@") == "forte"  # 1 dígito + 2 símbolos = 5 pontos
        assert forca("abcdefg@@@") == "forte"  # 3 símbolos = 6 pontos
    
    def test_loop_quatro_voltas_ponto_critico(self):
        assert forca("abcdefg1234") == "forte"   # 4 dígitos = 4 pontos (FORTE!)
        assert forca("abcdefg@@@@") == "forte"   # 4 símbolos = 8 pontos
        assert forca("abcdefg1abc") == "media"   # 1 dígito + letras = 1 ponto
    
    def test_loop_multiplas_voltas(self):
        assert forca("a1b2c3d4e5") == "forte"   # 10 voltas, 5 dígitos = 5 pontos
    
    def test_loop_voltas_sem_pontos(self):
        assert forca("aaaaaaaaaa") == "media"     # 10 voltas, apenas letras = 0 pontos
        assert forca("aaaaaaaaaaaaaaaaaaaa") == "media"  # 20 voltas
    
    def test_loop_acumulacao_pontos(self):
        assert forca("abcdefg1") == "media"      # 1 volta: 1 ponto
        assert forca("abcdefg12") == "media"     # 2 voltas: 2 pontos
        assert forca("abcdefg123") == "media"    # 3 voltas: 3 pontos
        assert forca("abcdefg1234") == "forte"   # 4 voltas: 4 pontos ✓
    
    def test_loop_comportamento_elif(self):
        assert forca("abcdefg1@") == "media"     # 1+2 = 3 pontos
        assert forca("abcdefg1@@") == "forte"    # 1+4 = 5 pontos
