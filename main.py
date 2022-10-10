from codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '27/10/1987', 3000)
    print(f'Teste = {funcionario_teste.idade()}')
    
    funcionario_teste01 = Funcionario('Teste1', '30/09/1972', 5000)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()