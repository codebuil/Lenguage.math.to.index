import re

def expressao_para_processos(expressao, funcoes_permitidas):
    # Dividir a expressão em tokens
    tokens = re.findall(r'[\d]+|[a-z,\(\d\)]+|[\+\-\*\\]', expressao)

    # Mapear operadores matemáticos para operadores de processos
    operadores = {
        '+': 'ADD',
        '-': 'SUB',
        '*': 'MUL',
        '/': 'DIV'
    }

    processo = []
    processo_variavel = 1

    for token in tokens:
        if token.isdigit():
            # Se o token for um número, crie uma variável temporária
            if processo_variavel == 1:
                processo.append(f'var{processo_variavel}={token}\r\n')
            else:
                processo.append(f',{token}\r\n')
            processo_variavel += 1
        elif token in operadores:
            # Se o token for um operador matemático, converta-o para um operador de processo
            operador_processo = operadores[token]
            args = [f'var{i}' for i in range(processo_variavel - 2, processo_variavel)]
            processo.append(f'{operador_processo},{",".join(args)}')
        elif token[0].isdigit()==False:
            # Se o token for uma chamada de função
            processo.append(f',{token}\r\n')
        

    return ''.join(processo)

def main():
    funcoes_permitidas = ["funcs"]  # Adicione as funções permitidas aqui
    expressao = input("Digite uma expressão com funções: ")
    processo = expressao_para_processos(expressao, funcoes_permitidas)
    
    if processo is not None:
        print("Expressão convertida em processos:")
        print(processo)

print("\x1bc\x1b[44;37m")
main()

