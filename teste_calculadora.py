import unittest
from calculadora import Calculadora

class CalculadoraTeste(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def testeSomar(self):
        resultado = self.calculadora.soma(3, 3)
        self.assertEqual(resultado, 6)

    def testeSubtrair(self):
        resultado = self.calculadora.subtracao(5, 2)
        self.assertEqual(resultado, 3)

    def testeDividir(self):
        resultado = self.calculadora.divisao(10, 2)
        self.assertEqual(resultado, 5)

    def testeMultiplicar(self):
        resultado = self.calculadora.multiplicacao(7, 1)
        self.assertEqual(resultado, 7)

if __name__ == '__main__':
    unittest.main()
