#ex2

def total_com_desconto(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
        return round(total, 2)

'''
Suíte inicial: um teste, assert total_com_desconto([10, 20, 30,
40, 50]) > 0.


Medir com pytest --cov-branch e com mutmut, para responder a) sobre cobertura e MS.


a)Meça a cobertura de ramos e o MS. O que os dois números dizem sobre
a suíte?

Cobertura de ramos: mostra quantos ramos o teste executa. Com o return no laço, o ramo do desconto e a saída normal do laço não rodam.

MS: mostra quantos mutantes o teste mata. Um `assert > 0` aceita quase qualquer valor positivo, então a maioria dos mutantes sobrevive.



b) Troque só o assert pelo valor exato, sem mudar a entrada. Quantos
vivos restam?


c)Para cada vivo que restou, diga qual condição falhou: alcançar, infectar,
propagar ou revelar



d)Acrescente as entradas que faltam até o MS chegar a 100%. Que tipo de
preço foi preciso?


'''