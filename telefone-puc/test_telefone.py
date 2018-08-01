#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from telefone import Telefone
from telefone import ConverteError

class TestTelefone(unittest.TestCase):
    def setUp(self):
        self.telefone = Telefone()

    def tearDown(self):
        pass

    def test_classe_telefone_existe(self):
        self.assertTrue(self.telefone)

    def test_entrada_telefone(self):
        self.assertEqual(
            "ABC",
            self.telefone.ler_entrada("ABC")
        )

    def test_converte_letra_abc_retorna_2(self):
        self.assertEqual(
            '2',
            self.telefone.converte_letra("A")
        )

    def test_converte_letra_def_retorna_3(self):
        self.assertEqual(
            '3',
            self.telefone.converte_letra("D")
        )

    def test_converte_letra_ghi_retorna4(self):
        self.assertEqual(
            '4',
            self.telefone.converte_letra("G")
        )

    def test_converte_letra_jkl_retorna5(self):
        self.assertEqual(
            '5',
            self.telefone.converte_letra("J")
        )

    def test_converte_letra_mno_retorna6(self):
        self.assertEqual(
            '6',
            self.telefone.converte_letra("M")
        )

    def test_converte_letra_pqrs_retorna7(self):
        self.assertEqual(
            '7',
            self.telefone.converte_letra("P")
        )

    def test_converte_letra_tuv_retorna8(self):
        self.assertEqual(
            '8',
            self.telefone.converte_letra("T")
        )

    def test_converte_letra_wxyz_retorna9(self):
        self.assertEqual(
            '9',
            self.telefone.converte_letra("W")
        )

    def test_converte_letra_0_retorna0(self):
        self.assertEqual(
            '0',
            self.telefone.converte_letra("0")
        )

    def test_converte_tudo(self):
        self.assertEqual(
            '69-647372253-562',
            self.telefone.decriptografar("MY-MISERABLE-JOB")
        )

    def test_converte_numero(self):
        self.assertRaises(
            ConverteError,
            self.telefone.decriptografar,
            0
        )

if __name__ == '__main__':
    unittest.main()