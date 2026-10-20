import sys
sys.path.insert(0, '/Users/beatrizmanaia/Desktop/FEI 8S/Laboratorios-simulacao-e-testes/atividade5 - testes')

from preco import preco_final


#Linha 5: total = total - desconto  (ao invés de: total * 0.8 - desconto)

testes = [
    {"entrada": (60, True), "esperado": 48, "descricao": "(2, 5): preco com VIP, total < 50"},
    {"entrada": (200, False), "esperado": 200, "descricao": "(2, 6): preco sem VIP, total >= 50"},
    {"entrada": (100, False), "esperado": 100, "descricao": "(2, 8): preco sem VIP, retorna direto"},
    {"entrada": (60, True), "esperado": 48, "descricao": "(4, 5): desconto aplicado em L5"},
    {"entrada": (30, True), "esperado": 50, "descricao": "(5, 6): L5 define, L6 verifica < 50"},
    
    # (5, 8) - L5 define, L8 usa (vip=True, total >= 50) **ANTES FALTAVA**
    {"entrada": (300, True), "esperado": 240, "descricao": "(5, 8): L5 define, L8 retorna (NOVO!)"},
    
    # (7, 8) - L7 define, L8 usa (total < 50)
    {"entrada": (40, False), "esperado": 50, "descricao": "(7, 8): L7 define min 50, L8 retorna"},
]

todos_passaram = True
for i, teste in enumerate(testes, 1):
    entrada = teste["entrada"]
    esperado = teste["esperado"]
    descricao = teste["descricao"]
    
    resultado = preco_final(*entrada)
    passou = resultado == esperado
    todos_passaram = todos_passaram and passou
    
    status = "✓ PASSOU" if passou else "✗ FALHOU"
    print(f"\nTeste {i}: {status}")
    print(f"  Descrição: {descricao}")
    print(f"  Entrada: preco_final{entrada}")
    print(f"  Esperado: {esperado}")
    print(f"  Obtido: {resultado}")


if todos_passaram:
    print("TODOS OS TESTES PASSARAM!")

else:
    print("ALGUNS TESTES FALHARAM")
 