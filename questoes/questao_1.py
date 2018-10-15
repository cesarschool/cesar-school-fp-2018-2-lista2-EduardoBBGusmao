## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 1")
    entrada = input().split(", ")
    Saida = []
    i = 0
    j = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    while i < len(entrada):
   		while j < len((entrada[i])):
   			if len(entrada[i]) > 5 and len(entrada[i]) < 13:
   				num6 = 1

   			if entrada[i][j].isdigit():
   				num1 = 1
   			elif entrada[i][j].isupper():
   				num3 = 1
   			elif entrada[i][j].islower():
   				num4 = 1
   			elif entrada[i][j] == '$' or entrada[i][j] == '#' or entrada[i][j] == '@':
   				num5 = 1
   			
   			j += 1
   		num = num1 + num2+ num3 + num4 + num5 + num6
   		Saida.append(num)
   		num =0
   		num1 =0
   		num2 =0
   		num3 =0
   		num4 =0
   		num5 =0
   		num6 =0
   		j=0
   		i+=1

    j=0
    while j < len(Saida):
   		if Saida[j] == 5:
   			print(entrada[j])
   		j+=1


if __name__ == '__main__':
    main()
