from util_arquivos import escrever_arquivo, ler_arquivo
escrever_arquivo("mensagem.txt", "Olá, mundo!")
conteudo = ler_arquivo("mensagem.txt")
print(conteudo)