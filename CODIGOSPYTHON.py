#LISTA DE CÓDIGOS E SOLUÇÕES PYTHON.
# AQUI EU DEIXAREI UMA LISTA DE TODOS OS CODIGOS QUE EU VI DURANTE AS AULAS,
#EM ORDEM CRONOLÓGICA E DESCRITO SUAS FUNÇÕES.# 



# TIPOS DE VARIAVEIS.
# 1 VARIAVEL: "INT" (INTEGER) INDICA NUMEROS INTEIROS
# 2 VARIAVEL: "FLOAT" (PONTO FLUTUANTE) INDICA NUMEROS DECIMAIS
# 3 VARIAVEL: "STRING" (CARACTERES) INDICA TEXTO OU UMA SEUQENCIA DE CARACTERES
# 4 VARIAVEL: "BOOLEAN" (VERDADEIRO OU FALSO)
# 5 VARIAVEL: "NONE"  (NADA) INDICA AUSENCIA DE VALOR

#EXEMPLOS 

IDADE = 30  #(INTEIRO)
PESO = 30.85 #(FLOAT/OU DECIMAL)
NOME = "JOAO" #(STRING)
BOOLEAN = "VERDADEIRO" #(VERDADEIRO OU FALSO)
NONE = " " #(AUSENCIA DE VALOR)

#O PYTHON IDENTIFICA OS TIPOS DE VARIAVEIS AUTOMATICAMENTE CASO
#QUEIRA IDENFICAR O TIPO DA QUAL DEVE USAR O SEGUINTE COMANDO
print (type (IDADE)) #O TIPO DA VARIAVEL "INT" QUE INDICA "INTEIRO" APARECERA NA SUA CONSOLE.

#OBS: DIGITAR TAGS EM LETRA MINUSCULA ALGUMAS PODEM DAR ERRO EM MAIUSCULA 





 
#TAG "PRINT" FUNCIONALIDADE: MOSTRAR RESULTADO, ESCREVER NA TELA UMA VARIAVEL, MENSAGEM DE
# TEXTO OU RESULTADO DE VARIAVEIS ETC.
#PARA USAR ESTA TAG VOCE PRECISA ATRIBUIR UM VALOR A ELA (VARIAVEL) OU SOMENTE UM TEXTO QUALQUER.
# SINTAXE: PRINT ('CONTEUDO DE TEXTO OU VARIAVEL') 
# EXEMLPO:#

 # LADO ESQUERDO (VARIAVEL) LADO DIREITO VALOR DA VARIAVEL OU ATRIBUTO
                       
                       MENSAGEM = 'OLÁ ALUNO.'
                       
                       print (MENSAGEM)
                             #OU 
                       print ('OLA ALUNO.')
#***********************************************************************************


# COMO DIGITAR MAIS DE UMA VARIAVEL EM UMA SÓ LINHA.
#NORMALMENTE APRENDEMOS DA SEGUINTE FORMA COMO FAZER UMA SEQUENCIA DE CODIGOS EM
#APENAS UMA LINHA:

VARIAVEL1 = 23
VARIAVEL2 = 1.85
VARIAVEL3 = 'Paulo'

#SEPARAMOS AS VARIAVEIS POR VIRGULA
print ('oi meu nome é', VARIAVEL3, 'tenho', VARIAVEL1, 'anos de idade e tenho', VARIAVEL2, 'de altura', )

#FICANDO DA SEGUINTE MANEIRA:
  'oi meu nome é paulo tenho 23 anos de idade e tenho 1.85 de altura'
                         
                         
                         
#USANDO A TAG: PRINT(F{})
#FAZ O MESMO QUE A SINTAXE ACIMA PORÉM DE UM JEITO MAIS DIDÁTICO E COMPREESÍVEL SEPARANDO 
#AS VARIAVEIS ENTRE CHAVES {}.
#EXEMPLO:
        
print (f'oi meu nome é {VARIAVEL3} e tenho {VARIAVEL1} de idade')
        
        
        
  