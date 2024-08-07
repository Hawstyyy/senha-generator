from funct import gerador

while True:
  try:
    choice = int(input("""
+------------------------+
|   1 - Gerar senha      |
|   2 - Sair             |
+------------------------+
  - """))
  except ValueError:
    print("\n- Escolha invalida, tente novamente")
  if choice == 1:
    try:
      largura = int(input("- Insira a quantidade de caracteres que a senha deve ter: "))
      if largura > 28:
        print("- A largura deve ir ate 28")
        continue
    except ValueError:
      print("- Dado invalido")
      continue
    gerador.gerarSenha(largura)

  elif choice == 2:
    print("Adeus!..")
    break