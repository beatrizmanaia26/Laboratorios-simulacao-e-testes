def forca(senha):
    if len(senha) < 8:
        return "fraca"
    pontos = 0
    for c in senha:
        if c.isdigit():
            pontos += 1
        elif not c.isalnum():
          pontos += 2
    if pontos >= 4:
        return "forte"
    return "media"


'''
EXERCICIO 1

cada linha de codigo é um vertice 
é losango se for condicuao (if,for) é ciruclo se for outra coisa
seta tem "v" pq é verdadeiro

-linha 2 é onde coemca codigo e é if, é losango 2, seta com nome v pq se for verdade, retorna 3 (retorno é circulo)
-linha 2 pode leva pra linha 4, circulo 

A)
-calcule GFC: imagemgfcEX1A.jpeg
-calcule V(G):
  -fórmula1:E-N+2. (e=arestas,n=nos)
            16-12+2=6
  -fórmula2:P+1.  (p=nos de decisao com 2 ramos)
           5+1=6 (nos 2,5,10,6,8)


B)
-resolução no 1B.jpeg
-6 caminhos linearmente independentes 
-testar 6 caminhos que sai do inicio (que é 2) e levam p f
-pega caminhos e inverte condicionais e considera novo caminho sempre que adiciona um vertice novo ao caminho é linear independente:


-caminho1: (2,3),(3,f) -> 2,3,f -->resultado: senha <8 espero q retorne fraca
-caminho2: (2,4),(4,5),(5,10),(10,12),(12,f) -> 2,4,5,10,12,f  -->resultado: retorne média 
(caminho2 5,10 é caminho falso, ai mudo a condicional ao inves de pega f pego v.
so vai ter 6 caminho com aresta qnnc foi considerada)
-caminho3: (2,4),(4,5),(5,6),(6,7),(7,5),(5,10),(10,12),(12,f) ->2,4,5,6,7,5,10,12,f  (tanto faz ser 10,11 ou 10,12, contanto que 11 e 12 aparecam em algum caminho)-->resultado return media 
-caminho4: 2,4,5,10,11,f --> resultado return forte
-caminho5: 2,4,5,6,8,5,10,11,f --> resultado return forte
-caminho6: 2,4,5,6,8,9,5,12,f --> resultado media 

CAMINHO TIPOCO: 2,3,f 
2,4,5,10,12,F. ->peguei f do 5 pro 10 ai pego v do 5 pro 6(inverte condicionais)

fazer caminhos e ve resultado esperado olhando pro codigo 


Acho que nenhum caminho é inviavel...



C) TESTE COM PARAMETRIZE E COBERTURA:
Resultado: 25 testes implementados, TODOS COM 100% DE COBERTURA!
- Cobertura: 100% (13 linhas de código, 10 branches)
- Testes que deram 100% de ramos: 25/25 
- V(G) = 6, Testes implementados = 25 (significativamente maior que V(G))
- Cada teste foi mapeado para cobrir os 6 caminhos independentes
- Arquivo de testes: test_senha.py com @pytest.mark.parametrize


D)  test_loop_testing.py, Teste de laço for c in senha (linha 5):

Quantas voltas possiveis?
-Mínimo: 0 voltas (quando len(senha) < 8, a função retorna antes do laço)
-Máximo: INFINITO (não há limite de tamanho de senha definido no código)
-Prático: Depende do tamanho da senha após validação inicial

CATEGORIAS DE VOLTAS TESTADAS:
-0 voltas: Laço não executa (senha < 8 caracteres) - retorna "fraca"
-1 volta: Laço executa 1 vez (len=8) - processa 1 caractere
-2 voltas: Laço executa 2 vezes (len=9) - processa 2 caracteres
-3 voltas: Laço executa 3 vezes (len=10) - processa 3 caracteres
-4 voltas: CRÍTICO! (len=11) - aqui pontos pode atingir >= 4 (retorna "forte")
-N voltas: Múltiplas voltas (len > 11) - laço continua processando


CASOS DE LAÇO QUE FAZEM SENTIDO:
1. Zero voltas: Validação (senha muito curta)
2. Uma volta: Teste mínimo de processamento
3. Duas voltas: Teste com dois caracteres
4. Três voltas: Teste com três caracteres
5. Quatro voltas: CRÍTICO - primeiro ponto onde pode retornar "forte"
6. Múltiplas voltas: Teste de robustez com senhas longas
7. Acumulação de pontos: Verificar cálculo progressivo

'''