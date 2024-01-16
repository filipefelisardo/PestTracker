import random
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

def main():
    # Código do banco de dados e funções aqui...

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
            # Fechar conexão com o banco de dados antes de sair
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

# Conectar ao banco de dados (será criado se não existir)
conn = sqlite3.connect('armadilhas.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS armadilhas (
        nome TEXT PRIMARY KEY,
        coordenada_x REAL,
        coordenada_y REAL
    )
''')
conn.commit()

# Função que simula leituras de uma armadilha inteligente
def ler_sensor_mosca():
    return random.randint(0, 5)  # Simula a contagem de moscas da azeitona

# Função que simula leituras de sensores ambientais
def ler_sensor_temperatura():
    return random.randint(15, 30)  # Simula a leitura de temperatura em graus Celsius

def ler_sensor_humidade():
    return random.randint(30, 80)  # Simula a leitura de umidade do solo em porcentagem

# Função que notifica sobre a presença de moscas e condições ambientais
def notificar_mosca(contagem_moscas, nome_armadilha, coordenadas, temperatura, humidade):
    print(f"Foi detectada a presença de {contagem_moscas} moscas da azeitona na armadilha '{nome_armadilha}' nas coordenadas {coordenadas}.")
    print(f"Condições ambientais - Temperatura: {temperatura}°C, Humidade: {humidade}%.")

# Função para contar o número de moscas por armadilha e quais as condições ambientais
def contar_moscas_por_armadilha():
    cursor.execute('SELECT nome, coordenada_x, coordenada_y FROM armadilhas')
    armadilhas = cursor.fetchall()
    if not armadilhas:
        print("Nenhuma armadilha registada.")
    else:
        for nome, coordenada_x, coordenada_y in armadilhas:
            contagem = ler_sensor_mosca()
            temperatura = ler_sensor_temperatura()
            humidade = ler_sensor_humidade()
            notificar_mosca(contagem, nome, (coordenada_x, coordenada_y), temperatura, humidade)

# Função para adicionar armadilha
def adicionar_armadilha():
    try:
        nome = input("Qual o nome da nova armadilha: ")
        coordenada_x = float(input("Digite a coordenada X da nova armadilha: "))
        coordenada_y = float(input("Digite a coordenada Y da nova armadilha: "))

        # Inserir dados no banco de dados
        cursor.execute('INSERT INTO armadilhas VALUES (?, ?, ?)', (nome, coordenada_x, coordenada_y))
        conn.commit()

        print("Armadilha adicionada com sucesso!")
    except ValueError:
        print("Por favor, insira coordenadas válidas (números).")

# Função para mostrar detalhes das armadilhas
def mostrar_detalhes_armadilhas():
    cursor.execute('SELECT nome, coordenada_x, coordenada_y FROM armadilhas')
    armadilhas = cursor.fetchall()
    if not armadilhas:
        print("Nenhuma armadilha registada.")
    else:
        print("Detalhes das armadilhas:")
        for nome, coordenada_x, coordenada_y in armadilhas:
            print(f"Nome: {nome}, Coordenadas: ({coordenada_x}, {coordenada_y})")

# Função para mostrar o número de armadilhas
def mostrar_numero_armadilhas():
    cursor.execute('SELECT COUNT(*) FROM armadilhas')
    numero_armadilhas = cursor.fetchone()[0]
    print(f"Número de armadilhas registadas: {numero_armadilhas}")

# Função para alterar o nome da armadilha
def alterar_nome_armadilha():
    nome_atual = input("Qual o nome da armadilha que deseja alterar: ")
    novo_nome = input("Qual o novo nome para a armadilha: ")

    cursor.execute('UPDATE armadilhas SET nome = ? WHERE nome = ?', (novo_nome, nome_atual))
    conn.commit()
    print("Nome da armadilha alterado com sucesso.")

# Função para apagar uma armadilha
def apagar_armadilha():
    nome_apagar = input("Qual o nome da armadilha que deseja apagar: ")

    cursor.execute('DELETE FROM armadilhas WHERE nome = ?', (nome_apagar,))
    conn.commit()
    print("Armadilha apagada com sucesso.")
    
# Função para avaliar o risco de presença da mosca da azeitona em todas as armadilhas
def avaliar_risco_presenca_mosca():
    cursor.execute('SELECT nome, coordenada_x, coordenada_y FROM armadilhas')
    armadilhas = cursor.fetchall()
    
    if not armadilhas:
        print("Nenhuma armadilha registada.")
    else:
        print("Avaliação de risco de presença da mosca da azeitona:")
        for nome, coordenada_x, coordenada_y in armadilhas:
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