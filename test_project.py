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

def test_notificar_mosca_output_formato_correto():
    # Verificando se a função produz a saída no formato esperado
    contagem_moscas = 5
    nome_armadilha = "Armadilha1"
    coordenadas = (10, 20)
    temperatura = 25
    humidade = 60

    expected_output = (
        f"Foi detectada a presença de {contagem_moscas} moscas da azeitona na armadilha '{nome_armadilha}' nas coordenadas {coordenadas}.\n"
        f"Condições ambientais - Temperatura: {temperatura}°C, Humidade: {humidade}%.\n"
    )


