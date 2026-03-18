import processamento

print("Cadastro de alunos\n")

alunos = processamento.coletar_alunos()

processamento.processar_alunos(alunos)

top, media = processamento.encontrar_top_student(alunos)

print(f"\nTop Student: {top} com média {media:.2f}")

processamento.gerar_relatorio(alunos)