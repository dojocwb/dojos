#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from conversor import Conversor

class TestCheque(unittest.TestCase):
    def test_um(self):
        self.assertEqual(Conversor().bla('um'), 1)
    def test_dois(self):
        self.assertEqual(Conversor().bla('dois'), 2)
    def test_tres(self):
        self.assertEqual(Conversor().bla('três'), 3)
    def test_quatro(self):
        self.assertEqual(Conversor().bla('quatro'), 4)
    def test_cinco(self):
        self.assertEqual(Conversor().bla('cinco'), 5)
    def test_vinte(self):
        self.assertEqual(Conversor().bla('vinte'), 20)
    def test_doze(self):
        self.assertEqual(Conversor().bla('doze'), 12)    
    def test_cem(self):
        self.assertEqual(Conversor().bla('cem'), 100)
    def test_mil(self):
        self.assertEqual(Conversor().bla('mil'), 1000)
    def test_cento(self):
        self.assertEqual(Conversor().bla('cento'), 100)
    def test_centoequinze(self):
        self.assertEqual(Conversor().bla('cento e quinze'), 115)
    def test_centoedez(self):
        self.assertEqual(Conversor().bla('cento e dez'), 110)
    def test_virgula(self):
        self.assertEqual(Conversor().bla('cento e dez e quinze centavos'), 110.15)
    

if __name__ == '__main__':
    unittest.main()
