class AssistenteVirtual:
    def _init_(self):
        # Dicionário para armazenar as funções do assistente
        self.funcoes = {}

    def adicionar_funcao(self, nome, funcao):
        """
        Adiciona uma nova função ao assistente.

        :param nome: Nome da função (string)
        :param funcao: Função executável
        """
        self.funcoes[nome] = funcao
        print(f"Função '{nome}' adicionada com sucesso.")

    def executar_funcao(self, nome, *args, **kwargs):
        """
        Executa uma função registrada no assistente.

        :param nome: Nome da função a ser executada (string)
        :param args: Argumentos posicionais da função
        :param kwargs: Argumentos nomeados da função
        """
        if nome in self.funcoes:
            try:
                return self.funcoes[nome](*args, **kwargs)
            except Exception as e:
                print(f"Erro ao executar a função '{nome}': {e}")
        else:
            print(f"Função '{nome}' não encontrada. Use 'listar_funcoes' para verificar as disponíveis.")

    def listar_funcoes(self):
        """Lista todas as funções disponíveis no assistente."""
        if self.funcoes:
            print("Funções disponíveis:")
            for nome in self.funcoes:
                print(f"- {nome}")
        else:
            print("Nenhuma função cadastrada.")


# Exemplos de funções para o assistente
def saudacao(nome):
    return f"Olá, {nome}! Como posso ajudar você hoje?"

def calculadora(a, b, operacao):
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    elif operacao == "divisao":
        return a / b if b != 0 else "Erro: divisão por zero"
    else:
        return "Operação inválida. Escolha entre soma, subtracao, multiplicacao ou divisao."

# Instanciando o assistente
assistente = AssistenteVirtual()

# Adicionando funções
assistente.adicionar_funcao("saudacao", saudacao)
assistente.adicionar_funcao("calculadora", calculadora)

# Testando o assistente
assistente.listar_funcoes()
print(assistente.executar_funcao("saudacao", "Carlos"))
print(assistente.executar_funcao("calculadora", 10, 5, "soma"))
print(assistente.executar_funcao("calculadora", 10, 0, "divisao"))