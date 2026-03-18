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
