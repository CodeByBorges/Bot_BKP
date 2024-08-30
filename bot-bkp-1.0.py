import shutil
import os
import datetime

def realizar_backup(diretorio_fonte, diretorio_destino):
    try:
        # Verifica se o diretório de destino existe
        if os.path.exists(diretorio_destino):
            # Remove o diretório de destino se ele já existir
            shutil.rmtree(diretorio_destino)
            print(f"Pasta de backup anterior removida: '{diretorio_destino}'")

        # Realiza a cópia dos arquivos do diretório fonte para o diretório de destino
        shutil.copytree(diretorio_fonte, diretorio_destino)
        print(f"Backup concluído com sucesso de '{diretorio_fonte}' para '{diretorio_destino}'")
    except Exception as e:
        print(f"Erro ao realizar backup: {str(e)}")

if __name__ == "__main__":
    # Diretórios de origem e destino para os backups
    diretorio_origem1 = r"B:\1. HELPDESK\28- Alisson Borges"
    diretorio_destino1 = r"B:\1. HELPDESK\BKP-Alisson-Borges"

    diretorio_origem2 = r"B:\1. HELPDESK\TESTE1"
    diretorio_destino2 = r"B:\1. HELPDESK\BKP-TESTE1"

    # Data atual para utilizar na criação de diretórios de destino únicos
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Nome dos diretórios de destino baseados na data atual
    diretorio_destino1_data = rf"B:\1. HELPDESK\BKP-Alisson-Borges_{data_atual}"
    diretorio_destino2_data = rf"B:\1. HELPDESK\BKP-TESTE1_{data_atual}"

    # Realiza backup para BKP1
    realizar_backup(diretorio_origem1, diretorio_destino1_data)

    # Realiza backup para BKP2
    realizar_backup(diretorio_origem2, diretorio_destino2_data)
