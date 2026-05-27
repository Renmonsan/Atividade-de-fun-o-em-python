def jursimp(c:float,i:float,t:int):
    '''
    Função que calcula juros simples(utilizei a divisão por 100 para não ter que digitar a forma decimal da porcentagem)'''
    m = ((c*(i*t))/100)+c
    return m

def jurcomp(c:float,i:float,t:int):
    '''Função que calcula juros compostos'''
    m = (c*(1 + (i/100))**t)
    return m
def desconto(vi:float,d:float):
        '''Função que calculo desconto em um produto'''
        Valor = vi * (1-d/100)
        return Valor

def aumento(vi:float,d:float):
        '''Função que calcula um aumento de valor em percentual'''
        Valor = vi * (1+d/100)
        return Valor

def financ(v:float,n:int):
      '''Função que calculo o valor de uma parcela em um financiamento'''
      p = v/n
      return p
