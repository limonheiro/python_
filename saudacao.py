def saudacao(nome):
    if nome:
        return f'Olá, {nome.capitalize()}. Bem-vindo.'
    return 'Erro: nome vazio.'

nome = input("digite seu nome: ")
print(saudacao(nome))
