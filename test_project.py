from project import ler_sensor_humidade, ler_sensor_mosca, ler_sensor_temperatura


def test_ler_sensor_mosca_esta_dentro_do_intervalo():
    resultado = ler_sensor_mosca()
    assert 0 <= resultado <= 5

def test_ler_sensor_temperatura_esta_dentro_do_intervalo():
    resultado = ler_sensor_temperatura()
    assert 15 <= resultado <= 30

def test_ler_sensor_humidade_esta_dentro_do_intervalo():
    resultado = ler_sensor_humidade()
    assert 30 <= resultado <= 80

def notificar_mosca(contagem_moscas, nome_armadilha, coordenadas, temperatura, humidade):
    print(f"Foi detectada a presença de {contagem_moscas} moscas da azeitona na armadilha '{nome_armadilha}' nas coordenadas {coordenadas}.")
    print(f"Condições ambientais - Temperatura: {temperatura}°C, Humidade: {humidade}%.")

# Exemplo de teste usando pytest
def test_notificar_mosca(capsys):
    contagem_moscas = 5
    nome_armadilha = "Armadilha1"
    coordenadas = (10.0, 20.0)
    temperatura = 25.0
    humidade = 70.0

    notificar_mosca(contagem_moscas, nome_armadilha, coordenadas, temperatura, humidade)

    captured = capsys.readouterr()
    assert "Foi detectada a presença de 5 moscas da azeitona na armadilha 'Armadilha1' nas coordenadas (10.0, 20.0)." in captured.out
    assert "Condições ambientais - Temperatura: 25.0°C, Humidade: 70.0%." in captured.out


