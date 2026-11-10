import sqlite3


class EmailDuplicado(Exception):
    pass


class RepoSqlite:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            "CREATE TABLE usuarios (email TEXT PRIMARY KEY, nome TEXT NOT NULL)"
        )

    def salvar(self, email, nome):
        try:
            self.conn.execute(
                "INSERT INTO usuarios (email, nome) VALUES (?, ?)",
                (email.lower(), nome),
            )
        except sqlite3.IntegrityError:
            raise EmailDuplicado(email)
        self.conn.commit()

    def buscar(self, email):
        linha = self.conn.execute(
            "SELECT nome FROM usuarios WHERE email = ?", (email.lower(),)
        ).fetchone()
        return linha[0] if linha else None


class FakeIngenuo:
    def __init__(self):
        self.usuarios = {}

    def salvar(self, email, nome):
        self.usuarios[email] = nome

    def buscar(self, email):
        return self.usuarios.get(email)


class FakeFiel:
    def __init__(self):
        self.usuarios = {}

    def salvar(self, email, nome):
        chave = email.lower()
        if chave in self.usuarios:
            raise EmailDuplicado(email)
        self.usuarios[chave] = nome

    def buscar(self, email):
        return self.usuarios.get(email.lower())
