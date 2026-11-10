"""
Suíte de contrato do repositório de usuários.

A mesma suíte roda nas três implementações (fixture parametrizada):
- RepoSqlite: implementação real, em memória.
- FakeIngenuo: dicionário simples. Espera-se que FALHE em parte dos testes.
- FakeFiel: respeita o contrato. Deve passar em todos.

Interpretação das falhas do FakeIngenuo:
- Não normaliza maiúsculas/minúsculas: "Ana@x.com" e "ana@x.com" viram
  duas chaves diferentes, então a busca e a checagem de duplicidade falham.
- Não levanta EmailDuplicado: salvar de novo sobrescreve o nome existente.
- Buscar um e-mail não cadastrado devolve None (dict.get), então esse
  teste passa. Um teste verde não prova que o contrato inteiro é cumprido.

Efeito nos testes de unidade que usassem o FakeIngenuo: eles passariam
mesmo com o contrato violado. Um serviço que depende do repositório
continuaria verde enquanto, em produção, o cadastro duplicado sobrescreveria
dados e a busca falharia com maiúsculas. O double repete uma suposição sobre
a dependência; se a suposição estiver errada, o teste de unidade não percebe.
Por isso o FakeFiel precisa ser validado pela mesma suíte do RepoSqlite.
"""

import pytest

from repo_usuarios import EmailDuplicado, FakeFiel, FakeIngenuo, RepoSqlite


@pytest.fixture(
    params=[RepoSqlite, FakeIngenuo, FakeFiel],
    ids=["sqlite", "ingenuo", "fiel"],
)
def repo(request):
    return request.param()


def test_salvar_e_buscar_devolve_o_nome(repo):
    repo.salvar("ana@exemplo.com", "Ana")
    assert repo.buscar("ana@exemplo.com") == "Ana"


def test_buscar_nao_cadastrado_devolve_none(repo):
    assert repo.buscar("ninguem@exemplo.com") is None


def test_salvar_email_duplicado_levanta_erro(repo):
    repo.salvar("ana@exemplo.com", "Ana")
    with pytest.raises(EmailDuplicado):
        repo.salvar("ana@exemplo.com", "Ana Outra")


def test_duplicado_nao_sobrescreve_o_nome_original(repo):
    repo.salvar("ana@exemplo.com", "Ana")
    with pytest.raises(EmailDuplicado):
        repo.salvar("ana@exemplo.com", "Ana Outra")
    assert repo.buscar("ana@exemplo.com") == "Ana"


def test_busca_ignora_maiusculas_e_minusculas(repo):
    repo.salvar("ana@exemplo.com", "Ana")
    assert repo.buscar("ANA@Exemplo.COM") == "Ana"


def test_salvar_duplicado_ignora_maiusculas_e_minusculas(repo):
    repo.salvar("ana@exemplo.com", "Ana")
    with pytest.raises(EmailDuplicado):
        repo.salvar("Ana@EXEMPLO.com", "Ana Outra")
