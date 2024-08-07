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
    continue

  if choice == 1:
    try:
      largura = int(input("- Insira a quantidade de caracteres que a senha deve ter: "))
      if largura > 28:
        print("- A largura deve ir ate 28")
        continue
  
    except ValueError:
      print("- Dado invalido")
      continue
  
    choice_special = input("- A senha deve conter caracteres especiais? (S/N) ").capitalize()

    if choice_special not in ['S', 'N']:
      print("\n- Escolha invalida, tente novamente")
      continue
    
    choice_num = input("- A senha deve conter numeros? (S/N) ").capitalize()

    if choice_num not in ['S', 'N']:
      print("\n- Escolha invalida, tente novamente")
      continue

    choice_letras = input("- A senha deve conter letras? (S/N) ").capitalize()

    if choice_letras not in ['S', 'N']:
      print("\n- Escolha invalida, tente novamente")
      continue

    gerador.gerarSenha(largura,choice_special,choice_num,choice_letras)

    again = input("- Deseja gerara sua senha novamente? (S/N) ").capitalize()

    if again not in ['S','N']:
      print("\n- Escolha invalida, tente novamente")
      continue

    if again == 'S':
      gerador.gerarSenha(largura,choice_special,choice_num,choice_letras)

  elif choice == 2:
    print("Adeus!..")
    break
