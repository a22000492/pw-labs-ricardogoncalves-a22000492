def count_children(dictionary):
  print(f"Existem {len(dictionary)} crianças")

def count_toys(dictionary):
  for child in dictionary:
    print(f"{child}: {len(dictionary[child])} brinquedos")

def count_total_toys(dictionary):
  soma = 0
  for child in dictionary:
    soma += len(dictionary[child])
  print(f"Existem {soma} brinquedos")


def toy_exists(dictionary, toy):
  soma = 0
  for child in dictionary:
    if toy in dictionary[child]:
      return True
  return False



