# Objetivo do projeto 
O projeto Pest Tracker tem como objetivo simular uma aplicação para a previsão da praga da mosca da azeitona no olival. A aplicação tem como objetivo alertar os agricultores sobre o risco da praga, utilizando dados simulados. A escolha desse projeto foi motivada pelo trabalho teórico e descritivo desenvolvido na disciplina "Fundamentos da Ciência de Dados Agro-Ambientais". Aqui, transformamos conceitos teóricos em uma aplicação prática com dados simulados.

# Banco de dados 
O sistema utiliza um banco de dados o SQLite 3 chamado armadilhas.db para armazenar informações sobre as armadilhas. Essas informações incluem o nome da armadilha, latitude e longitude, garantindo que as informações das armadilhas e coordenadas sejam mantidas a cada execução do programa.

# Funcionalidades 
O nome da aplicação a desenvolver será o pest tracker, que conta com 7 opções:

opção 1 : Número de moscas por armadilha 
opção 2 : Adicionar armadilha 
opção 3 : Risco de presença da mosca da azeitona 
opção 3 : Mostrar detalhes das armadilhas 
opção 4 : Alterar nome da armadilha 
opção 5 : Apagar armadilha 
opção 6 : Terminar o programa

Na "opção 1" permite adicionar mais armadilhas, e adicionamos um nome á armadilha juntamente com as coordenadas geográficas (latitude e longitude)

Na "opção 2" permite ver o número de de moscas existente em cada armadilha com as coordenadas, e tambem as condições ambientais de quando foi feito esse registo, nomeadamente a temperatura e humidade.

Na "opção 3" permite saber o nivel de risco de presença da mosca da azeitona nas diferentes armadilhas, classificando o risco como "alta", "moderada" e "baixa"

Na "opção 4" permite ver o número de armadilhas registadas, e as suas coordenadas geográficas

Na "opção 5" permite alterar o nome das armadilhas, inicialmente escrevemos o nome da armadilha que queremos alterar e depois o novo nome que pretendemos para essa armadilha 

Na "opção 6" permite apagar as armadilhas que pretendermos 

Na "opção 7" serve para terminar o programa 


# Explicação das funções criadas

- Adicionar Armadilha (adicionar_armadilha):
Solicita e registra um nome para uma nova armadilha, juntamente com as coordenadas geográficas (latitude e longitude).
Insere os dados no banco de dados SQLite.

- Número de Moscas por Armadilha (contar_moscas_por_armadilha):
Lê o número simulado de moscas da azeitona, temperatura e humidade para cada armadilha registada.
Notifica sobre a presença de moscas e mostra as condições ambientais.

- Risco de Presença da Mosca da Azeitona (avaliar_risco_presenca_mosca):
Avalia o risco de presença da mosca da azeitona em todas as armadilhas registradas.
Classifica o risco como "alta", "moderada" ou "baixa" com base na contagem simulada de moscas.

- Mostrar Detalhes das Armadilhas (mostrar_detalhes_armadilhas):
Mostra os detalhes (nome, latitude, longitude) de todas as armadilhas registradas no banco de dados.

- Alterar Nome da Armadilha (alterar_nome_armadilha):
Permite a alteração do nome de uma armadilha existente.
Atualiza o banco de dados com o novo nome.

- Apagar Armadilha (apagar_armadilha):
Apaga uma armadilha específica com base no nome fornecido.
Atualiza o banco de dados removendo os registros associados.

- Terminar Programa (main):
Executa a função correspondente à escolha do usuário.
Encerra o programa quando a opção 7 é selecionada, fechando a conexão com o banco de dados.