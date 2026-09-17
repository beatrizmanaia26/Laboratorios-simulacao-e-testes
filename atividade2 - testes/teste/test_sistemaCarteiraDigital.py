from traceback import StackSummary
import pytest
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'funcional'))

from sistemaCarteiraDigital import CarteiraDigital, classificar_transacao, transferir, SaldoInsuficienteError


#fixture ex 1 e 2
@pytest.fixture
def carteira_inicial():
    return CarteiraDigital(10)


#fixture especifica para ex 3
@pytest.fixture
def carteira_com_log():
    # setup: antes do teste, apague o arquivo se ele ja existir
    log_path = " carteira .log "
    arquivo = Path(log_path)
    if arquivo.is_file():
        arquivo.unlink()
        print(f"\nSETUP Arquivo {log_path} deletado (existia antes)")
    
    carteira = CarteiraDigital(10, log_path)
    print(f"\nSETUP CarteiraDial criada com log_path: {log_path}")
    
    yield carteira
    
    # teardown: depois do teste, apague o arquivo criado pelo teste, mesmo se o teste falhar
    if arquivo.is_file():
        arquivo.unlink()
        print(f"\nTEARDOWN Arquivo {log_path} deletado com sucesso")
    else:
        print(f"\nTEARDOWN Arquivo {log_path} nao existe (nao precisou deletar)")


'''EXE1'''

# Saldo Inicial
def test_carteira_digital_saldo_inicial():
    # Arrange
    saldo_esperado = 10
    # Act
    carteira = CarteiraDigital(10)
    # Assert
    assert carteira.saldo == saldo_esperado


# Deposito
def test_carteira_digital_deposito_saldo(carteira_inicial):
    # Arrange
    valor_deposito = 2
    saldo_esperado = 12
    # Act
    carteira_inicial.depositar(valor_deposito)
    # Assert
    assert carteira_inicial.saldo == saldo_esperado


# Saque Dentro do Saldo
def test_carteira_digital_saque_saldo_positivo(carteira_inicial):
    # Arrange
    valor_saque = 5
    saldo_esperado = 5
    # Act
    carteira_inicial.sacar(valor_saque)
    # Assert
    assert carteira_inicial.saldo == saldo_esperado


# Saldo Inicial Padrao
def test_carteira_digital_saldo_inicial_padrao():
    # Arrange
    saldo_esperado = 0
    # Act
    carteira = CarteiraDigital()
    # Assert
    assert carteira.saldo == saldo_esperado


'''EX2'''
def test_saldo_insuficiente_erro_saldo_nao_muda():
    # Arrange
    saldo_inicial = 10
    saldo_esperado = 10
    erro_esperado = "saldo insuficiente"
    # Act
    carteira = CarteiraDigital(saldo_inicial)
    # Assert
    with pytest.raises(SaldoInsuficienteError, match=erro_esperado):
        carteira.sacar(20)
    assert carteira.saldo == saldo_esperado


def test_saldo_insuficiente_erro_tipo_mensagem():
    # Arrange
    saldo_esperado = 20
    erro_esperado = "saldo insuficiente"
    # Act
    carteira = CarteiraDigital()
    # Assert
    with pytest.raises(#ao inves de raise valueError direto, criei a class SaldoInsuficienteError
        SaldoInsuficienteError, match=erro_esperado
    ):
        carteira.sacar(saldo_esperado)  

'''EX3'''

def test_verifica_log_apos_deposito(carteira_com_log):
    # Arrange
    valor_deposito = 10
    log_path = " carteira .log "
    # Act
    carteira_com_log.depositar(valor_deposito)
    # Assert
    arquivo = Path(log_path)
    assert arquivo.is_file(), "Arquivo de log nao foi criado"
    
    conteudo = arquivo.read_text()
    print(f"\nConteudo do log: {repr(conteudo)}")
    assert f" deposito :{ valor_deposito }" in conteudo, "Deposito nao foi registrado no log"


'''EX4'''
@pytest.mark.parametrize("transacao,esperado", [
    (100, "media"),      
    (20, "pequena"),    
    (500, "media"),  
    (650, "media"),   
    (700, "media"),  
    (1000, "grande"),  
])
def test_validar_transacao_parametrizado(transacao, esperado):
    # Arrange
    valor_transacao = transacao
    resultado_esperado = esperado
    # Act
    resultado = classificar_transacao(valor_transacao)
    # Assert
    assert resultado == resultado_esperado


'''EX5 - Suite Completa de Transferencia'''

# Fixture A: duas carteiras (origem com saldo, destino vazia)
@pytest.fixture
def carteiras_para_transferencia():
    # Arrange: criar carteiras
    carteira_origem = CarteiraDigital(100)  # Com saldo inicial de 100
    carteira_destino = CarteiraDigital(0)   # Vazia
    
    yield carteira_origem, carteira_destino
    
    # Cleanup: apagar logs se existirem
    log_path = " carteira .log "
    arquivo = Path(log_path)
    if arquivo.is_file():
        arquivo.unlink()


# Teste B: Transferencia bem-sucedida (parametrizado com ids)
@pytest.mark.parametrize("valor_transferencia,saldo_origem_esperado,saldo_destino_esperado", [
    (10, 90, 10),
    (50, 50, 50),
    (100, 0, 100),
], ids=["pequena_transferencia", "media_transferencia", "transferencia_total"])
def test_transferencia_bem_sucedida(carteiras_para_transferencia, valor_transferencia, saldo_origem_esperado, saldo_destino_esperado):
    # Arrange
    carteira_origem, carteira_destino = carteiras_para_transferencia
    
    # Act
    transferir(carteira_origem, carteira_destino, valor_transferencia)
    
    # Assert
    assert carteira_origem.saldo == saldo_origem_esperado, f"Saldo origem esperado {saldo_origem_esperado}, mas foi {carteira_origem.saldo}"
    assert carteira_destino.saldo == saldo_destino_esperado, f"Saldo destino esperado {saldo_destino_esperado}, mas foi {carteira_destino.saldo}"


# Teste C: Transferencia com saldo insuficiente (nenhuma carteira muda)
def test_transferencia_saldo_insuficiente_nao_muda(carteiras_para_transferencia):
    # Arrange
    carteira_origem, carteira_destino = carteiras_para_transferencia
    saldo_origem_inicial = carteira_origem.saldo  # 100
    saldo_destino_inicial = carteira_destino.saldo  # 0
    valor_transferencia = 150  # maior que o saldo disponivel
    
    # Act & Assert
    with pytest.raises(SaldoInsuficienteError, match="saldo insuficiente"):
        transferir(carteira_origem, carteira_destino, valor_transferencia)
    
    # verificar que os saldos nao mudaram
    assert carteira_origem.saldo == saldo_origem_inicial, f"Saldo origem mudou! Era {saldo_origem_inicial}, agora e {carteira_origem.saldo}"
    assert carteira_destino.saldo == saldo_destino_inicial, f"Saldo destino mudou! Era {saldo_destino_inicial}, agora e {carteira_destino.saldo}"
