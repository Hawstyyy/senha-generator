import string
import random as r

class gerador():
  def gerarSenha(largura):
    random = []
    senha = []
    senha_str = ''

    random += string.ascii_lowercase
    random += string.ascii_uppercase
    random += string.digits
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