print("=" * 41)
print("  SELEÇÃO PARA O PROJETO DE TECNOLOGIA ")
print("=" * 41)

conhecimentos_exigidos = {
    "python",
    "lógica",
    "git",
    "banco de dados",
    "html"
}

turnos_disponiveis = ("manhã", "tarde")

nome = input("Qual o seu nome? ")
idade = int(input("Qual sua idade? "))
curso = input("Qual seu curso? ")
semestre = int(input("Está em qual semestre neste curso? "))

semestre1 = str(semestre)
codigoinscricao = semestre1 + curso + nome

def get_email():
    valid = False
    while not valid:
        email = input("Qual seu email: ")
        if "@" in email and "." in email:
            valid = True
            return email
        else:
            print("Email valido deve conter(@) e (.)")
email = get_email()

conhecimentos = input("Qual seus conhecimentos?")
turno = input("Qual a sua disponibilidade de turnos? ")
trabalho_em_equipe = input("Tem capacidade de trabalhar em equipe? ").lower() == "sim"
computador_proprio = input("Tem computador própio? ").lower() == "sim"

con = set((conhecimentos.strip().lower() for conhecimentos in conhecimentos.split(",")))

conhecimentos_difference = conhecimentos_exigidos.difference(con)
conhecimento_que_falta = len(conhecimentos_difference)

conhecimentos_intersection = con.intersection(conhecimentos_exigidos)
quantidade_de_conhecimento = len(conhecimentos_intersection)
pontos = quantidade_de_conhecimento * 2

if turno in turnos_disponiveis: 
    pontos = pontos + 1

if trabalho_em_equipe == True:
    pontos = pontos + 2

if computador_proprio == True:
    pontos = pontos + 1

Candidato = {
    "nome" : nome,
    "idade" : idade,
    "curso" :curso,
    "semestre" :semestre,
    "email" : email,
    "conhecimentos" : con,
    "turno": turno,
    "trabalho_em_equipe" : trabalho_em_equipe,
    "computador_proprio" : computador_proprio
    }

print("=" * 41)
print("          RESULTADO DA SELEÇÃO")
print("=" * 41)

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Conhecimentos compatíveis: {conhecimentos_intersection}")
print(f"Quantidade de conhecimento(s) compativeis: {quantidade_de_conhecimento}")
print(f"Conhecimentos faltantes: {conhecimentos_difference}")
print(f"Quantidade de conhecimento(s) faltantes: {conhecimento_que_falta}")
if turno in turnos_disponiveis:
    print("Turno válido: sim")
else:
    print("Turno válido: não")
    
if trabalho_em_equipe:
    print("Trabalho em equipe: sim")
else:
    print("Trabalho em equipe: não")

if computador_proprio:
    print("Computador próprio: sim")
else:
    print("Computador próprio: não")

print("Pontuação final: {} pontos".format(pontos))

if ( idade >= 16 
    and quantidade_de_conhecimento >= 3 
    and turno in turnos_disponiveis 
    and trabalho_em_equipe == True 
    and pontos >=12
):
    print("CLASSIFICAÇÃO: CANDIDATO DESTAQUE")
    print("Conseguiu o minimo de 12 pontos e cumpriu todos os requisitos obrigatórios.")

elif ( idade >= 16 
    and quantidade_de_conhecimento >= 3 
    and turno in turnos_disponiveis 
    and trabalho_em_equipe == True 
    and pontos <12 and pontos >= 7
):
    
    print("CLASSIFICAÇÃO: APROVADO")
    print("Cumpriu todos os requisitos obrigatórios.")

elif pontos >=5:
    print("CLASSIFICAÇÃO: BANCO DE TALENTOS")
    print("Obteve pelo menos 5 pontos, mas não cumpriu todos os requisitos.")
    

else:
    print("CLASSIFICAÇÃO: NÃO APROVADO")
    print("Obteve menos de 5 pontos.")


motivos = []

if idade <= 15: 
    motivos.append("Idade abaixo da idade minima")
if quantidade_de_conhecimento < 3:
    motivos.append("Quantidade minima de conhecimento não atingido")
if turno not in turnos_disponiveis:
    motivos.append("Turno escolhido não disponivel")
if trabalho_em_equipe == False:
    motivos.append("Não tem capacidade de trabalar em equipe")

print("Lista de motivos para reprovação:")
print(motivos)

print(f"Seu codigo de inscrição é: {codigoinscricao}")