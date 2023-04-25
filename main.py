import json 
from datetime import date
#Abre arquivo
load = open("respostas.json")
#Armazena em uma variavel
gabarito = json.load(load)

# resultado_A = """Você é uma pessoa de Dominância e por isso é muito ativa(o) ao lidar com problemas e desafios.
# Você pode ser descrita(o) como uma pessoa egocêntricas, diretas, ousadas, dominadoras, exigentes, enérgicas, determinadas.
# Porém podem parecer arrogante porque fala sem pensar e isso cria medo nas pessoas. Como você é multitarefa, pode não dar conta de toda demanda que absorve.
# Possui problema com delegação e não consegue receber feedback.
# A palavra de ordem para você é CALMA, vai mais devagar com Pessoas.
# Além disso, você pontuou bem em Estabilidade e por isso também é apreciador(a) de um ritmo constante, de segurança e não gosta de mudança súbita.
# Você pode ser descrita(o) como uma pessoa paciente, confiável, calma, leal, persistente, gentil e previsível.
# Porém você pode abandonar quanto têm um conflito, ser demasiadamente otimista e ser indireto na comunicação, já que fala muito.
# Possui falta de iniciativa e, por não gostar de mudanças, corre pouco risco. Além disso, você guarda rancor e pode ser possessível.
# A palavra de ordem para você é VAI. Porque depois que você começa, vai até o fim."""
# resultado_B = """Você é uma pessoa de Influência e por isso é uma pessoa que gosta de influenciar os outros através da conversa e atividades.
# Você pode ser descrita(o) como uma pessoa entusiasta, persuasiva, convincente, amistosa, comunicativa, confiante e otimista.
# Porém você pode abandonar quanto têm um conflito, ser demasiadamente otimista e ser indireto na comunicação, já que fala muito.
# Possui problema com administração do tempo, não completa tarefas e é desorganizada(o). Confia demais nas pessoas e isso pode te trazer problemas.
# A palavra de ordem para você é ACABATIVA. Termina aquilo que começou, vai até o fim!
# Além disso, você pontuou bem em Estabilidade e por isso também é apreciador(a) de um ritmo constante, de segurança e não gosta de mudança súbita.
# Você pode ser descrita(o) como uma pessoa paciente, confiável, calma, leal, persistente, gentil e previsível.
# Porém podem parecer arrogante porque fala sem pensar e isso cria medo nas pessoas. Como você é multitarefa, pode não dar conta de toda demanda que absorve.
# Possui falta de iniciativa e, por não gostar de mudanças, corre pouco risco. Além disso, você guarda rancor e pode ser possessível.
# A palavra de ordem para você é VAI. Porque depois que você começa, vai até o fim."""
# resultado_C = """Você é uma pessoa de Dominância e por isso é muito ativa(o) ao lidar com problemas e desafios.
# Você pode ser descrita(o) como uma pessoa egocêntricas, diretas, ousadas, dominadoras, exigentes, enérgicas, determinadas.
# Porém podem parecer arrogante porque fala sem pensar e isso cria medo nas pessoas. Como você é multitarefa, pode não dar conta de toda demanda que absorve.
# Possui problema com delegação e não consegue receber feedback.
# A palavra de ordem para você é CALMA, vai mais devagar com Pessoas.
# Além disso, você pontuou bem em Conformidade e por isso também é adepta(o) à aderir regras, regulamentos e estrutura. Gosta de fazer com qualidade e certo na primeira vez.
# Você pode ser descrita(o) como uma pessoa disciplinada, cautelosa, sistemática, precisa, analítica, perfeccionista e lógica.
# Porém podem parecer arrogante porque fala sem pensar e isso cria medo nas pessoas. Como você é multitarefa, pode não dar conta de toda demanda que absorve.
# Você é uma pessoa muito crítica e inflexível e isso faz com que seja muito dura(o) consigo mesma(o) e internalize sentimentos.
# A palavra de ordem para você é FLEXIBILIDADE. Pára de buscar os 110% de conhecimento e começa logo!"""
# resultado_D = """Você é uma pessoa de Dominância e por isso é muito ativa(o) ao lidar com problemas e desafios.
# Você pode ser descrita(o) como uma pessoa egocêntricas, diretas, ousadas, dominadoras, exigentes, enérgicas, determinadas.
# Porém podem parecer arrogante porque fala sem pensar e isso cria medo nas pessoas. Como você é multitarefa, pode não dar conta de toda demanda que absorve.
# Possui problema com delegação e não consegue receber feedback.
# A palavra de ordem para você é CALMA, vai mais devagar com Pessoas.
# Além disso, você pontuou bem em Estabilidade e por isso também é apreciador(a) de um ritmo constante, de segurança e não gosta de mudança súbita.
# Você pode ser descrita(o) como uma pessoa paciente, confiável, calma, leal, persistente, gentil e previsível.
# Porém podem parecer arrogante porque fala sem pensar e isso cria medo nas pessoas. Como você é multitarefa, pode não dar conta de toda demanda que absorve.
# Possui falta de iniciativa e, por não gostar de mudanças, corre pouco risco. Além disso, você guarda rancor e pode ser possessível.
# A palavra de ordem para você é VAI. Porque depois que você começa, vai até o fim."""


#Dados do aluno
RA = input("Qual o seu RA?\n")
Nome = input("Qual o seu nome?\n")
Email = input("Qual o seu email?\n")



respondido = []
#Itera sobre os dados
for i in gabarito["Respostas"]:
    pergunta_atual = ""
    while pergunta_atual not in ["A", "B", "C", "D"]:
        pergunta_atual = input(f'Com qual você mais se identifica?\n A:{i["D"]} \n B:{i["I"]} \n C:{i["S"]} \n D:{i["C"]}\n Resposta: ').upper()
    respondido += pergunta_atual
print(respondido)
# respondido = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
A = str(format(respondido.count("A")/0.4, ".0f"))+"%"
B = str(format(respondido.count("B")/0.4, ".0f"))+"%"
C = str(format(respondido.count("C")/0.4, ".0f"))+"%" 
D = str(format(respondido.count("D")/0.4, ".0f"))+"%"
# print(f'Você pontuou: \n{A}% Dominante \n{B}% Influente \n{C}% Estavel \n{D}% Conformado')

#Registrando a data do teste
data_atual = date.today()
data_em_texto = '0{}/0{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)

registro = {"RA": RA,
            "Nome" : Nome, 
            "Email" : Email, 
            "Dominante": A,
            "Influente": B,
            "Estavel": C,
            "Conformado": D,
            "Data" : data_em_texto}

with open('cadastro.json', 'w') as outfile:
    json.dump(registro,outfile,indent=3)
#Fecha o arquivo
load.close()