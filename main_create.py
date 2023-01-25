
# Created by KickOfSilver
# https://github.com/KickOfSilver/Create_an_executable

def main_run():
    import os
    import re

    os.system("cls")  # Limpa o terminal
    requirements_check()  # Instala as dependências do pyinstaller

    file = input_name_file()  # Recebe o nome do arquivo principal da aplicação
    console = input_console_read()  # Recebe a opção de mostra o console
    name = input_name_exe()  # Recebe o nome para o executável
    one_file = input_onefile_exe()  # Recebe a opção de combinar os arquivos em um só
    icon_add = add_icon_path()  # Copia o ícone para a pasta do projeto

    # Cria a string de comando para o pyinstaller com base nas opções fornecidas pelo usuário
    comando = f"pyinstaller {console} {name} {icon_add} {one_file} {file}"

    # Substitui dois espaços em branco por um único espaço
    comando = re.sub(r"\s+", " ", comando)
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
            break  # O loop será interrompido

        elif console == "2":  # Se o usuário escolher não,
            console = "--noconsole"  # a opção de console é "--noconsole"
            break  # O loop será interrompido

        else:  # Se o usuário fornecer uma resposta inválida,
            print("Resposta inválida\n")  # imprime uma mensagem de erro

    return console


def input_name_exe():
    import re

    while True:  # Loop infinito até que o usuário forneça um nome válido para o arquivo executável

        program = input("Digite um nome para o arquivo executável"  # Solicita ao usuário um nome para o arquivo executável
                        " ou "
                        "pressione Enter para manter o nome padrão:\n")  # pressione Enter para manter o nome padrão
        print("")

        unallowed = '[@\/:*?"<>|]'  # Caracteres especiais não permitidos

        for character in unallowed:

            if character in program:  # Verifica se o nome do arquivo executável contém algum caractere especial não permitido
                print(  # Exibe uma mensagem de erro se o nome do arquivo contiver algum caractere não permitido:
                    f"Proibido usar este tipo de caractere especial ({character}).")
                continue

        if not program:  # Verifica se o usuário pressionou Enter sem fornecer um nome
            break  # Se sim, o loop será interrompido

        else:  # Se não, adiciona o nome ao comando de criação do executável
            program = re.sub(  # Substitui os espaços no nome por traços
                "[ ]", "-", program)
            program = f"--name={program}"
            break  # O loop será interrompido

    # Retorna o nome do arquivo executável
    return program


def input_onefile_exe():

    while True:

        one_file = input(  # Pergunte ao usuário se ele deseja combinar os arquivos em um único arquivo.
            "Você deseja criar um arquivo executável que inclua todas as dependências do seu aplicativo?\n"
            "1: sim\n" "2: não\n")
        print("")

        if one_file == "1":  # Se o usuário escolher sim,
            one_file = "--onefile"  # a opção de console é "--onefile"
            break  # O loop será interrompido

        elif one_file == "2":  # Se o usuário escolher não,
            one_file = ""  # a opção de one_file é vazia
            break  # O loop será interrompido

        else:  # Se o usuário fornecer uma resposta inválida,
            print("Resposta inválida\n")  # imprime uma mensagem de erro

    return one_file


def add_icon_path():
    import os



    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if "icon.ico" in name:
                print(os.path.join(root, name))

    path_one = "icon.ico"  # Caminho para o ícone
    path_two = "icon/icon.ico"  # Caminho para o ícone

    if os.path.exists(path_one) == True:  # Verifica se o caminho para o ícone existe
        icon = (  # Define as infomaçoes do ícone
            f"--add-data={path_one};. --icon={path_one}")

    elif os.path.exists(path_two) == True:  # verifica o segundo caminho
        icon = (  # Define as infomaçoes do ícone
            f"--add-data={path_two};. --icon={path_two}")

    else:
        while True:  # Se nenhum dos caminhos existir, entra em um loop para solicitar um caminho válido ou ignorar
            print("O ícone não foi encontrado.")
            path_check = input(  # Solicita o caminho do arquivo ícone ou pressionar Enter para ignorar
                "Por favor, forneça o caminho do arquivo ou pressione Enter para ignorar.")

            if os.path.exists(path_check) == True:  # Verifica se o caminho existe
                icon = (  # Define as infomaçoes do ícone
                    f"--add-data={path_check};. --icon={path_check}")
                break  # O loop será interrompido

            if not path_check:  # Se o usuário pressionar Enter, define a opção de ícone como uma string vazia e sai do loop
                icon = ""  # a opção de icon é vazia
                break  # O loop será interrompido

    return icon  # Retorna a opção de ícone


def requirements_check():
    import os
    import time
    import subprocess

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
