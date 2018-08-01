#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest

def testa_leitura(texto):
    print(texto)
    return 'Babaca'

def ler_frase(ler=input):
    '''

    >>> teste = 'a'
    >>> print(teste)
    a
    >>> print(ler_frase(testa_leitura))
    Escrever a frase:
    Babaca
    '''
    recebe_frase = ler('Escrever a frase: ')
    return recebe_frase


class TestaTeclado(unittest.TestCase):
    def testa_frase_a(self):
        self.assertEqual(teclas('a'), '2')
        self.assertEqual(teclas('A'), '2')

    def testa_frase_b(self):
        self.assertEqual(teclas('b'), '22')
        self.assertEqual(teclas('B'), '22')

    def testa_frase_c(self):
        self.assertEqual(teclas('c'), '222')
        self.assertEqual(teclas('C'), '222')

    def testa_frase_d(self):
        self.assertEqual(teclas('d'), '3')
        self.assertEqual(teclas('D'), '3')

    def testa_frase_f(self):
        self.assertEqual(teclas('f'), '333')
        self.assertEqual(teclas('F'), '333')

    def testa_duas_letras(self):
        self.assertEqual(teclas('Da'), '32')

    def testa_frase_ce(self):
        self.assertEqual(teclas('ce'), '22233')

    def testa_ler(self):
        self.assertEqual(teclas(ler_frase(testa_leitura)), '2222222222')

def teclas(frase):
    retorno = []
    dicio = {
        'A': '2',
        'B': '22',
        'C': '222',
        'D': '3',
        'E': '33',
        'F': '333'
    }

    frase_maiuscula = frase.upper()

    for letra in frase_maiuscula:
        retorno.append(dicio.get(letra, ''))

    return ''.join(retorno)


if __name__ == '__main__':
    recebe_frase = ler_frase()
    print(teclas(recebe_frase))

