# Daily Cleanup application (BACKUP CLEANING)
Below we have the `Portuguese` version of this document.
This Python application performs daily cleanup operations on specified directories, removing files and subfolders that are older than a given number of days. The application logs its actions and can be configured via a `settings.json` file.

### Purpose of the application
The **Backup Cleaning** allows to purge folders of backups in a server. The parameters of time (in days), locations and logs configurations can be set through a file named settings.json. This application runs reading all folders and files on the root path, verifying the modification date, and if the name of file or folder has some part as excluded or exception. After that, all of files or folders and its files will be deleted.

The settings.json file uses some examples to config:
- The first setting is the time at which the application should be run again. This time is defined in seconds on the `run_pause_time` item.
- Log folder and name. You can choose the best name and location for that using the items `logs_path` and `log_name`.
- `watchedDir` is the item that brings together the following sets:
 - `day_less` to count before the current computer date to purge files, folders and its files.
 - `folder_path` Is the root path that the application needs to search for fildes and subfolders with modification date below the maximum purge date. For example, if you set the value to 15 and the current date is 2024/05/20, the application will only delete folders that were modified on dates less than or equal to 2024/05/04.
 - `ExceptExtDir` is the configuration of exceptions, where you can write terms that you want to remove items from list that have some part of name as the exception settings. Example, if you have a file called file.txt and you input there the `tx`, `txt`, `file`, `.txt` or any other part from name file, this file will be excluded from list of file.
 (file_name = `["287478379AHMD.EAS","89384782334HRHASD.EAS"]` ExceptExtDir = ["TXT,JPG,47823"] | DELETE ONLY = 287478379AHMD.EAS because 8938`47823`34HRHASD.EAS has `47823`)

 OBS: dont type SPACES into `ExceptExtDir` list.

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Details](#details)

## Overview

The application:
1. Reads configuration parameters from `settings.json`.
2. Defines the current date and formats it.
3. Iterates over specified directories to delete files and subfolders older than a specified number of days.
4. Logs all actions using `lib_applogs`.
5. Sleeps for a configurable amount of time before running again.

## Setup

1. Ensure you have Python installed on your system.
2. Install necessary dependencies (if any, like `lib_applogs`).
3. Place the application and `settings.json` in the same directory.

## Configuration

Create a `settings.json` file with the following structure:

```json
[
    {
        "folder_path": "path/to/your/folder",
        "day_less": 30,
        "run_pause_time": 3600
    }
]
```

- `folder_path`: The path of the directory to clean up.
- `day_less`: The number of days to subtract from the current date to determine which files/folders to delete.
- `run_pause_time`: The time in seconds to wait before running the application again.

## Usage

Runing with python
 - Copy this repository to any folder on your computer
 - Make sure install python and its mentioned dependencies below.
 - Change the settings.json file according to your preferences.
Run the application using the command:
```sh
python backup-cleaning.py
```
To stop the application, press `Ctrl+C`.

Run the application using the compiled file:

 - 1 - Copy the backup-cleaning.v2.1.0.exe from `dist` folder to any folder
 - 2 - Copy the settings.json file to the same folder of backup-cleaning.v2.1.0.exe
 - 3 - Change the settings.json file according to your preferences.
 - 4 - Try doing a test before to ensure if the result is the same waited for you.

## Details

### application Breakdown

- **Imports**: The application imports necessary libraries, including `datetime`, `time`, `os`, `shutil`, `pathlib`, and `json`.
- **Logging**: Uses `lib_applogs` for logging important actions and messages.
- **Main Function**: The `main()` function is where the core logic resides.
  - **Current Date**: Defines and formats the current date.
  - **Delete Function**: Deletes files and subfolders older than the specified number of days.
  - **Sleep and Repeat**: Sleeps for the specified amount of time before repeating the process.

### Main Function

The `main()` function executes the following steps:
1. **Define Date**: Gets the current date and formats it.
2. **Delete Old Files/Folders**: Reads the `settings.json` and deletes files/folders older than the specified number of days.
3. **Pause and Restart**: Calculates the sleep time from `settings.json` and pauses before the next run.

### Delete Function

The `delete()` function performs the following actions:
1. **Read Settings**: Opens and reads the `settings.json` file.
2. **Iterate Over Parameters**: For each parameter set in the settings, it:
   - Prints and logs the directory path.
   - Calculates the date threshold.
   - Deletes subfolders and files older than the threshold.
3. **Log and Sleep**: Logs actions and sleeps for 2 seconds between deletions.

### Error Handling

The application includes basic error handling:
- **Try/Except Block**: Catches and logs errors if no objects are found for deletion.

### application Termination

The application can be terminated gracefully using `KeyboardInterrupt` (Ctrl+C) or in using the compiled version, you can only close the terminal.

=======
# Aplicativo de Limpeza Diária de backups (BACKUP CLEANING)

Este aplicativo Python realiza operações diárias de limpeza em diretórios especificados, removendo arquivos e subpastas que são mais antigos que um determinado número de dias. O aplicativo registra suas ações e pode ser configurado através de um arquivo `settings.json`.

### Propósito do Aplicativo

O **Backup Cleaning** permite a limpeza de pastas de backups em um servidor. Os parâmetros de tempo (em dias), locais e configurações de logs podem ser definidos através de um arquivo chamado settings.json. Este aplicativo funciona lendo todas as pastas e arquivos no caminho raiz, verificando a data de modificação, e se o nome do arquivo ou pasta contém alguma parte como excluída ou exceção. Após isso, todos os arquivos ou pastas e seus arquivos serão deletados.

O arquivo settings.json usa alguns exemplos para configuração:
- A primeira configuração é o tempo no qual o aplicativo deve ser executado novamente. Este tempo é definido em segundos no item `run_pause_time`.
- Pasta e nome do log. Você pode escolher o melhor nome e local para isso usando os itens `logs_path` e `log_name`.
- `watchedDir` é o item que agrupa os seguintes conjuntos:
  - `day_less` para contar antes da data atual do computador para purgar arquivos, pastas e seus arquivos.
  - `folder_path` é o caminho raiz que o aplicativo precisa procurar por arquivos e subpastas com data de modificação abaixo da data máxima de purga. Por exemplo, se você definir o valor para 15 e a data atual for 20/05/2024, o aplicativo só excluirá pastas que foram modificadas em datas menores ou iguais a 04/05/2024.
  - `ExceptExtDir` é a configuração de exceções, onde você pode escrever termos que deseja remover itens da lista que têm alguma parte do nome como as configurações de exceção. Exemplo, se você tem um arquivo chamado file.txt e você inserir ali `tx`, `txt`, `file`, `.txt` ou qualquer outra parte do nome do arquivo, este arquivo será excluído da lista de arquivos.
    (file_name = `["287478379AHMD.EAS","89384782334HRHASD.EAS"]` ExceptExtDir = ["TXT,JPG,47823"] | APAGAR SOMENTE = 287478379AHMD.EAS porque 8938`47823`34HRHASD.EAS tem `47823`)

OBS: não digite ESPAÇOS na lista `ExceptExtDir`.

## Índice
- [Visão Geral](#visão-geral)
- [Configuração](#configuração)
- [Uso](#uso)
- [Detalhes](#detalhes)

## Visão Geral

O aplicativo:
1. Lê os parâmetros de configuração do `settings.json`.
2. Define a data atual e a formata.
3. Itera sobre os diretórios especificados para deletar arquivos e subpastas mais antigos que um número especificado de dias.
4. Registra todas as ações usando `lib_applogs`.
5. Pausa por um tempo configurável antes de executar novamente.

## Configuração

1. Certifique-se de ter o Python instalado no seu sistema.
2. Instale as dependências necessárias (se houver, como `lib_applogs`).
3. Coloque o aplicativo e o `settings.json` no mesmo diretório.

## Configuração

Crie um arquivo `settings.json` com a seguinte estrutura:

```json
[
    {
        "folder_path": "path/to/your/folder",
        "day_less": 30,
        "run_pause_time": 3600
    }
]
```

- `folder_path`: O caminho do diretório a ser limpo.
- `day_less`: O número de dias a subtrair da data atual para determinar quais arquivos/pastas deletar.
- `run_pause_time`: O tempo em segundos para esperar antes de executar o aplicativo novamente.

## Uso

Executando com python:
- Copie este repositório para qualquer pasta em seu computador.
- Certifique-se de instalar o Python e suas dependências mencionadas abaixo.
- Altere o arquivo settings.json de acordo com suas preferências.

Execute o aplicativo usando o comando:
```sh
python backup-cleaning.py
```
Para parar o aplicativo, pressione `Ctrl+C`.

Executando o aplicativo usando o arquivo compilado:

1. Copie o backup-cleaning.v2.1.0.exe da pasta `dist` para qualquer pasta.
2. Copie o arquivo settings.json para a mesma pasta do backup-cleaning.v2.1.0.exe.
3. Altere o arquivo settings.json de acordo com suas preferências.
4. Tente fazer um teste antes para garantir que o resultado seja o esperado.

## Detalhes

### Detalhamento do Aplicativo

- **Imports**: O aplicativo importa as bibliotecas necessárias, incluindo `datetime`, `time`, `os`, `shutil`, `pathlib` e `json`.
- **Logging**: Usa `lib_applogs` para registrar ações e mensagens importantes.
- **Função Principal**: A função `main()` é onde reside a lógica principal.
  - **Data Atual**: Define e formata a data atual.
  - **Função de Deleção**: Deleta arquivos e subpastas mais antigos que o número especificado de dias.
  - **Pausa e Repetição**: Pausa pelo tempo especificado antes de repetir o processo.

### Função Principal

A função `main()` executa os seguintes passos:
1. **Definir Data**: Obtém a data atual e a formata.
2. **Deletar Arquivos/Pastas Antigos**: Lê o `settings.json` e deleta arquivos/pastas mais antigos que o número especificado de dias.
3. **Pausa e Reinício**: Calcula o tempo de pausa a partir do `settings.json` e pausa antes da próxima execução.

### Função de Deleção

A função `delete()` executa as seguintes ações:
1. **Ler Configurações**: Abre e lê o arquivo `settings.json`.
2. **Iterar Sobre Parâmetros**: Para cada conjunto de parâmetros nas configurações, ele:
   - Imprime e registra o caminho do diretório.
   - Calcula o limite de data.
   - Deleta subpastas e arquivos mais antigos que o limite.
3. **Registrar e Pausar**: Registra as ações e pausa por 2 segundos entre as deleções.

### Tratamento de Erros

O aplicativo inclui tratamento básico de erros:
- **Bloco Try/Except**: Captura e registra erros se nenhum objeto for encontrado para deleção.

### Encerramento do Aplicativo

O aplicativo pode ser encerrado graciosamente usando `KeyboardInterrupt` (Ctrl+C) ou, na versão compilada, basta fechar o terminal.

