def ler_numero():
  return input("Introduza um inteiro: ")

def imprime_resultados(n, positivo, par):
  print(f"Número {n}, {'positivo' if positivo else 'negativo'}, {'par' if par else 'ímpar'}")