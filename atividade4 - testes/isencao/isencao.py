def isento(pcd, valor_compra, cadastro_app, minutos):
    if pcd:
        return True
    
    if (valor_compra >= 150 or cadastro_app) and minutos <= 240:
        return True
    
    return False