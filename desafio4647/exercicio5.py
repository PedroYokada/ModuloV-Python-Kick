### 5. Função de Contagem de Vogais
""" 
**Enunciado:**

Crie uma função chamada `contar_vogais` que recebe uma string como parâmetro 
e retorna o número de vogais (a, e, i, o, u) presentes na string. """

def contar_vogais(texto):
  
  soma_vogais = 0
  for letra in texto: 
    if letra in "aeiou":
      soma_vogais += 1
  return soma_vogais

resultado = contar_vogais("Programacao".lower())
print(resultado)  # Saída: 5
    
  
