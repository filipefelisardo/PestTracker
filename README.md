# Obejtivo do projeto 
### O projeto Pest Tracker tem como objetivo simular uma aplicação para a previsão da praga da mosca da azeitona no olival. A aplicação tem como objetivo alertar os agricultores sobre o risco da praga, utilizando dados simulados. A escolha desse projeto foi motivada pelo trabalho teórico e descritivo desenvolvido na disciplina "Fundamentos da Ciência de Dados Agro-Ambientais". Aqui, criamos uma aplicação prática com dados simulados.

# Banco de dados 
### O sistema utiliza um banco de dados o SQLite 3 chamado armadilhas.db para armazenar informações sobre as armadilhas, incluindo nome, coordenada X e coordenada Y, garantindo que as informações das armadilhas e coordenadas sejam mantidas a cada execução do programa.



# Funcionalidades 
O nome da aplicação a desenvolver será o pest tracker, que ocnta com 6 opções:

opção 1 : Número de moscas por armadilha 
opção 2 : Adicionar armadilha 
opção 3 : Mostrar detalhes das armadilhas 
opção 4 : Alterar nome da armadilha 
opção 5 : Apagar armadilha 
opção 6 : Terminar o programa

Na "opção 1" permite adicionar mais armadilhas, e vamos adicionar um nome a armadilha juntamente com as coordenadas geográficas (latitude e longitude)

Na "opção 2" permite ver o número de de moscas existente em cada armadilha com as coordenadas, e tambem as condições ambientais de quando foi feito esse registo, nomeadamente a temperatura e humidade.

Na "opção 3" permite saber o nivel de risco de presença da mosca da azeitona nas diferentes armadilhas, este risco varia de "alta", "moderada" e "baixa"

Na "opção 4" permite ver o número de armadilhas registadas, e as suas coordenadas geográficas

Na "opção 5" permite alterar o nome das armadilhas, inicialmente escrevemos o nome da armadilha que queremos alterar e depois o novo nome que pretendemos para essa armadilha 

Na "opção 6" permite apagar as armadilhas que desejarmos

Na "opção 7" serve para terminar o programa 
