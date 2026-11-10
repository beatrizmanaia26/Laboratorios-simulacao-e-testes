"""
Por que, aqui, conferir as chamadas não é excesso?

confirmar() não devolve o efeito da cobrança nem o conteúdo do e-mail.
O retorno é só o status ("aprovado" ou "negado"). Os efeitos que importam
(quantas vezes o cliente foi cobrado, com quais valores, e qual mensagem
foi enviada) só existem como chamadas feitas a gateway e email.

Se a asserção olhasse apenas o retorno, um código errado passaria:
- cobrar duas vezes num aprovado de primeira (retorno continua "aprovado");
- enviar "pedido confirmado" para um pedido negado (retorno continua "negado");
- cobrar com o centavos trocado (retorno pode continuar igual);
- não enviar "falha na cobranca" quando a última tentativa falha.

Com Mock, conferimos cobranças (call_count), argumentos (assert_called_with)
e e-mails (assert_called_once_with / assert_not_called). Isso fecha os
caminhos que o retorno não mostra.
"""


from unittest.mock import Mock

import pytest

from confirmacao import confirmar


def test_aprovado_cobra_uma_vez_e_envia_confirmacao():
    gateway = Mock()
    gateway.cobrar.return_value = "aprovado"
    email = Mock()

    status = confirmar("pedido-1", 1500, gateway, email)

    assert status == "aprovado"
    gateway.cobrar.assert_called_once_with("pedido-1", 1500)
    email.enviar.assert_called_once_with("pedido-1", "pedido confirmado")


def test_negado_devolve_negado_e_nao_envia_email():
    gateway = Mock()
    gateway.cobrar.return_value = "negado"
    email = Mock()

    status = confirmar("pedido-2", 900, gateway, email)

    assert status == "negado"
    gateway.cobrar.assert_called_once_with("pedido-2", 900)
    email.enviar.assert_not_called()


def test_connection_error_depois_sucesso_recobra_e_confirma():
    gateway = Mock()
    gateway.cobrar.side_effect = [ConnectionError(), "aprovado"]
    email = Mock()

    status = confirmar("pedido-3", 2000, gateway, email)

    assert status == "aprovado"
    assert gateway.cobrar.call_count == 2
    gateway.cobrar.assert_called_with("pedido-3", 2000)
    email.enviar.assert_called_once_with("pedido-3", "pedido confirmado")


def test_todas_tentativas_falham_envia_falha_e_relanca_excecao():
    gateway = Mock()
    gateway.cobrar.side_effect = ConnectionError()
    email = Mock()

    with pytest.raises(ConnectionError):
        confirmar("pedido-4", 700, gateway, email)

    assert gateway.cobrar.call_count == 3
    email.enviar.assert_called_once_with("pedido-4", "falha na cobranca")


def test_tentativas_padrao_e_3():
    gateway = Mock()
    gateway.cobrar.side_effect = ConnectionError()
    email = Mock()

    with pytest.raises(ConnectionError):
        confirmar("pedido-5", 100, gateway, email)

    assert gateway.cobrar.call_count == 3


def test_tentativas_customizadas_limitam_o_numero_de_cobrancas():
    gateway = Mock()
    gateway.cobrar.side_effect = ConnectionError()
    email = Mock()

    with pytest.raises(ConnectionError):
        confirmar("pedido-6", 100, gateway, email, tentativas=5)

    assert gateway.cobrar.call_count == 5


def test_tentativas_menor_que_1_lanca_erro():
    gateway = Mock()
    email = Mock()

    with pytest.raises(ValueError):
        confirmar("pedido-7", 100, gateway, email, tentativas=0)

    gateway.cobrar.assert_not_called()
    email.enviar.assert_not_called()
