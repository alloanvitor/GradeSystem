# Função para validar se a lista de notas é válida
def validar_notas(notas):

    if not isinstance(notas, list):
        return False

    if len(notas) == 0:
        return False

    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False

    return True

# Função para calcular média
def calcular_media(notas):

    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    return media

# Função para verificar situação do aluno
def verificar_situacao(media):

    if media < 7:
        return "Recuperação"
    else:
        return "Aprovado"
    
# Função para encontrar o Top Student
def encontrar_top_student(lista_alunos):

    maior_media = 0
    top_student = ""

    for nome, notas in lista_alunos:

        if validar_notas(notas):

            media = calcular_media(notas)

            if media > maior_media:
                maior_media = media
                top_student = nome

    return top_student, maior_media