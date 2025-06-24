def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        return f.read()