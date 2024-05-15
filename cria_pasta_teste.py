# import os
# import datetime

# # Define o número de meses
# num_months = 12
# # Define o ano base
# year = 2023

# # Função para alterar a data de modificação de um diretório
# def change_modification_date(folder_name, mod_time):
#     # Converte o datetime para um timestamp (segundos desde a epoch)
#     mod_timestamp = mod_time.timestamp()
#     # Aplica a data de modificação e acesso
#     os.utime(folder_name, (mod_timestamp, mod_timestamp))

# # Cria as pastas, arquivos e altera a data de modificação
# for i in range(1, num_months + 1):
#     folder_name = f'Test_Enviroment\month{i:02}'
#     os.makedirs(folder_name, exist_ok=True)
#     print(f'Pasta "{folder_name}" criada com sucesso.')
    
#     # Cria um arquivo de texto dentro da pasta
#     file_name = os.path.join(folder_name, f'arquivo{i:02}.txt')
#     with open(file_name, 'w') as file:
#         file.write(f'Este é o arquivo {i:02} na pasta {folder_name}.')
#     print(f'Arquivo "{file_name}" criado com sucesso.')
    
#     # Define a data de modificação para o dia 01 do mês correspondente
#     mod_time = datetime.datetime(year, i, 1)
#     change_modification_date(folder_name, mod_time)
#     print(f'Data de modificação da pasta "{folder_name}" alterada para {mod_time}.')

# print('Todas as pastas e arquivos foram criados, e as datas de modificação das pastas foram alteradas.')







import os
import datetime

# Define o número de dias no mês de maio
num_days = 30
# Define o ano e o mês base
year = 2024
month = 4

# Função para alterar a data de modificação de um diretório
def change_modification_date(folder_name, mod_time):
    # Converte o datetime para um timestamp (segundos desde a epoch)
    mod_timestamp = mod_time.timestamp()
    # Aplica a data de modificação e acesso
    os.utime(folder_name, (mod_timestamp, mod_timestamp))

# Cria as pastas, arquivos e altera a data de modificação
for day in range(1, num_days + 1):
    folder_name = f'Test_Enviroment\\month04\\abr{day:02}'
    os.makedirs(folder_name, exist_ok=True)
    print(f'Pasta "{folder_name}" criada com sucesso.')
    
    # Cria um arquivo de texto dentro da pasta
    file_name = os.path.join(folder_name, f'arquivo{day:02}.txt')
    with open(file_name, 'w') as file:
        file.write(f'Este é o arquivo {day:02} na pasta {folder_name}.')
    print(f'Arquivo "{file_name}" criado com sucesso.')
    
    # Define a data de modificação para o respectivo dia do mês de maio de 2024
    mod_time = datetime.datetime(year, month, day)
    change_modification_date(folder_name, mod_time)
    print(f'Data de modificação da pasta "{folder_name}" alterada para {mod_time}.')

print('Todas as pastas e arquivos foram criados, e as datas de modificação das pastas foram alteradas.')

