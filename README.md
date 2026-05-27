# Atividade-de-fun-o-em-python
#Atividade proposta na disciplina de software básico.

## 1) Crie uma biblioteca chamada financeiro.py contendo funções para realizar os seguintes cálculos financeiros.

### a) Uma função que calcule e retorna o montante final utilizando juros simples. Onde: M (montante final), C (capital inicial), i (taxa de juros) e t (tempo). Fórmula: 𝑀 = 𝐶 ⋅ (1 + 𝑖 ⋅ 𝑡)
```bash
def jursimp(c:float,i:float,t:int):
    '''
    Função que calcula juros simples(utilizei a divisão por 100 para não ter que digitar a forma decimal da porcentagem)'''
    m = ((c*(i*t))/100)+c
    return m
```
