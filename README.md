# Projeto Calculadora - Testes de Unidade e Integração

## Como executar 
1. Instalar dependências: 
   - pip install -r requirements.txt 

2. Executar todos os testes: 
   - python -m unittest discover tests -v 

3. Executar cobertura:
   - coverage run -m unittest discover tests 
   - coverage report 
   - coverage html 

4. Executar teste específico: 
   - python-m unittest tests.test_unidade.TestCalculadora.test_soma-v  
