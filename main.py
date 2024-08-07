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
    largura = int(input("- Insira a quantidade de caracteres que a senha deve ter: "))
    gerador.gerarSenha(largura)