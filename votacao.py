#se a pessoa tem idade >= a 18 anos e <= 69 anos, ela tem voto obrigatório. Se a idade for >= a 70 anos, o voto é facultativo

idade = 71
voto_obrig = idade >= 18 and idade <= 69
voto_facul = idade >= 70 or idade <= 16 and idade <= 17
voto_negado = idade < 16

if idade  >= 18 and idade <= 69:
    print("Voto obrigatório")
elif idade < 16:
    print("Voto negado")
else:
    print("Voto facultativo")


#jeito otimizado de fazer (de acordo com IA):

idade = 71

if 18 <= idade <= 69:
    print("Voto obrigatório")
elif idade >= 70 or 16 <= idade <= 17:
    print("Voto facultativo")
else:
    print("Voto negado")
