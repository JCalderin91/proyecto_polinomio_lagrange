#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""


def li(x, i):
  def _(var):
    acum = 1
    for j in range(len(x)):
      if(i != j):
        acum *= (var-x[j])/(x[i]-x[j])
    return acum
  return _

def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)

    def polinomio(var):
        acum = 0
        for j in range(len(x)):
            acum += y[j] * li(x, j)(var)
        return acum
    return polinomio


if __name__ == '__main__':
    
    x = [-5,0,3,8,10]
    y = [-4,-2,5,12,18]

    l = polinomio_lagrange(x, y)

    #evaluar el polinomio resultante en un rango de valores
    for i in x:
        print(l(i))
