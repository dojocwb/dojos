#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest

import pizza

class PizzaTest(unittest.TestCase):
    def test_luca_deve_ser_renato(self):
        self.assertEqual(pizza.compatibilidade('Luca'), 'Renato')

    def test_lenon_deve_ser_renata(self):
        self.assertEqual(pizza.compatibilidade('Lenon'), 'Renata')

    def testa_distancia_simples(self):
        self.assertEqual(pizza.distancia({"Marguerita":5}, {"Marguerita":5}),0)   

    def testa_distancia_calculada(self):
        self.assertEqual(pizza.distancia({"Marguerita":1}, {"Marguerita":2}),1)  
    
    def testa_distancia_calculada_invertida(self):
        self.assertEqual(pizza.distancia({"Marguerita":2}, {"Marguerita":1}),1)    

    def testa_distancia_calculada_invertida(self): 
        sabores={"Marguerita":2, "Napolitana":1,} 
        self.assertEqual(pizza.distancia(sabores, sabores), 0)

if __name__ == '__main__':
    unittest.main()
