def confirmar(pedido, centavos, gateway, email, tentativas=3):
    if tentativas < 1:
        raise ValueError("tentativas deve ser >= 1")

    for _ in range(tentativas - 1):
        try:
            status = gateway.cobrar(pedido, centavos)
            break
        except ConnectionError:
            pass
    else:
        try:
            status = gateway.cobrar(pedido, centavos)
        except ConnectionError:
            email.enviar(pedido, "falha na cobranca")
            raise

    if status == "aprovado":
        email.enviar(pedido, "pedido confirmado")

    return status
