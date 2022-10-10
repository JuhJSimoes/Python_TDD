import unittest
import pytest
from pytest import mark
import sys
sys.path.append('.')

from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_27_10_1987_deve_rertornar_35(self):
        
        entrada = '27/10/1987' #Given-Contexto
        esperado = 35
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When-ação
        
        assert resultado == esperado #Then-desfecho
    
    
    def test_quando_sobrenome_recebe_Juliana_Simoes_deve_retornar_apenas_Simoes(self):
        entrada = ' Juliana Simoes ' #Given
        esperado = 'Simoes'
        
        juliana = Funcionario(entrada, '27/10/1987', 1111)
        resultado = juliana.sobrenome() #When
        
        assert resultado == esperado #Then
    
    
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
                
        
        funcionario_teste = Funcionario(entrada_nome, '27/10/1987', entrada_salario)
        funcionario_teste.decrescimo_salario() #Then
        resultado = funcionario_teste.salario
        
        assert resultado == esperado #Then
        
    @mark.calcular_bonus    
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 #Given
        esperado = 100
                
        funcionario_teste = Funcionario('teste', '27/10/1987', entrada)
        resultado = funcionario_teste.calcular_bonus()#When
        
        assert resultado == esperado #Then
    
    @mark.calcular_bonus  
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
         with pytest.raises(Exception):  
            entrada = 1000000 #Given
                
            funcionario_teste = Funcionario('teste', '27/10/1987', entrada)
            resultado = funcionario_teste.calcular_bonus()#When
            
            assert resultado #Then
            
   
            
            
#https://docs.pytest.org/en/7.1.x/reference/reference.html#ini-options-ref
#https://www.alura.com.br/artigos/ambientes-virtuais-em-python
#pytest --cov tests/ --cov-report term-missing
#pytest --cov tests/