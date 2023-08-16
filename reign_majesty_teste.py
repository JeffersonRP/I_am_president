import sys
import os
import time
import random
import time

numeros_escolhidos_primeira_dama = []

numeros_escolhidos_gabriel = []

numeros_escolhidos_pastor_obaid = []


anos_poder = [0]

midia = [50]
seguranca = [50]
dinheiro = [50]
povo = [50]


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def nomes():
    lista_de_nomes = [
        "Miguel",
        "Arthur",
        "Adailton",
        "Eduardo",
        "Renan",
        "Fernando",
        "Carlos",
        "Alberto",
        "Rodrigo",
        "Moisés",
        "Jefferson",
        "Jonatas",
        "Jackson",
        "Bruno",
        "Inácio",
        "Dante",
        "Túlio",
        "Ronaldo",
        "João",
        "Juscelino",
        "Paulo",
        "Reinaldo",
        "Cabral",
        "Janilson",
        "Jair",
        "Michel",
        "Fernando Henrique",
        "Itamar",
        "José",
        "Tancredo",
        "Roussef"
    ]
    nomes_aleatorio = random.choice(lista_de_nomes)
    # Aqui é para mandar o nome para o texto de boas vindas
    return nomes_aleatorio


# Aqui são as boas vindas ao novo presidente
def boas_vindas_presidente():
    nomes_aleatorio = nomes()
    # lista_de_oi = [
    #     f"Parabéns pela candidatura presidente {nomes_aleatorio}, todos estão empolgados com sua candidatura",
    #     f"Uma vitória nos votos presidente {nomes_aleatorio}, espero que seja bom de jogo de cintura pois a cidade está passando por mudanças",
    #     f"Alguns não concordam com os numeros de votos presidente {nomes_aleatorio}, as coisas não estão nada faceis, muita corrupção envolvida, acredito que você irá nos salvar.",
    #     "Em seu primeiro dia, o governo se encontra dividido entre os poderes.",
    # ]


    lista_de_oi = [
        f"Parabéns pela candidatura, todos estão empolgados com sua candidatura.",
        f"Uma vitória nos votos, espero que seja bom de jogo de cintura pois a cidade está passando por mudanças.",
        f"Alguns não concordam com os números de votos, as coisas não estão nada fáceis, muita corrupção envolvida, acredito que você irá nos salvar.",
        "Em seu primeiro dia, o governo se encontra dividido entre os poderes.",
        "Bem-vindo ao cargo. O país enfrenta sérios desafios econômicos e sociais que exigirão liderança forte.",
        "A nação está cética em relação ao governo, precisamos de resultados concretos.",
        "Com a posse do novo presidente, as expectativas são altas, mas o cenário é de dificuldades e desconfiança.",
        "O país aguarda ações concretas do governo para enfrentar os problemas que nos afligem.",
        "O momento é delicado e requer decisões difíceis para tirar o país da crise.",
        "Após a posse, surgem desafios políticos que testarão a habilidade da liderança.",
        "O país enfrenta incertezas e instabilidade política no início do mandato.",
        "A situação econômica é preocupante e exigirá medidas urgentes.",
        "Esperamos que o novo governo encontre soluções para os problemas que seu antecessor não conseguiu resolver.",
        "Com a posse, o novo governo assume a responsabilidade por questões complexas que precisarão de soluções rápidas e efetivas.",
    ]

    while True:
        try:
            oi_comum_aleatorio = random.choice(lista_de_oi)
            print(oi_comum_aleatorio)
            print("[1] Passe")
            print("[2] Passe")
            continuar = int(input("Escolha: "))
            if continuar == 1 or continuar == 2:
                break

        except ValueError:
            print("Tente escolher algo entre 1 e 2")

    return nomes_aleatorio

def gerar_numero_unico_gabriel():
    numero = random.randint(1, 10)
    while numero in numeros_escolhidos_gabriel:
        numero = random.randint(1, 10)
    numeros_escolhidos_gabriel.append(numero)
    return numero

def gerar_numero_unico_primeira_dama():
    numero = random.randint(1, 10)
    while numero in numeros_escolhidos_primeira_dama:
        numero = random.randint(1, 10)
    numeros_escolhidos_primeira_dama.append(numero)
    return numero

def gerar_numero_unico_pastor():
    numero = random.randint(1, 10)
    while numero in numeros_escolhidos_pastor_obaid:
        numero = random.randint(1, 10)
    numeros_escolhidos_pastor_obaid.append(numero)
    return numero


# personagens
def gabriel_search_ever(dinheiro, midia, povo, seguranca, nome_presidente):
    
    

    while True:
        qualquer_uma_gabriel =gerar_numero_unico_gabriel()


        # Pergunta 1
        if qualquer_uma_gabriel == 1:    
            
            while True:
                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')

                           
                print(f"\nDinheiro {dinheiro[0]} | Midia {midia[0]} | Povo {povo[0]} | Seguranca {seguranca[0]}\n")
                
                print(f"[Gabriel - Representante da Search Ever]\nOlá presidente gostariamos de conversar sobre seu apoio com a construção do novo empreendimento!")
                print("[1] Como posso ajudar?")
                print("[2] Nem pensar")
                search_ever_pergunta = int(input("Escolha: "))
                mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                if search_ever_pergunta == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')     

                           
                    print(f"\nDinheiro {dinheiro[0]} | Midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"[Gabriel - Representante da Search Ever]\nÉ muito simples senhor, apenas precisamos de algumas assinaturas e você recebe um presente, ok?")
                    print("[1] Conta comigo           | Segurança //   Povo ///   Dinheiro ///")
                    print("[2] Não me parece prudente | Segurança //   Povo ///")
                    search_ever_pergunta2 = int(input("Escolha: "))

                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                    if search_ever_pergunta2 == 1:
                        anos_poder[0] += 1

                        seguranca[0] += 10
                        povo[0] -= 15
                        dinheiro[0] += 15
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    if search_ever_pergunta2 == 2:
                        anos_poder[0] += 1

                        seguranca[0] -= 10
                        povo[0] += 15
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                if search_ever_pergunta == 2:
                    anos_poder[0] += 1

                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

        # Pergunta 2
        if qualquer_uma_gabriel == 2:
            # Pergunta 2
            while True:         
                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')                
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nPresidente, oque acha de diminuir os impostos de grandes exportações?")
                print("[1] Será um bom investimento        | Povo ///  Dinheiro ///")
                print("[2] Isso pode afetar os mais pobres | Povo ///  Dinheiro ///")
                search_ever_pergunta4 = int(input("Escolha: "))
                

                if search_ever_pergunta4 == 1:
                    anos_poder[0] += 1
                    
                    povo[0] -= 15
                    dinheiro[0] += 15
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

                if search_ever_pergunta4 == 2:
                    anos_poder[0] += 1

                    povo[0] += 15
                    dinheiro[0] -= 15
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

        # pergunta 3
        if qualquer_uma_gabriel == 3:
            # Pergunta 2
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')                    
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nO que acha de pesquisarmos petróleo no nosso país?")
                print("[1] Sim, será a reviravolta do país   | Povo / Seguranca /  Dinheiro //")
                print("[2] Petróleo não vale a pena          | Povo / Dinheiro /")
                search_ever_pergunta = int(input("Escolha: "))
                mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                if search_ever_pergunta == 1:
                    clear_terminal()
                    anos_poder[0] += 1

                    povo[0] += 5
                    seguranca[0] += 5
                    dinheiro[0] -= 10
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"[noticia]\nAnuncios de vagas para pesquisadores de solo.")
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

                if search_ever_pergunta == 2:
                    anos_poder[0] += 1

                    povo[0] -= 5
                    dinheiro[0] += 5
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

        # pergunta 4
        if qualquer_uma_gabriel == 4:
            while True:
                clear_terminal()
                print(f'No poder: {anos_poder[0]}')
                print(nome_presidente)
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nAcho que podemos criar coragem para os foguetes!")
                print("[1] Bora para a lua")
                print("[2] Pra que?        | Midia /// Dinheiro ///")
                search_ever_pergunta = int(input("Escolha: "))



                if search_ever_pergunta == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print("[Gabriel - Representante da Search Ever]\nIr a lua? Calma, não precisamos ir tão longe.")
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    print("[1] Então um satélite   | Midia ///  Segurança ///  Dinheiro ///")
                    print("[2] Desanimei           | Midia ///  Dinheiro ///")                        
                    search_ever_pergunta1 = int(input('Escolha: '))

                    if search_ever_pergunta1 == 1:
                        clear_terminal()
                        anos_poder[0] += 1

                        midia[0] += 15
                        seguranca[0] += 15
                        dinheiro[0] -= 15
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print("[noticia]\nSatélite governamental em órbita.")
                        print("[1] Passe")
                        print("[2] Passe")
                        search_ever_pergunta111 = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    if search_ever_pergunta1 == 2:
                        anos_poder[0] += 1

                        midia[0] -= 15
                        dinheiro[0] += 15
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                if search_ever_pergunta == 2:
                    anos_poder[0] += 1

                    midia[0] -= 15
                    dinheiro[0] += 15
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

        # pergunta 5
        if qualquer_uma_gabriel == 5:
            while True:
                
                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nQue tal investir em industrias para que haja mais empregos")
                print("[1] Mais empregos            |  Midia /  Dinheiro ///  Povo //")
                print("[2] Naah, o país está ótimo  |  Povo //")
                search_ever_pergunta = int(input("Escolha: "))




                if search_ever_pergunta == 1:
                    clear_terminal()
                    anos_poder[0] += 1

                    midia[0] += 5
                    povo[0] += 10
                    dinheiro[0] -= 15
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print("[noticia]\nMais jovens iniciam seu primeiro emprego.")
                    print("[1] Passe")
                    print("[2] Passe")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

                if search_ever_pergunta == 2:
                    clear_terminal()
                    anos_poder[0] += 1

                    povo[0] -= 10
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print("[noticia]\nO desemprego bate um novo recorde esse ano.")
                    print("[1] Passe")
                    print("[2] Passe")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break



        # pergunta 6
        if qualquer_uma_gabriel == 6:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nO que acha de ganhar um barco só seu?")
                print("[1] Ah eu gostaria sim     |  ")
                print("[2] Não preciso no momento | ")
                search_ever_pergunta = int(input("Escolha: "))




                if search_ever_pergunta == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Gabriel - Representante da Search Ever]\nMuito bem é seu, apenas assine para que dimnua algumas porcentagens de juros das nossas dividas")
                    print("[1] Eu assino me de logo meu barco  |  Segurança //  Midia  /  Povo /")
                    print("[2] Acho que isso é corrupção       |  Segurança //  Povo //")
                    search_ever_pergunta1 = int(input("Escolha: "))

                    if search_ever_pergunta1 == 1:
                        clear_terminal()
                        anos_poder[0] += 1

                        seguranca[0] += 10
                        midia[0] += 5
                        povo[0] -= 5
                        print(f"[Você tem um barco de luxo na marina]")
                        print("[1] Passe")
                        print("[2] Passe")
                        search_ever_pergunta11 = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    if search_ever_pergunta1 == 2:
                        anos_poder[0] += 1

                        seguranca[0] -= 10
                        povo[0] += 5
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                if search_ever_pergunta == 2:
                    anos_poder[0] += 1

                    seguranca[0] -= 10
                    povo[0] += 5
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break





        # pergunta 7
        if qualquer_uma_gabriel == 7:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | Midia {midia[0]} | Povo {povo[0]} | Seguranca {seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nGostaria que retirasse uns orfanatos da rua central, eu quero criar um grande shopping")
                print("[1] Crianças gostam de shopping    |  Povo ///  Dinheiro ///  Midia //")
                print("[2] Deixe como estão os orfanatos  |  Povo ///  Dinheiro /")
                search_ever_pergunta = int(input("Escolha: "))


                if search_ever_pergunta == 1:
                    clear_terminal()
                    anos_poder[0] += 1

                    povo[0] -= 15
                    dinheiro[0] += 15
                    midia[0] -= 10
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | Midia {midia[0]} | Povo {povo[0]} | Seguranca {seguranca[0]}\n")
                    print("[Noticia]\nO shopping atrai muitos visitantes e é um dos mais lindos, o unico problema são algumas crianças na calçada.")
                    print("[1] Passe")
                    print("[2] Passe")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break


                if search_ever_pergunta == 2:
                    clear_terminal()
                    anos_poder[0] += 1

                    povo[0] += 15
                    dinheiro[0] -= 5
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print("[Noticia]\nPresidente continua ignorando cituação precária dos orfanatos")
                    print("[1] Passe")
                    print("[2] Passe")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break



        # pergunta 8
        if qualquer_uma_gabriel == 8:
            while True:
                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nPresidente o senhor é muito importante, só falta dinheiro, assine esse papel sem muita importancia e essa mala é sua.")
                print("[1] O que tem escrito nesse contrato?  |  ")
                print("[2] Estou curioso com a mala           |  Povo /// Midia /// Dinheiro ///")
                search_ever_pergunta = int(input("Escolha: "))




                if search_ever_pergunta == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"[Gabriel - Representante da Search Ever]\nÉ uma permissão para a criação de uma mina de carvão no interior da capital.")
                    print("[1] Pode esquecer, nada disso          |  Povo ///  Midia //   Dinheiro //")
                    print("[2] Ah tudo bem, minas são importantes |  Povo ///  Midia ///  Dinheiro ///")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)



                    if search_ever_pergunta1 == 1:
                        clear_terminal()
                        anos_poder[0] += 1

                        povo[0] += 15
                        midia[0] += 10
                        dinheiro[0] -= 10
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca {seguranca[0]}\n")
                        print(f'[Noticia]\nPresidente nega dinheiro sujo de acionistas e preserva o interior da capital')
                        search_ever_pergunta1 = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    if search_ever_pergunta1 == 2:
                        clear_terminal()
                        anos_poder[0] += 1

                        povo[0] -= 15
                        midia[0] -= 15
                        dinheiro[0] += 15
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print("[noticia]\nUma mina de carvão é escavada no interior da capital, milhares ficam doentes por intoxicação de metais pesados")
                        search_ever_pergunta1 = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break








                if search_ever_pergunta == 2:
                    clear_terminal()
                    anos_poder[0] += 1

                    povo[0] -= 15
                    midia[0] -= 15
                    dinheiro[0] += 15
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print("[Noticia]\nUma mina de carvão é escavada no interior da capital, milhares ficam doentes por intoxicação de metais pesados")
                    print("[1] Passe")
                    print("[2] Passe")
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break



        # pergunta 9
        if qualquer_uma_gabriel == 9:
            while True:
                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nOlá presidente que tal revogar lei de redução dos preços dos combustiveis?")
                print("[1] Acho que um pouco não tem problema mesmo |  Povo //  Midia /  Dinheiro /")
                print("[2] Nada disso                               |  Midia /  Dinheiro /")
                search_ever_pergunta = int(input("Escolha: "))




                if search_ever_pergunta == 1:
                    clear_terminal()
                    anos_poder[0] += 1

                    povo[0] -= 10
                    midia[0] -= 5
                    dinheiro[0] += 5
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Noticia]\nCidadãos fazem manifestação contra o aumentos dos combustiveis")
                    print("[1] Passe")
                    print("[2] Passe")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break






                if search_ever_pergunta == 2:
                    clear_terminal()
                    anos_poder[0] += 1
                    
                    midia[0] += 5
                    dinheiro[0] -= 5
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print("[Noticia]\nPresidente mantêm o preço dos combustiveis, povo reclama por falta de mudanças.")
                    print("[1] Passe")
                    print("[2] Passe")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break




        # pergunta 10
        if qualquer_uma_gabriel == 10:
            while True:
                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Gabriel - Representante da Search Ever]\nPresidente que tal investir em nossos shows beneficentes?")
                print("[1] Seria ótimo para os artistas  |  Povo //  Midia ///  Dinheiro //")
                print("[2] Agora não estou afim          |  Dinheiro //")
                search_ever_pergunta = int(input("Escolha: "))




                if search_ever_pergunta == 1:
                    clear_terminal()
                    anos_poder[0] += 1

                    povo[0] += 10
                    midia[0] += 15
                    dinheiro[0] -= 10
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Noticia]\nShows são a sensação das capitais do país")
                    print("[1] Passe")
                    print("[2] Passe")
                    search_ever_pergunta1 = int(input("Escolha: "))
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break






                if search_ever_pergunta == 2:
                    clear_terminal()
                    anos_poder[0] += 1

                    dinheiro[0] += 10
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break



        # Esse break é para as perguntas retornarem ao inicio
        break

def primeira_dama(dinheiro, midia, povo, seguranca, nome_presidente):
    while True:
            qualquer_uma_primeira_dama = gerar_numero_unico_primeira_dama()


            # Pergunta 1
            if qualquer_uma_primeira_dama == 1:
                while True:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')  
                    print(f"\nDinheiro {dinheiro[0]} | Midia {midia[0]} | Povo {povo[0]} | Seguranca {seguranca[0]}\n")
                    print(f"[Primeira Dama]\nOi meu amor, você pode me emprestar o jatinho presidencial?")
                    print("[1] Claro, tudo para minha esposinha  |  Povo /  Midia /  Dinheiro //")
                    print("[2] Não, é errado para usos bobos     |  Povo /  Midia //")
                    primeira_dama_pergunta = int(input("Escolha: "))

                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                    if primeira_dama_pergunta == 1:
                        clear_terminal()
                        

                        povo[0] += 5
                        midia[0] += 5
                        dinheiro[0] -= 10
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')  
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f"[Noticia]\nPrimeira Dama é flagrada utilizando o força aérea 1 para viajar até o exterior, internautas afirmam que ela está linda")
                        print('[1] Passe')
                        print('[2] Passe')
                        primeira_dama_pergunta1 = int(input("Escolha: "))

                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break


                    if primeira_dama_pergunta == 2:
                        

                        povo[0] -= 5
                        midia[0] -= 10
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')  
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f"[Noticia]\nPrimeira Dama posta na internet que está sendo mal tratada pelo marido")
                        anos_poder[0] += 1
                        print('[1] Passe')
                        print('[2] Passe')
                        search_ever_pergunta2 = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

            # Pergunta 2
            if qualquer_uma_primeira_dama == 2:
                # Pergunta 2
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')  
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nVocê sabe que sou apaixonada por jardinagem! Será que podemos transformar a casa em um imenso jardim botânico? Vai ser lindo e ecológico!")
                        print("[1] Parece bom, gosto de verde   |  Povo //  Dinheiro ///")
                        print("[2] Talvez seja melhor não       |  Dinheiro /")
                        search_ever_pergunta = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                        if search_ever_pergunta == 1:
                            clear_terminal()
                            anos_poder[0] += 1

                            povo[0] -= 10
                            dinheiro[0] -= 15
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')  
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print('[Noticia] O resultado não ficou bom, acharam um disperdicio dos fundos')
                            print('[1] Passe')
                            print('[2] Passe')
                            primeira_dama_pergunta1 = int(input("Escolha: "))
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break

                        if search_ever_pergunta == 2:
                            anos_poder[0] += 1

                            dinheiro[0] -= 5
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break

                    except ValueError:
                        print("Não está certo")

            # pergunta 3
            if qualquer_uma_primeira_dama == 3:
                # Pergunta 2
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print('No poder:',anos_poder)
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nTalvez tenha sido o whiskey, mas você está mais gatinho hoje!")
                        print("[1] Vem aqui meu doce de leite  |  ")
                        print("[2] Estou com sono")
                        search_ever_pergunta = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                        if search_ever_pergunta == 1:
                            qualquer_uma_primeira_dama_gravidez = random.randint(1,2)


                            if qualquer_uma_primeira_dama_gravidez == 1:
                                clear_terminal()
                                anos_poder[0] += 1

                                print(nome_presidente)
                                print(f'No poder: {anos_poder[0]}')
                                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                                print(f"[Noticia]\nA primeira Dama anuncia sua gravidez")
                                print('[1] Passe')
                                print('[2] Passe')
                                primeira_dama_pergunta1 = int(input("Escolha: "))
                                mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                                break


                            if qualquer_uma_primeira_dama_gravidez == 2:
                                clear_terminal()
                                anos_poder[0] += 1

                                print(nome_presidente)
                                print(f'No poder: {anos_poder[0]}')
                                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                                print(f"[Noticia]\nA primeira Dama e o Presidente não tem filhos, talvez não gostem de crianças!")
                                print('[1] Passe')
                                print('[2] Passe')
                                primeira_dama_pergunta1 = int(input("Escolha: "))
                                mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                                break                                


                        if search_ever_pergunta == 2:
                            anos_poder[0] += 1

                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break

                    except ValueError:
                        print("Não está certo")

            # pergunta 4
            if qualquer_uma_primeira_dama == 4:
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f"[Primeira Dama]\nO que você acha de organizarmos um baile temático na Casa Branca? Posso sugerir 'Traje Formal de Fazendeiro'? Seria uma visão e tanto!")
                        print("[1] Talvez apostar no terno mesmo  |  Segurança //  Midia //")
                        print("[2] Tem razão, humildade           |  Midia ///  Segurança ///  Dinheiro ///")
                        search_ever_pergunta = int(input("Escolha: "))



                        if search_ever_pergunta == 1:
                            clear_terminal()
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            seguranca[0] -= 10
                            midia[0] -= 10
                            print("[Noticia]\nO baile é constrangedor, você não tem assunto, todos ficam quietos e acaba cedo.")
                            print('[1] Passe')                   
                            print('[2] Passe')                   
                            search_ever_pergunta1 = int(input('Escolha: '))
                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente) 
                            break

                        if search_ever_pergunta == 2:
                            clear_terminal()
                            midia[0] += 15
                            seguranca[0] += 15
                            dinheiro[0] -= 15
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print("[Noticia]\nSuas roupas trazem uma critica social a todos, os politicos e poderosos ficam impressionados.")
                            print("[1] Passe")
                            print("[2] Passe")
                            search_ever_pergunta = int(input("Escolha: "))
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            anos_poder[0] += 1
                            break

                            
                    except ValueError:
                        print("Não está certo")

            # pergunta 5
            if qualquer_uma_primeira_dama == 5:
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nMeu amorzinho, o que acha de criar uma escola comunitária de padeiros para as crinaças pobres?")
                        print("[1] Ta maluca?       |  Midia ///  Dinheiro /")
                        print("[2] Você é um gênio  |  Midia ///  Povo //  Segurança /  Dinheiro ///")
                        search_ever_pergunta = int(input("Escolha: "))




                        if search_ever_pergunta == 1:
                            clear_terminal()
                            midia[0] -= 15
                            dinheiro[0] += 5
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print("[Noticia]\nFalta de mudanças.")
                            print("[1] Passe")
                            print("[2] Passe")
                            search_ever_pergunta1 = int(input("Escolha: "))
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            anos_poder[0] += 1
                            break

                        if search_ever_pergunta == 2:
                            clear_terminal()
                            midia[0] += 15
                            povo[0] += 10
                            seguranca[0] += 5
                            dinheiro[0] -= 15
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print("[Noticia]\nCriou uma escola comunitaria para jovens.")
                            print("[1] Passe")
                            print("[2] Passe")
                            search_ever_pergunta1 = int(input("Escolha: "))
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            anos_poder[0] += 1
                            break


                    except ValueError:
                        print("Não está certo")

            #pergunta 6
            if qualquer_uma_primeira_dama == 6:
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nAmorzinho do coração, que tal criarmos mais centros gratuitos de comida?")
                        print("[1] As pessoas estão mesmo magras  |  Povo ///")
                        print("[2] Não precisa, obesidade faz mal |  Povo ///")
                        search_ever_pergunta = int(input("Escolha: "))




                        if search_ever_pergunta == 1:
                            clear_terminal()
                            povo[0] += 15

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break

                        if search_ever_pergunta == 2:
                            clear_terminal()
                            povo[0] -= 15

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                    except ValueError:
                        print("Não está certo")

            # pergunta 7
            if qualquer_uma_primeira_dama == 7:
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nAmor, eu preciso de roupas novas, sofás, tudo novo")
                        print("[1] Escolha o que quiser  |  Dinheiro //  Midia //")
                        print("[2] Agora não             |  Dinheiro //  Midia //")
                        search_ever_pergunta = int(input("Escolha: "))




                        if search_ever_pergunta == 1:
                            clear_terminal()
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            dinheiro[0] -= 10
                            midia[0] += 10
                            print("[Noticia]\nA fabulosa primeira Dama apresenta a nova decoração da casa presidencial")
                            print("[1] Passe")
                            print("[2] Passe")
                            search_ever_pergunta = int(input("Escolha: "))

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                        if search_ever_pergunta == 2:
                            clear_terminal()
                            dinheiro[0] += 10
                            midia[0] -= 10

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                    except ValueError:
                        print("Não está certo")



            # pergunta 8
            if qualquer_uma_primeira_dama == 8:
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nAmorzinho quero um carrinho novo, estava vendo um baratinho, só tem dois lugares")
                        print("[1] Você precisa de um carro novo mesmo  |  Dinheiro ///  Midia /")
                        print("[2] Isso é luxo demais                   |  Dinheiro /  Midia //  Povo // ")
                        search_ever_pergunta = int(input("Escolha: "))


                        if search_ever_pergunta == 1:
                            clear_terminal()
                            dinheiro[0] -= 15
                            midia[0] -= 5
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print(f"[Primeira Dama]\nDesculpinha, bati o carro na vidraça da cafeteria.")
                            print('[1] Passe')
                            print('[2] Passe')
                            primeira_dama_pergunta1 = int(input("Escolha: "))

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                        if search_ever_pergunta == 2:
                            clear_terminal()
                            povo[0] -= 10
                            midia[0] += 10
                            dinheiro[0] -= 5
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print(f"[Noticia]\nPrimeira Dama é flagrada passeando de helicóptero")
                            print("[1] Passe")
                            print("[2] Passe")
                            search_ever_pergunta1 = int(input("Escolha: "))

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                    except ValueError:
                        print("Não está certo")

            # pergunta 9
            if qualquer_uma_primeira_dama == 9:
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nAmor por que você não me engravida, não gosta de mim?")
                        print("[1] Não quero filhos agora    |  Midia  /")
                        print("[2] Estou tentando juro       |  Midia  /")
                        search_ever_pergunta = int(input("Escolha: "))




                        if search_ever_pergunta == 1:
                            clear_terminal()
                            midia[0] -= 5
                            
                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break






                        if search_ever_pergunta == 2:
                            clear_terminal()
                            midia[0] += 5

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                    except ValueError:
                        print("Não está certo")

            # pergunta 10
            if qualquer_uma_primeira_dama == 10:
                while True:
                    try:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                        print(f"[Primeira Dama]\nAmor o que acha de andarmos soltos no labirinto do quintal só por diversão?")
                        print("[1] Claro")
                        print("[2] Não me sinto bem")
                        search_ever_pergunta = int(input("Escolha: "))




                        if search_ever_pergunta == 1:
                            clear_terminal()
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print('Está de frente a dois corredores de arbustos')
                            print("[1] Passe")
                            print("[2] Passe")
                            search_ever_pergunta1 = int(input("Escolha: "))

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break






                        if search_ever_pergunta == 2:
                            clear_terminal()
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                            print('Um chafaríz enorme no meio das arvores')
                            print("[1] Passe")
                            print("[2] Passe")
                            search_ever_pergunta = int(input("Escolha: "))
                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                    except ValueError:
                        print("Não está certo")


            # Esse break é para as perguntas retornarem ao inicio
            break

def pastor_obaid(dinheiro, midia, povo, seguranca, nome_presidente):
    while True:
        qualquer_uma_pastor_obaid = gerar_numero_unico_pastor()

        # Pergunta 1
        if qualquer_uma_pastor_obaid == 1:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')  
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nPaz do senhor presidente, oque acha de construir templos com dinheiro público?.")
                print("[1] Parece bom   |  Midia  //  Povo ///  Dinheiro ///")
                print("[2] Nem pensar   |  Povo //  Dinheiro ///")
        
                escolha = int(input("Escolha: "))

                if escolha == 1:
                    clear_terminal()
                    midia[0] -= 10
                    povo[0] += 15
                    dinheiro[0] -= 15
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')  
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Noticia]\nPresidente disperdiça dinheiro com igrejas que não terminam as obras.")
                    print("[1] Passar.")
                    print("[2] Passar.")
                    escolha1 = int(input("Escolha: "))
                    if escolha1 == 1 or 2:

                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    

                if escolha == 2:
                    povo[0] -= 10
                    dinheiro[0] += 15

                    anos_poder[0] += 1
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                
                    break

        # Pergunta 2
        if qualquer_uma_pastor_obaid == 2:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}') 
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print(f"[Pastor Obaid]\nPaz do senhor, eu vi que estão querendo colocar impostos nas igrejas, você não concorda com isso, certo?")
                print("[1] Impostos em tudo  |  Midia ///  Povo //  Dinheiro //")
                print("[2] Eu não            |  Midia ///  Povo //  Dinheiro //")
        
                escolha = int(input("Escolha: "))

                if escolha == 1:
                    clear_terminal()
                    midia[0] += 15
                    povo[0] -= 10
                    dinheiro[0] += 10
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}') 
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Noticia]\nPresidente taxa os templos, religiosos ficam enfurecidos.")
                    print("[1] Passar.")
                    print("[2] Passar.")
                    escolha1 = int(input("Escolha: "))
                    if escolha1 == 1 or 2:

                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    

                if escolha == 2:
                    clear_terminal()
                    midia[0] -= 15
                    povo[0] += 10
                    dinheiro[0] -= 10
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}') 
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Noticia]\nIgreja do centro é o terceiro maior PIB do país.")
                    print("[1] Passar.")
                    print("[2] Passar.")
                    escolha1 = int(input("Escolha: "))
                    if escolha1 == 1 or 2:

                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                
                        break

        # Pergunta 3
        if qualquer_uma_pastor_obaid == 3:
            while True:

                clear_terminal()
                print('No poder:',anos_poder)
                print(nome_presidente)
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nPaz do senhor, presidente o que acha de criarmos o auxílio religioso")
                print("[1] Auxilio é sempre bom  |  Povo  //  Dinheiro //  Midia ///")
                print("[2] Melhor economizar     |  Povo  //  Dinheiro //  Midia ///")
        
                escolha = int(input("Escolha: "))

                if escolha == 1:
                    clear_terminal()
                    povo[0] += 10
                    dinheiro[0] -= 10
                    midia[0] -= 15
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}') 
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Noticia]\nPastores e diaconos esbanjam de dinheiro público em concessionárias de luxo")
                    print("[1] Passar.")
                    print("[2] Passar.")
                    escolha1 = int(input("Escolha: "))
                    anos_poder[0] += 1
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break



                if escolha == 2:
                    midia[0] += 15
                    povo[0] -= 10
                    dinheiro[0] += 10
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}') 
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Noticia]\nPresidente é contra gastos do governo para templos, religiosos se sentem atacados")
                    print("[1] Passar.")
                    print("[2] Passar.")
                    escolha1 = int(input("Escolha: "))
                    anos_poder[0] += 1
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

        # Pergunta 4
        if qualquer_uma_pastor_obaid == 4:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nEstá na paz irmão presidente?")
                print("[1] Amém             |  Midia /  Segurança //  Dinheiro /")
                print("[2] Não estou na paz |  ")
        
                escolha = int(input("Escolha: "))

                if escolha == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                    print(f"[Pastor Obaid]\nPreciso de um cargo político, mas um bem tranquilo")
                    print("[1] Tudo bem, lhe darei um cargo  |  Midia /  Segurança //  Dinheiro /")
                    print("[2] Não, isso é errado            |  Midia /  Segurança //  Dinheiro /")
                    escolha1 = int(input("Escolha: "))

                    if escolha1 == 1:
                        midia[0] -= 5
                        seguranca[0] += 10
                        dinheiro[0] += 5
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | Midia {midia[0]} | Povo {povo[0]} | Seguranca {seguranca[0]}\n")
                        print(f'[Noticia]\nPresidente entrega cargos para seus amigos')
                        print('[1] Passe')
                        print('[2] Passe')
                        escolha11 = int(input("Escolha: "))
                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    if escolha1 == 2:
                        midia[0] += 5
                        seguranca[0] -= 10
                        dinheiro[0] -= 5
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f'[Noticia]\nPresidente ofende pastores, seria ele intolerânte religioso?')
                        print('[1] Passe')
                        print('[2] Passe')
                        escolha11 = int(input("Escolha: "))
                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break



                if escolha == 2:
                    midia[0] -= 5
                    seguranca[0] -= 10
                    dinheiro[0] -= 5

                    anos_poder[0] += 1
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break

        # Pergunta 5
        if qualquer_uma_pastor_obaid == 5:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nIrmão?")
                print("[1] Na paz irmão!")
                print("[2] Não sou seu irmão")
        
                escolha = int(input("Escolha: "))

                # Escolha 1
                if escolha == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"[Pastor Obaid]\nQuero falar de você durante os meus cultos, mas preciso de um pequeno dizmo")
                    print("[1] Igreja vazia não para em pé  |  Midia //  Segurança //  Dinheiro ///  Povo ///")
                    print("[2] Eu não preciso disso         |  Midia /  Segurança //  Dinheiro ///  Povo ///")
                    escolha1 = int(input("Escolha: "))

                    if escolha1 == 1:
                        clear_terminal()
                        midia[0] += 10
                        seguranca[0] += 10
                        dinheiro[0] -= 15
                        povo[0] += 15
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | Midia {midia[0]} | Povo {povo[0]} | Seguranca {seguranca[0]}\n")
                        print(f'[Noticia]\nReligiosos passam a apoiar muito o governo')
                        print('[1] Passe')
                        print('[2] Passe')
                        escolha11 = int(input("Escolha: "))
                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    if escolha1 == 2:
                        clear_terminal()
                        midia[0] += 5
                        seguranca[0] -= 10
                        dinheiro[0] += 15
                        povo[0] -= 15
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f'[Noticia]\nPresidente ofende pastores, seria ele intolerânte religioso?')
                        print('[1] Passe')
                        print('[2] Passe')
                        escolha11 = int(input("Escolha: "))
                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break


                # escolha 2 

                if escolha == 2:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"[Pastor Obaid]\nO senhor está na carne?")
                    print("[1] Claro que não      |  Povo /  Dinheiro /")
                    print("[2] Tanto faz para mim |  Povo /  Dinheiro /")
                    escolha11 = int(input("Escolha: "))

                    if escolha11 == 1:
                        povo[0] += 5
                        dinheiro[0] += 5

                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                    if escolha11 == 2:
                        povo[0] -= 5
                        dinheiro[0] -= 5

                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                
                break

        # Pergunta 6
        if qualquer_uma_pastor_obaid == 6:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nA igreja precisa aparecer mais, o que acha de um jantar entre os politícos e pastores?")
                print("[1] Sim, conhecer mais de sua religião  |  Segurança //")
                print("[2] Não obrigado, já, jantei em casa    |  Segurança //")
        
                escolha = int(input("Escolha: "))

                # Escolha 1
                if escolha == 1:
                    clear_terminal()
                    print(nome_presidente)
                    anos_poder[0] += 1

                    seguranca[0] += 10
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"[Pastor Obaid]\nQuero falar de você durante os meus cultos, mas preciso de um pequeno dizmo")
                    print("[1] Igreja vazia não para em pé")
                    print("[2] Eu não preciso disso")
                    escolha1 = int(input("Escolha: "))
                    break


                # escolha 2 

                if escolha == 2:
                    clear_terminal()
                    print(nome_presidente)
                    anos_poder[0] += 1
                    
                    seguranca[0] -= 10
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"[Pastor Obaid]\nO senhor está na carne?")
                    print("[1] Claro que não")
                    print("[2] Tanto faz para mim")
                    escolha11 = int(input("Escolha: "))
                    break

    

                break

        #pergunta 7
        if qualquer_uma_pastor_obaid == 7:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nQue a paz do senhor esteja contigo, pode pagar o dizmo presidente?")
                print("[1] Sim   |  Povo  //  Dinheiro //  Segurança /")
                print("[2] Não   |  Povo  //  Dinheiro //  Segurança /")
        
                escolha = int(input("Escolha: "))

                # Escolha 1
                if escolha == 1:
                    povo[0] += 10
                    dinheiro[0] -= 10
                    seguranca[0] += 5

                    anos_poder[0] += 1


                # escolha 2 
                if escolha == 2:
                    povo[0] -= 10
                    dinheiro[0] += 10
                    seguranca[0] -= 5

                    anos_poder[0] += 1
                
                break

        # Pergunta 8
        if qualquer_uma_pastor_obaid == 8:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nDeus me falou para lhe pedir algo meu presidente")
                print("[1] Me fale")
                print("[2] Ah me poupe  |  Midia /  Dinheiro //  Povo //")
                escolha = int(input("Escolha: "))

                # Escolha 1
                if escolha == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"[Pastor Obaid]\nPor favor, uma lei contra as casas de apostas, são pecaminosos")
                    print("[1] Tem razão              |  Midia  //  Dinheiro ///  Povo //  Segurança /")
                    print("[2] Deixem eles apostarem  |  Midia /  Dinheiro //  Povo //")
                    escolha1 = int(input("Escolha: "))

                    if escolha1 == 1:
                        clear_terminal()
                        midia[0] -= 5
                        dinheiro[0] -= 15
                        povo[0] += 10
                        seguranca[0] += 5
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f"[Noticia]\nPresidente criminaliza apostas")
                        print('[1] Passe')
                        print('[2] Passe')
                        escolha11 = int(input("Escolha: "))
                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break

                    if escolha1 == 2:
                        clear_terminal()
                        midia[0] += 5
                        dinheiro[0] -= 10
                        povo[0] -= 10
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f"[Pastor Obaid]\nVocê se diverte com os brinquedos do inferno")
                        print('[1] Passe')
                        print('[2] Passe')
                        escolha11 = int(input("Escolha: "))
                        anos_poder[0] += 1
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                        break


                # escolha 2 

                if escolha == 2:
                    povo[0] -= 5
                    seguranca[0] -= 10
                    
                    anos_poder[0] += 1
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                break

        # Pergunta 9
        if qualquer_uma_pastor_obaid == 9:
            while True:

                clear_terminal()
                print(nome_presidente)
                print(f'No poder: {anos_poder[0]}')
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nQuer ir a um evento beneficente da igreja?")
                print("[1] Parece divertido")
                print("[2] Estou ocupado    |  Povo  //")
                escolha = int(input("Escolha: "))

                # Escolha 1
                if escolha == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"O evento é enorme, te chamam no palco, está de frente a milhares de pessoas, Obaid te pergunta")
                    print("[1] Passe")
                    print("[2] Passe")
                    escolha1 = int(input("Escolha: "))

                    if escolha1 == 1 or 2:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f"[Pastor Obaid]\nPresidente em frente a todas essas crianças orfãs, faria uma grande doação?")
                        print('[1] Obvio que sim  |  Midia  ///  Dinheiro ///  Povo //')
                        print('[2] Éeh            |  Midia  ///  Povo ///')
                        escolha11 = int(input("Escolha: "))
                        mortes(dinheiro, midia, povo, seguranca, nome_presidente)

                        if escolha11 == 1:
                            clear_terminal()
                            midia[0] += 15
                            dinheiro[0] -= 15
                            povo[0] += 10
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                            print(f"[Noticia]\nEvento bate recorde de doações")
                            print('[1] Passe')
                            print('[2] Passe')
                            escolha111 = int(input("Escolha: "))
                                                
                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break

                        if escolha11 == 2:
                            clear_terminal()
                            midia[0] += 15
                            povo[0] -= 15
                            print(nome_presidente)
                            print(f'No poder: {anos_poder[0]}')
                            print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                            print(f"[Noticia]\nApós a vergonha do presidente, muitas pessoas deixaram o evento antes das doações")
                            print('[1] Passe')
                            print('[2] Passe')
                            escolha111 = int(input("Escolha: "))

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                # escolha 2 

                if escolha == 2:
                    povo[0] -= 5
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print('[Noticia] Povo sente saudade do presidente em evento religioso')
                    print('[1] Passe')
                    print('[2] Passe')
                    escolha111 = int(input("Escolha: "))
                    anos_poder[0] += 1
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    
                    break

        # Pergunta 10
        if qualquer_uma_pastor_obaid == 10:
            while True:

                clear_terminal()
                print('No poder:',anos_poder)
                print(nome_presidente)
                print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                print(f"[Pastor Obaid]\nVamos ao culto?")
                print("[1] Claro, pegarei minha biblía")
                print("[2] Estou muito ocupado agora     |  Povo /")
                escolha = int(input("Escolha: "))

                # Escolha 1
                if escolha == 1:
                    clear_terminal()
                    print(nome_presidente)
                    print(f'No poder: {anos_poder[0]}')
                    print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                    print(f"O culto parece comum, muitas pessoas sentadas com suas biblías e celulares e ouvindo a palavra")
                    print("[1] Passe")
                    print("[2] Passe")
                    escolha1 = int(input("Escolha: "))

                    if escolha1 == 1 or 2:
                        clear_terminal()
                        print(nome_presidente)
                        print(f'No poder: {anos_poder[0]}')
                        print(f"\nDinheiro {dinheiro[0]} | midia {midia[0]} | Povo {povo[0]} | seguranca {seguranca[0]}\n")
                        print(f"[Pastor Obaid]\nO presidente garante que toda igreja é simbolo de poder")
                        print('[1] Sim e sempre será    |  Povo  //  Dinheiro ///')
                        print('[2] Eu nunca disse isso  |  Povo  //  Dinheiro ///')
                        escolha11 = int(input("Escolha: "))

                        if escolha11 == 1:
                            povo[0] += 10
                            dinheiro[0] += 15

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break

                        if escolha11 == 2:
                            clear_terminal()
                            dinheiro[0] -= 15
                            povo[0] -= 10

                            anos_poder[0] += 1
                            mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                            break


                # escolha 2 

                if escolha == 2:
                    povo[0] -= 5

                    anos_poder[0] += 1
                    mortes(dinheiro, midia, povo, seguranca, nome_presidente)
                    break













        break

            





# parado
def captain_jorge(dinheiro, midia, povo, seguranca, nome_presidente):
    pass

def Rose_marqueteira(dinheiro, midia, povo, seguranca, nome_presidente):
    print(
        f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n"
    )
    print(
        f"[Marqueteira Rose]\nO que acha de postar uma foto ao lado de crianças pobres?."
    )
    print("[1] É uma boa ideia!")
    print("[2] Melhor não.")
    try:
        escolha = int(input("Escolha: "))

        if escolha == 1:
            clear_terminal()
            print(
                f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n"
            )
            print(f"[noticia]\nPresidente posta foto zombando de crianças necessitadas")
            midia[0] -= 10
            povo[0] -= 25
            print("[1] Passar.")
            print("[2] Passar.")
            escolha1 = int(input("Escolha: "))
            if escolha1 == 1 or 2:
                mortes(dinheiro, midia, povo, seguranca, nome_presidente)

            mortes(dinheiro, midia, povo, seguranca, nome_presidente)

        if escolha == 2:
            povo[0] += 5
            mortes(dinheiro, midia, povo, seguranca, nome_presidente)

        mortes(dinheiro, midia, povo, seguranca, nome_presidente)

    except ValueError:
        print("Não está certo")

def eluni(dinheiro, midia, povo, seguranca, nome_presidente):
    while True:
        try:
            clear_terminal()
            print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
            print(f"[ELUNI - Assessor do presidente]\n{nome_presidente} A CYBER GANG, METAL LUNATICS ACABARAM DE ENTRAR NA DELEGACIA e estão destruindo tudo!")
            print("[1] Mandem o esquadrão especial agora!")
            print("[2] Tentem argumentar")
            escolha = int(input("Escolha: "))

            if escolha == 1:
                clear_terminal()
                povo[0] += 15
                midia[0] -= 15
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print("O povo adorou as mortes dos bandidos, mas os direitos humanos nem um pouco, o jornal diz que é um lider de chacina.")
                print("[1] Aaah")
                print("[2] Não ligo para eles.")
                passar = int(input("Escolha: "))
                if passar == 1:
                    break

            if escolha == 2:
                clear_terminal()
                povo[0] -= 25
                midia[0] += 15
                print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
                print("O negociador conversou e dialogou, mas a gang não ligou para nada, roubaram tudo antes que a policia conseguisse fazer algo.")
                print("[1] Meu Deus")
                print("[2] Vish.")
                passar = int(input("Escolha: "))
                if passar == 1 or 2:
                    break

        except ValueError:
            print("Não está certo")

def eleanor_direitos_humanos(dinheiro, midia, povo, seguranca, nome_presidente):
    pass
# parado







# Mortes
def mortes(dinheiro, midia, povo, seguranca, nome_presidente):

    if povo[0] < 0:
        povo[0] = 0

    if povo[0] > 100:
        povo[0] = 100

    if dinheiro[0] < 0:
        dinheiro[0] = 0

    if dinheiro[0] > 100:
        dinheiro[0] = 100

    if seguranca[0] < 0:
        seguranca[0] = 0

    if seguranca[0] > 100:
        seguranca[0] = 100

    if midia[0] < 0:
        midia[0] = 0

    if midia[0] > 100:
        midia[0] = 100

    # POVO
    if povo[0] <= 0:
        clear_terminal()

        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")

        print("O povo se cansou de suas más escolhas, invadiram o senado.")
        print("Você foi socado e pisoteado.")
        exit()

    if povo[0] >= 100:
        clear_terminal()
        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")        
        print("Todos votam em você, todos te amam, pulam pelas janelas para agarra lo tanto que fica sem ar.")
        print("Abraçado até ficar sufocado e morrer.")
        exit()
    # POVO

    # DINHEIRO
    if dinheiro[0] <= 0:
        clear_terminal()
        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
        print("[Primeira Dama]\nÉ amor, você gastou tudinho então precisamos entrar no avião e fugir agora mesmo")
        print("[1] O que?")
        print("[2] O que?")
        escolha = input("Escolha: ")
        if escolha == 1 or 2:
            print(
                "Vocês fogem para um lugar simples, se escondem e economizam para pagarem o botijão de gás"
            )
            exit()

    if dinheiro[0] >= 100:
        clear_terminal()
        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
        print("[Primeira Dama]\nMeu bem, somos tão eternamente ricos que precisamos aproveitar, vamos passear em nossa aeronave de ouro maciço")
        print("[1] O que?")
        print("[2] O que?")
        escolha = input("Escolha: ")
        if escolha == 1 or 2:
            print(
                "O jato de ouro voa por apenas 10 minutos, o peso enorme fez com que colidisse contra o chão e explodindo de forma catastrófica."
            )
            exit()
    # DINHEIRO

    # seguranca
    if seguranca[0] <= 0:
        clear_terminal()
        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
        print("[Acessor de contas]\nSenhor presidente, a segurança está horrivel, uma multidão está la fora fale com eles, talvez se acalmem.")
        print("[1] O que?")
        print("[2] O que?")
        escolha = input("Escolha: ")
        if escolha == 1 or 2:
            print(
                "Você tenta conversar com alguns protestantes, mas antes atiram em você."
            )
            exit()

    if seguranca[0] >= 100:
        clear_terminal()
        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
        print("[Celular]\nSenhor presidente, o general mandou você se retirar e desocupar a sala imediatamente.")
        print("[1] O que?")
        print("[2] O que?")
        escolha = input("Escolha: ")
        if escolha == 1 or 2:
            print("As ruas ficam cheias de tanques e tropas, a ditadura militar foi acionada, agora o exercito toma o poder.")
            exit()
    # seguranca

    # midia
    if midia[0] <= 0:
        clear_terminal()
        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
        print("[Marqueteira Rose]\nSenhor presidente, o seu impeachment foi concluído.")
        print("[1] O que?")
        print("[2] O que?")
        escolha = input("Escolha: ")
        if escolha == 1 or 2:
            print("Após os escandalos absurdos você perde o poder")
            exit()

    if midia[0] >= 100:
        clear_terminal()
        print(f"\nDinheiro{dinheiro[0]} | midia {midia[0]} | Povo{povo[0]} | seguranca{seguranca[0]}\n")
        print("[Rose - Marketeira]\nO jornal só fala do senhor, por favor desça e fale com as câmeras.")
        print("[1] O que?")
        print("[2] O que?")
        escolha = input("Escolha: ")
        if escolha == 1 or 2:
            print("[Noticia]\nDurante as perguntas amorosas da mídia, ocorre um ataque mortal de um ativista radical.")
            exit()
    # midia


# Mortes


def perguntas(dinheiro, midia, povo, seguranca, nome_presidente):
    while True:
        qualquer_uma = random.randint(1, 3)
        # qualquer_uma = 2


        if qualquer_uma == 1:
            clear_terminal()
            pastor_obaid(dinheiro, midia, povo, seguranca, nome_presidente)

        if qualquer_uma == 2:
            clear_terminal()
            gabriel_search_ever(dinheiro, midia, povo, seguranca, nome_presidente)

        if qualquer_uma == 3:
            clear_terminal()
            primeira_dama(dinheiro, midia, povo, seguranca, nome_presidente)







        if qualquer_uma == 4:
            clear_terminal()
            Rose_marqueteira(dinheiro, midia, povo, seguranca, nome_presidente)

        if qualquer_uma == 5:
            clear_terminal()
            eluni(dinheiro, midia, povo, seguranca, nome_presidente)

nome_aleatorio = boas_vindas_presidente()
perguntas(dinheiro, midia, povo, seguranca, nome_aleatorio)
