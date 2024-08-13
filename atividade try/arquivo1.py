from datetime import datetime
def calcular_idade():
    try:
        ano_nascimento = input("Digite o ano de nascimento: ")
        if not ano_nascimento.isdigit():
            raise ValueError("Entrada não numérica")
        ano_nascimento = int(ano_nascimento)
        ano_atual = datetime.now().year
        if ano_nascimento > ano_atual:
            raise ValueError("Ano de nascimento no futuro")
        if ano_nascimento < 1900:
            raise ValueError("Ano de nascimento muito precoce")
        idade = ano_atual - ano_nascimento
        print(f"Sua idade é: {idade} anos")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira um ano de nascimento válido.")
calcular_idade()
