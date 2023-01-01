import subprocess
import os
import time


def main_run(  # Created by KickOfSilver
):

    os.system("cls")  # Limpa o terminal
    requirements_check()  # Instala as dependências do pyinstaller

    file = input_name_file()  # Recebe o nome do arquivo principal da aplicação
    console = input_console_read()  # Recebe a opção de mostra o console
    name = input_name_exe()  # Recebe o nome para o executável
    one_file = input_onefile_exe()  # Recebe a opção de combinar os arquivos em um só

    icon_copy = copy_icon_path()  # Copia o ícone para a pasta do projeto
    icon_use = use_icon_path()  # Usa o ícone na criação do executável

    # Cria a string de comando para o pyinstaller com base nas opções fornecidas pelo usuário
    comando = f"pyinstaller {console} {name} {icon_copy} {icon_use} {one_file} {file}"

    # Substitui dois espaços em branco por um único espaço
    comando = comando.replace("  ", " ")
    os.system(comando)  # Executa o comando no terminal


def input_name_file():

    # Solicita o nome do arquivo principal ao usuário
    name_raw = input("nome do arquivo principal:\n")
    print("")

    # Verifica se o nome do arquivo já tem a extensão '.py'
    if ".py" in name_raw:  # Se sim, não faz nada
        pass

    else:  # Se não, adiciona a extensão '.py' ao nome do arquivo
        name = f"{name_raw}.py"

    return name  # Retorna o nome do arquivo


def input_console_read():

    while True:  # Loop infinito até que o usuário forneça uma resposta válida

        console = input("Deve mostrar o console:\n"  # Solicita ao usuário se deve mostrar o console
                        "1: sim\n" "2: não\n")
        print("")

        # Verifica a resposta do usuário
        if console == "1":  # Se o usuário escolher sim,
            console = ""  # a opção de console é vazia
            break  # Sai do loop

        elif console == "2":  # Se o usuário escolher não,
            console = "--noconsole"  # a opção de console é "--noconsole"
            break  # Sai do loop

        else:  # Se o usuário fornecer uma resposta inválida,
            print("Resposta inválida\n")  # imprime uma mensagem de erro

    return console


def input_name_exe():

    while True:  # Loop infinito até que o usuário forneça um nome válido para o arquivo executável

        program = input("Digite um nome para o arquivo executável"  # Solicita ao usuário um nome para o arquivo executável
                        " ou "
                        "pressione Enter para manter o nome padrão:\n")
        print("")

        if not program:  # Verifica se o usuário pressionou Enter sem fornecer um nome
            break  # Se sim, sai do loop

        else:  # Se não, adiciona o nome ao comando de criação do executável
            program = f"--name={program}"
            break  # Sai do loop

    # Retorna o nome do arquivo executável
    return program


def input_onefile_exe():

    while True:

        one_file = input(  # Pergunte ao usuário se ele deseja combinar os arquivos em um único arquivo.
            "Você deseja criar um arquivo executável que inclua todas as dependências do seu aplicativo?\n"
            "1: sim\n" "2: não\n")
        print("")

        if one_file == "1":  # Se o usuário escolher sim,
            one_file = "--onefile"  # a opção de console é vazia
            break  # Sai do loop

        elif one_file == "2":  # Se o usuário escolher não,
            one_file = ""  # a opção de console é "--noconsole"
            break  # Sai do loop

        else:  # Se o usuário fornecer uma resposta inválida,
            print("Resposta inválida\n")  # imprime uma mensagem de erro

    return one_file


def copy_icon_path():

    path_icon = "icon/icon.ico"  # Caminho para o ícone
    check_path = os.path.exists(path_icon)  # Verifica se o caminho existe

    if check_path == True:  # Se o caminho existe, adiciona o ícone ao executável
        icon = (  # Se o caminho não existe, não adiciona o ícone
            f"--add-data={path_icon};.")
    else:
        icon = ""  # manda a string vazia

    return icon  # Retorna a opção de ícone


def use_icon_path():

    path_icon = "icon/icon.ico"  # Caminho para o ícone
    check_path = os.path.exists(path_icon)  # Verifica se o caminho existe

    if check_path == True:  # Se o caminho existe, usa o ícone no executável
        icon = (  # Se o caminho não existe, não usa o ícone
            f"--icon={path_icon}")

    else:
        icon = ""  # manda a string vazia

    return icon  # Retorna a opção de ícone


def requirements_check():

    packages = subprocess.check_output(  # Obtém a lista de pacotes instalados usando o pip
        ["pip", "freeze"]).decode().split("\n")
    exists = False  # Inicialmente, considera que o pacote "pyinstaller" não está instalado

    for requisition in packages:  # Verifica se o pacote "pyinstaller" está na lista de pacotes instalados

        if "pyinstaller" in requisition:  # Se o pacote estiver na lista,
            exists = True  # altera a flag exists para True

    if exists == False:  # Se o pacote pyinstaller não estiver instalado,

        subprocess.check_call([  # instala-o usando o pip
            "pip", "install", "pyinstaller"])

        time.sleep(5)  # Pausa por 5 segundos
        os.system("cls")  # Limpa a tela do terminal

        print(  # Exibe uma mensagem de confirmação após instalar o pacote
            "dependências instaladas")


main_run()
