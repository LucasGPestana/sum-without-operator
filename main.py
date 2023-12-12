"""
Copyright (c) 2019 Prabhu Pant

Permission is hereby granted, free of charge, to any person obtaining a copy
...
"""

from itertools import batched
import random

# batched é compatível com o python 3.12

def getSum(a, b):

    """
    :type a: int
    :type b: int
    :rtype: int
    """

    mask = 0xffffffff

    # Serve para pegar a soma binária entre os números, sem considerar os carries
    diff = 0

    '''
    Serve para pegar os "uns" resultantes da soma entre bits 1 e 1
    
    É semelhante a soma tradicional da matemática, no qual quando a soma de dois
    números resulta em um número de dois algarismos, passamos o segundo algarismo
    do valor resultante para a próxima casa a esquerda da soma
    '''
    carry = 0

    # Itera até que o carry (atribuído em "b") contenha apenas bits 0
    while b & mask:

        diff = a ^ b # Operação bitwise XOR
        
        carry = a & b # Operação bitwise AND
        carry = carry << 1 # Deslocamento a esquerda (adiciona um zero a direita)
        
        a = diff
        b = carry

    return a

if __name__ == "__main__":

    # Teste com valores aleatórios agrupados

    randnumbers = random.sample(range(0, 1000), 50)
    numbersgrouped = batched(randnumbers, 2)

    for group in numbersgrouped:

        print(f"Agrupamento: {group}")
        print(f"Soma entre os números: {getSum(*group)}")
