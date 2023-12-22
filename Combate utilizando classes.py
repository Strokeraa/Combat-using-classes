class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque indefinido"

        mensagem = f"o {self.tipo} atacou usando {ataque}"
        print(mensagem)


# Exemplo de uso
heroi1 = Heroi("Aragorn", 30, "ninja")
heroi1.atacar()

heroi2 = Heroi("Gandalf", 150, "monge")
heroi2.atacar()
