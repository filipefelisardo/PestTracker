import random
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

def main():
    # Código do banco de dados 

    while True:
        print("Pest Tracker")
        print("+------------------------------------------------------+")
        print("| Opção |            Descrição                         |")
        print("+------------------------------------------------------+")
        print("|   1   | Adicionar armadilha                          |")
        print("|   2   | Número de moscas por armadilha               |")
        print("|   3   | Risco de presença da mosca da azeitona       |")
        print("|   4   | Mostrar detalhes das armadilhas              |")
        print("|   5   | Alterar nome da armadilha                    |")
        print("|   6   | Apagar armadilha                             |")
        print("|   7   | Terminar programa                            |")
        print("+------------------------------------------------------+")

        opcao = input("Escolha uma opção (1 a 7): ")

        if opcao == '1':
            adicionar_armadilha() 
        elif opcao == '2':
            contar_moscas_por_armadilha()
        elif opcao == '3':
            avaliar_risco_presenca_mosca()
        elif opcao == '4':
            mostrar_detalhes_armadilhas()
        elif opcao == '5':
            alterar_nome_armadilha()
        elif opcao == '6':
            apagar_armadilha()
        elif opcao == '7':
            print("Programa encerrado.")
            # Fecha conexão com o banco de dados antes de sair
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

# Conecta ao banco de dados (será criado se não existir)
conn = sqlite3.connect('armadilhas.db')
cursor = conn.cursor()

# Cria tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS armadilhas (
        nome TEXT PRIMARY KEY,
        latitude Real,
        longitude Real
    )
''')
conn.commit()

# Função que simula leituras de uma armadilha inteligente
def ler_sensor_mosca():
    return random.randint(0, 10)  # Simula a contagem do numero de moscas da azeitona, entre 0 e 10 

# Função que simula leituras de sensores ambientais
def ler_sensor_temperatura():
    return random.randint(15, 30)  # Simula a leitura de temperatura em graus Celsius, entre os 15 e os 30

def ler_sensor_humidade():
    return random.randint(20, 80)  # Simula a leitura de humidade do solo em percentagem, entre os 20 e os 80 

# Função que notifica sobre a presença de moscas e condições ambientais
def notificar_mosca(contagem_moscas, nome_armadilha, coordenadas, temperatura, humidade):
    print(f"Foi detectada a presença de {contagem_moscas} moscas da azeitona na armadilha '{nome_armadilha}' nas coordenadas {coordenadas}.")
    print(f"Condições ambientais - Temperatura: {temperatura}°C, Humidade: {humidade}%.")

# Função para contar o número de moscas por armadilha e quais as condições ambientais
def contar_moscas_por_armadilha():
    cursor.execute('SELECT nome, latitude, longitude FROM armadilhas')
    armadilhas = cursor.fetchall()
    if not armadilhas:
        print("Nenhuma armadilha registada.")
    else:
        for nome, latitude, longitude in armadilhas:
            contagem = ler_sensor_mosca()
            temperatura = ler_sensor_temperatura()
            humidade = ler_sensor_humidade()
            notificar_mosca(contagem, nome, (latitude, longitude), temperatura, humidade)

# Função para adicionar uma nova armadilha
def adicionar_armadilha():
    try:
        nome = input("Qual o nome da nova armadilha: ")
        latitude = float(input("Digite a latitude da nova armadilha: "))
        longitude = float(input("Digite a longitude da nova armadilha: "))

        # Insere dados no banco de dados
        cursor.execute('INSERT INTO armadilhas VALUES (?, ?, ?)', (nome, latitude, longitude))
        conn.commit()

        print("Armadilha adicionada com sucesso!")
    except ValueError:
        print("Por favor, insira coordenadas válidas (números).")

# Função para mostrar informações das armadilhas
def mostrar_detalhes_armadilhas():
    cursor.execute('SELECT nome, latitude, longitude FROM armadilhas')
    armadilhas = cursor.fetchall()
    if not armadilhas:
        print("Nenhuma armadilha registada.")
    else:
        print("Detalhes das armadilhas:")
        for nome, latitude, longitude in armadilhas:
            print(f"Nome: {nome}, Coordenadas: ({latitude}, {longitude})")

# Função para mostrar o número de armadilhas
def mostrar_numero_armadilhas():
    cursor.execute('SELECT COUNT(*) FROM armadilhas')
    numero_armadilhas = cursor.fetchone()[0]
    print(f"Número de armadilhas registadas: {numero_armadilhas}")

# Função para alterar o nome da armadilha
def alterar_nome_armadilha():
    nome_atual = input("Qual o nome da armadilha que pretende alterar: ")
    novo_nome = input("Qual o novo nome para a armadilha: ")

    cursor.execute('UPDATE armadilhas SET nome = ? WHERE nome = ?', (novo_nome, nome_atual))
    conn.commit()
    print("Nome da armadilha alterado com sucesso.")

# Função para apagar uma armadilha
def apagar_armadilha():
    nome_apagar = input("Qual o nome da armadilha que pretende apagar: ")

    cursor.execute('DELETE FROM armadilhas WHERE nome = ?', (nome_apagar,))
    conn.commit()
    print("Armadilha apagada com sucesso.")
    
# Função para avaliar o risco de presença da mosca da azeitona em todas as armadilhas
def avaliar_risco_presenca_mosca():
    cursor.execute('SELECT nome, latitude, longitude FROM armadilhas')
    armadilhas = cursor.fetchall()
    
    if not armadilhas:
        print("Nenhuma armadilha registada.")
    else:
        print("Avaliação de risco de presença da mosca da azeitona:")
        for nome, latitude, coordenada_y in armadilhas:
            contagem = ler_sensor_mosca()
            
            # Defina seus critérios de avaliação de risco com base na contagem de moscas
            if contagem >= 4:
                print(f"Armadiha '{nome}': A presença de mosca da azeitona é alta. Recomendamos realizar um tratamento no olival.")
            elif 2 <= contagem < 4:
                print(f"Armadiha '{nome}': A presença de mosca da azeitona é moderada. Aconselhamos a manter-se alerta.")
            else:
                print(f"Armadiha '{nome}': A presença de mosca da azeitona é baixa.")

if __name__ == "__main__":
    main()

#teste
    

