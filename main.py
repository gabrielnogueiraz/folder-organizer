import os
import shutil

def organizar_arquivos_por_extensao(pasta_origem):
    if not os.path.exists(pasta_origem):
        print(f"A pasta '{pasta_origem}' não existe.")
        return
    
    for arquivo in os.listdir(pasta_origem):
        caminho_completo = os.path.join(pasta_origem, arquivo)

        if os.path.isdir(caminho_completo):
            continue

        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower().replace(".", "")  
        subpasta = os.path.join(pasta_origem, extensao if extensao else "sem_extensao")

        os.makedirs(subpasta, exist_ok=True)

        shutil.move(caminho_completo, os.path.join(subpasta, arquivo))
        print(f"Movido: {arquivo} -> {subpasta}")

pasta_origem = "/caminho/para/sua/pasta"  
organizar_arquivos_por_extensao(pasta_origem)
