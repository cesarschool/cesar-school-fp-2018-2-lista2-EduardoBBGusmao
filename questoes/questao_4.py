## QUESTÃO 5 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2015-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    data = input()

    # Verifica todos os numeros que acabam com 31 dias

    if((data[6] == '1' or data[6] == '3' or data[6] == '5' or data[6] == '7' or data[6] == '8' or data[5:7] == '10' or data[5:7] == '12') and data[8:10] == '31'):
        
        if(data[5:7] == '10'):
            Mes = int(data[5:7]) + 1
            data = data[:4]+ '-' + str(Mes) + '-' + '01'
        elif(data[5:7] == '12'):
        	Mes = int(data[5:7]) + 1
        	Ano = int(data[:4]) + 1
        	data = str(Ano) + '-' + str(Mes) + '-' + '01'
        else:
            Mes = int(data[5:7]) + 1
            data = data[:4]+ '-0' + str(Mes) + '-' + '01'
        print(data)

    # Verifica todos os numeros que acabam com 30 dias

    elif((data[6] == '4' or data[6] == '6' or data[6] == '9' or data[5:7] == '11') and data[8:10] == '30'):
        
        if(int(data[5:7]) > 8):
            Mes = int(data[5:7]) + 1            
            data = data[:4]+ '-' + str(Mes) + '-' + '01'
        else:
            Mes = int(data[5:7]) + 1
            data = data[:4]+ '-0' + str(Mes) + '-' + '01'

        print(data)    


    # Verifica se em está no mes de fevereiro e é bissexto

    elif(data[6] == '2' and (data[8:10] == '28' or data[8:10] == '29')):
        if(data[8:10] == '29'):
            Mes = int(data[5:7]) + 1
            if(int(data[:4]) % 4 == 0):
                data = data[:4]+ '-0' + str(Mes) + '-' + '01'
        elif(int(data[:4]) % 4 == 0):
            data = data[:4]+ '-' + data[5:7] + '-' + '29'
        else:
            Mes = int(data[5:7]) + 1
            data = data[:4]+ '-0' + str(Mes) + '-' + '01'
        print(data)

    else:
        print("Data inválida")

if __name__ == '__main__':
    main()
