#Programa desenvolvido em Python para verificação se o digitado se parece com um CNPJ
cnpj = input(' Digite os 14 números do seu CNPJ:  ') .replace (".","") .replace ("/","") .replace ("-", "")     #Linha para a digitação do CNPJ e comandos para que o ponto, barra e traço não sejam contados
conta = len(cnpj)    #linha para a leitura do CNPJ, quantos carcteres, fora os que não são contados, tem
if conta != 14:
    print("CNPJ inválido!")    #Primeira parte, se não houver 14 caracteres, não se parece então irá aparecer uma mensagem de erro
else:
    print("CNPJ aceito")    #Segunda parte, se tiver os 14 aceitáveis, se parece com um CNPJ, logo é aceito
