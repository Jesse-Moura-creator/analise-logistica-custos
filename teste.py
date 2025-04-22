#print("batata")
'''
#EXEMPLO DE UMA F STRING
first_name = "Jesse" #VARIAVEL A
last_name = "Moura" #VARIAVEL B
full_name = f"{first_name} {last_name}" #F STRING
print(full_name)
'''
'''
#EXEMPLO DE TUPLA USANDO FUNÇÃO RETORNANDO MÚLTIPLOS VALORES:
def sum_and_product(x, y):
    return(x + y), (x * y)
sp = sum_and_product(2, 3) # sp é (5, 6)
s, p = sum_and_product(5, 10) # s é 15, p é 50 
#print(sp)
#print(s)
#print(p)
'''


'''
# EXEMPLOS DE DICIONÁRIOS (dict) 
empty_dict = {}
empty_dict2 = dict()
grades = {"Jesse": 80, "Fabiano": 95}

# PARA PESQUISAR O VALOR DE UMA CHAVE, PODE-SE USAR O COLCHETE:
jesses_grade = grades["Jesse"]       # IGUAL A 80

#MAS APARECERÁ UM KEYERROR, CASOPROCURADA UMA CHAVE QUE NÃO ESTÁ NO DICIONÁRIO:
try:
    joes_grade =["Joe"]
except KeyError:
    print("no grade for Joe!")

#PARA VERIFICAR A EXISTÊNCIA DE UMA CHAVE, PODE-SE USAR O IN:
jesse_has_grade = "Jesse" in grades   # verdadeiro
joe_has_grade = "Joe" in grades       # falso

# NOS DICIONÁRIOS, O MÉTODO GET RETORNA UMA VALOR PADRÃO (EM VEZ DE GERAR UMA EXCEÇÃO) QUANDO SE PROCURA POR UMA CHAVE QUE NÃO ESTÁ NO DICIONÁRIO
jesses_grade = grades.get("Jesse", 0) #igual a 80
joes_grade = grades.get("Joe", 0) #igual a 0
no_ones_grade = grades.get("No One") # o padrão é none

# É POSSÍVEL TAMBÉM ATRIBUIR PARES DE VALOR-CHAVE USANDO OS COLCHETES:
grades["Fabiano"] = 99     #substitui o valor anterior, que era 95
grades["Joe"] = 100        #adiciona uma terceira entrada
num_students = len(grades) #igual a 3

# OS DICIONÁRIOS TAMBÉM PODEM REPRESENTAR DADOS ESTRUTURADOS:
tweet = {
    "user" : "jessemoura",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datasciense", "awesome", "#yolo"]
}
'''

