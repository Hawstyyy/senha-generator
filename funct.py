import string
import random as r

class gerador():
  def gerarSenha(largura,choice_special,choice_num,choice_letras):
    random = []
    senha = []
    senha_str = ''

    if choice_letras == 'S':
      random += string.ascii_lowercase
      random += string.ascii_uppercase

    if choice_num == 'S':
      random += string.digits

    if choice_special == 'S':
      random += string.punctuation

    for i in range(largura):
      randomcaracter = r.choice(random)

      if randomcaracter in senha:
        r.shuffle(random)
        randomcaracter = r.choice(random)
        senha.append(randomcaracter)
      
      else:
        senha.append(randomcaracter)

    for i in senha:
      senha_str += i
    print(f"- Sua nova senha: {senha_str}")