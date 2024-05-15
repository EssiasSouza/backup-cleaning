import datetime
import time
import os
import shutil
import pathlib
import lib_applogs

print('Starting application')
lib_applogs.logger.warning('Starting application')

# TESTING DATE
input_date_str = "04/05/2024"
current_date = datetime.datetime.strptime(input_date_str, "%d/%m/%Y")
formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

# current_date = datetime.datetime.now()
# formated_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

print("Data Formatada:", formated_date)
lib_applogs.logger.warning(f'Defined date:{formated_date}')

def daily():

    day_less = 4

    adjusted_date = current_date - datetime.timedelta(days=day_less)
    adjusted_formated_date = adjusted_date.strftime("%d/%m/%Y %H:%M:%S")
    print("Adjusted date:", adjusted_formated_date)

    folder_path = r"C:\\Users\\essias.souza\\OneDrive - FleetCor\DEV\\Python\\ConcLimpBackupV2.0.0\\Test_Enviroment\\month04"

    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    if subfolders:

        for subfolder in subfolders:
            modification_time = os.path.getmtime(subfolder)
            modification_date = datetime.datetime.fromtimestamp(modification_time)
            modification_formated_date = modification_date.strftime("%d/%m/%Y %H:%M:%S")

            if modification_date < adjusted_date:
                print(subfolder)
                print("Modification date of folder:", modification_formated_date)
                shutil.rmtree(subfolder)
                lib_applogs.logger.warning(f'Deleted: {subfolder}')
                time.sleep(2)
                
    else:
        print('-- There is nothing to delete')

    print('End of process.')
    lib_applogs.logger.warning(f'End of daily process.')
    time.sleep(135)

daily()

# Manipulação de arquivos
caminho_diretorio = pathlib.Path.home() / "exemplo_diretorio"
caminho_arquivo = caminho_diretorio / "exemplo_arquivo.txt"

# Criando um diretório
os.makedirs(caminho_diretorio, exist_ok=True)
print(f"Diretório '{caminho_diretorio}' criado.")

# Criando e escrevendo em um arquivo
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write("Este é um arquivo de exemplo.")
print(f"Arquivo '{caminho_arquivo}' criado e escrito.")

# Lendo de um arquivo
with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
print("Conteúdo do Arquivo:", conteudo)

# Movendo um arquivo (renomeando)
novo_caminho_arquivo = caminho_diretorio / "novo_exemplo_arquivo.txt"
shutil.move(caminho_arquivo, novo_caminho_arquivo)
print(f"Arquivo movido para '{novo_caminho_arquivo}'.")

# Removendo um arquivo
os.remove(novo_caminho_arquivo)
print(f"Arquivo '{novo_caminho_arquivo}' removido.")

# Removendo um diretório
os.rmdir(caminho_diretorio)
print(f"Diretório '{caminho_diretorio}' removido.")
