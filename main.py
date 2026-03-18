import processamento

print("=== SISTEMA DE DESEMPENHO ACADÊMICO ===\n")

# Você pode escolher usar entrada manual OU dados prontos

# OPÇÃO 1: Entrada do usuário
# alunos = processamento.coletar_alunos()

# OPÇÃO 2: Dados prontos (recomendado deixar isso no trabalho)
alunos = [
    ("Ana", [8.0, 7.5, 9.0]),
    ("Carlos", [5.0, 6.0]),
    ("Marina", [10.0, 9.5, 9.0]),
    ("João", []),
    ("Pedro", [6.0, 6.5, 5.5])
]


processamento.processar_alunos(alunos)

top, media = processamento.encontrar_top_student(alunos)

print("\nTop Student:")
print(f"{top} com média {media:.2f}")

processamento.gerar_relatorio(alunos)

print("\nRelatório gerado com sucesso!")