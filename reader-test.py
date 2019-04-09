from pathlib import Path
import os

boas_vindas = """


             _________     ____        _________
            /  ______/    / _  |      /  ______/
           /  /___       / /_| |     /  /___
          /  ____/      / ___  |    /  ____/ 
         /  /______    / /   | |   /  /______    ____
        /_________/   /_/    |_|  /_________/   /_  /
                                                 /_/
             __    __        ____        __    __
	    /  |  /  |      / _  |      /  |  / /
	   /   | /   |     / /_| |     /   | / /
	  / /| |/ /| |    / ___  |    / /| |/ /
	 / / |___/ | |   / /   | |   / / |   /
	/_/        |_|  /_/    |_|  /_/  |__/


            Isso aqui é um manipulador de arquivos de texto capaz de criar, adicionar linhas, ler e apagar arquivos.
            Desenvolvido por: niaev
"""

operacoes = """
-------- OPERAÇÕES ------------------------------------------------------
	
	# create() - cria seu arquivo de texto
	# fill()   - escreve no seu arquivo de texto
	# read()   - exibe o conteúdo do seu arquivo de texto
	# delete() - deleta o seu arquivo de texto
	# * aqui não se apaga ou altera linhas específicas do arquivo (ainda)

"""

# exibição da mensagem de introdução do programa
print (boas_vindas + operacoes)

### funcionamento do programa ###

# cria um arquivo de texto
def create():

    # é solicitado o nome do arquivo que será criado
    your_txt = input("Insira aqui o nome do seu novo arquivo: ") + ".txt"
    txt = Path(your_txt)

    # é verificado se esse arquivo tem um nome válido
    if your_txt != ".txt": # se tem
        
        # é verificado se ele ja existe
        if txt.exists(): # se sim

            # é dito ao usuário que esse arquivo já existe
            return f"{your_txt} já existe."

        else: # senão

            # o arquivo é criado
            create = open(your_txt, "x")
            # e é retornado ao usuário que a operação foi realizada com sucesso
            return f"{your_txt} foi criado com sucesso."
        
    else: # se não tem

        # é informado ao usuário que o nome solicitado e inválido
        return "Nome inválido."

        
# escreve em um arquivo de texto
def fill():

    # é solicitado o nome do arquivo que será editado
    your_txt = input("Insira aqui o nome do seu arquivo: ") + ".txt"
    txt = Path(your_txt)

    # é verificado se esse arquivo tem um nome válido
    if your_txt != ".txt": # se tem

        # é verificado se ele ja existe
        if txt.exists(): # se sim

            # é criado um 'escritor' de arquivos
            writer = open(your_txt, "a")
            # e solicitado o que o usuário deseja inserir nesse arquivo
            fill_with = str(input("Digite o que deseja escrever em " + your_txt + ": "))

            # se o usuário digitou alguma coisa
            if fill_with:
                
                # o texto solicitado é inserido no arquivo
                writer.write(fill_with + '\n')
                writer.close()
                # e é retornado ao usuário que a operação foi realizada com sucesso
                return f"{your_txt} foi editado com sucesso."

            # senão
            else:

                # e é retornado ao usuário que nada ocorreu
                return f"{your_txt} não foi alterado."
        
        else: # senão

            # é dito ao usuário que esse arquivo não existe
            return f"{your_txt} não existe."
        
    else: # se não tem

        # é informado ao usuário que o nome solicitado e inválido
        return "Nome inválido."


# exibe o conteudo de um arquivo de texto
def read():

    # é solicitado o nome do arquivo que será lido
    your_txt = input("Insira aqui o nome do seu arquivo: ") + ".txt"
    txt = Path(your_txt)

    # é verificado se esse arquivo tem um nome válido
    if your_txt != ".txt": # se tem
        
        # é verificado se ele ja existe
        if txt.exists(): # se sim

            # é criado um 'leitor' de arquivos
            reader = open(your_txt, "r").read()

            # se o arquivo possui conteúdo
            if reader:

                conteudo = f"""
{your_txt}
-------------------------------------------------------------------------

{str(reader)}
-------------------------------------------------------------------------
                """

                print(conteudo)

                # seu conteúdo é exibido
                return f"{your_txt} foi lido com sucesso!"

            else:

                # é informado ao usuário de que o arquivo não possui conteúdo
                return f"{your_txt} não possui conteúdo"

        else: # senão

            # é dito ao usuário que esse arquivo não existe
            return f"{your_txt} não existe."
        
    else: # se não tem

        # é informado ao usuário que o nome solicitado e inválido
        return "Nome inválido."


# deleta um arquivo de texto
def delete():

    # é solicitado o nome do arquivo que será criado
    your_txt = input("Insira aqui o nome do seu arquivo: ") + ".txt"
    txt = Path(your_txt)

    # é verificado se esse arquivo tem um nome válido
    if your_txt != ".txt": # se tem
        
        # é verificado se ele ja existe
        if txt.exists(): # se sim

            # se o usuário realmente quer deletar o arquivo
            if sn():

                # o arquivo é removido
                os.remove(your_txt)
                # e é informado ao usuário que a operação foi feita com sucesso
                return f"{your_txt} foi removido."

            else: # se o usuário decidiu que não quer remover o arquivo

                # a missão é abortada
                return "Operação cancelada."

        else: # senão

            # é dito ao usuário que esse arquivo não existe
            return f"{your_txt} não existe."
        
    else: # se não tem

        # é informado ao usuário que o nome solicitado e inválido
        return "Nome inválido."

# pergunta de remoção
def sn():

    # essa pergunta e feita ao usuário
    cond = input("Você deseja mesmo apagar esse arquivo? (s/n) ")

    # se o usuário diz que sim
    if cond.lower() == "s":

        # é retornado verdadeiro
        return True

    # se o usuário diz que não
    elif cond.lower() == "n":

        # é retornado falso
        return False

    # se o usuário respondeu outra coisa
    else:

        # a pergunta é feita novamente
        sn()
