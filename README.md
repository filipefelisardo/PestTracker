# Objetivo do projeto 
- O projeto Pest Tracker tem como objetivo simular uma aplicação para a previsão da praga da mosca da azeitona no olival. A aplicação tem como objetivo alertar os agricultores sobre o risco da praga, utilizando dados simulados. A escolha desse projeto foi motivada pelo trabalho teórico e descritivo desenvolvido na disciplina "Fundamentos da Ciência de Dados Agro-Ambientais". Aqui, transformamos conceitos teóricos em uma aplicação prática com dados simulados.

# Banco de dados 
- O sistema utiliza um banco de dados o SQLite 3 chamado armadilhas.db para armazenar informações sobre as armadilhas. Essas informações incluem o nome da armadilha, latitude e longitude, garantindo que as informações das armadilhas e coordenadas sejam mantidas a cada execução do programa.

# Funcionalidades da aplicação 

- Na "opção 1" (Número de moscas por armadilha) permite adicionar mais armadilhas, e adicionamos um nome á armadilha juntamente com as coordenadas geográficas (latitude e longitude)

- Na "opção 2" (Adicionar armadilha) permite ver o número de de moscas existente em cada armadilha com as coordenadas, e tambem as condições ambientais de quando foi feito esse registo, nomeadamente a temperatura e humidade.

- Na "opção 3" (Risco de presença da mosca da azeitona) permite saber o nivel de risco de presença da mosca da azeitona nas diferentes armadilhas, classificando o risco como "alta", "moderada" e "baixa"

- Na "opção 4" (Mostrar detalhes das armadilhas) permite ver o número de armadilhas registadas, e as suas coordenadas geográficas

- Na "opção 5" (Alterar nome da armadilha) permite alterar o nome das armadilhas, inicialmente escrevemos o nome da armadilha que queremos alterar e depois o novo nome que pretendemos para essa armadilha 

- Na "opção 6" (Apagar armadilha) permite apagar as armadilhas que pretendermos 

Na "opção 7" (Terminar o programa) serve para terminar o programa 


# Explicação das funções criadas

- **main()** 
Executa a função correspondente à escolha do utilizador.
Encerra o programa quando a opção 7 é selecionada, fechando a conexão com o banco de dados.

-  **ler_sensor_mosca()** 
Simula a contagem do numero de moscas da azeitona. Utiliza a biblioteca random do Python para fornecer um número inteiro aleatório no intervalo de 0 a 10

- **ler_sensor_temperatura()** 
Simula a leitura de temperatura em graus Celsius.Utiliza a biblioteca random do Python para fornecer um número inteiro aleatório no intervalo de 15 a 30, representando a leitura do sensor de temperatura

- **ler_sensor_humidade()** 
Simula a leitura de humidade do solo em percentagem. Utiliza a biblioteca random do Python para fornecer um número inteiro aleatório no intervalo de 20 a 80.

- **notificar_mosca()** 
Notifica a presença de moscas da azeitona numa armadilha, com informações sobre as condições ambientais. Esta função usa f-strings para formatar a saída de texto.

- **contar_moscas_por_armadilha()**  
A função utiliza o  cursor para executar uma consulta SQL que seleciona o nome, latitude e longitude de todas as armadilhas registadas. Em seguida, verifica se há armadilhas registradas e, se houver, mostra a lista de armadilhas, simulando a contagem de moscas e as leituras de sensores para cada uma dela.

- **adicionar_armadilha()** 
Solicita e regista um nome para uma nova armadilha, juntamente com as coordenadas geográficas (latitude e longitude). De seguida os valores são inseridos no banco de dados SQLite se a inserção for bem sucedida. Esta inserção é confirmada com *conn.commit()*, se os valores ao serem inseridos não forem numéricos a excepção *ValueError* mostra uma mensagem indicando para inserir coordenadas válidas (números)

- **mostrar_detalhes_armadilhas()**  
Nesta função é utilizado cursor.execute para executar uma consulta em  SQL que seleciona o nome, a latitude e a longitude de todas as armadilhas na tabela armadilhas.
Em seguida, utiliza-se cursor.fetchall() para recuperar todas as linhas resultantes da consulta, se não houver armadilhas registadas, a função mostra uma mensagem indicando que nenhuma armadilha está registrada. Caso contrário, a função mostra os detalhes de cada armadilha no formato "Nome: [nome], Coordenadas: ([latitude], [longitude])"

- **alterar_nome_armadilha()** 
Esta função pergunta ao utilizador o nome atual da armadilha que pretende alterar e o novo nome da armadilha usando o input. Depois é usado a instrução *SQL UPDATE* usando cursor.execute para alterar o nome da armadilha no banco de dados. A cláusula *WHERE* garante que apenas a entrada corresponde é alterada. A alteração é confirmada usando conn.commit() para guardar as alterações no banco de dados.
Por fim, a função mostra uma mensagem indicando que o nome da armadilha foi alterado com sucesso.

- **apagar_armadilha()** 
A função pergunta ao utilizador o nome da armadilha que pretende apagar usando a função input. Depois, é executa uma instrução *SQL DELETE* usando cursor.execute para remover a armadilha do banco de dados. A cláusula *WHERE* garante que apenas a entrada correspondente é apagada.
A alteração é confirmada usando *conn.commit()* para salvar as alterações no banco de dados.
Por fim, a função mostra uma mensagem indicando que a armadilha foi apagada com sucesso.

- **avaliar_risco_presenca_mosca()** 
A função executa uma consulta SQL para obter informações sobre todas as armadilhas no banco de dados.
Se não houver armadilhas registradas, a função mostra uma mensagem indicando que nenhuma armadilha está registada, caso contrário a função mostra para cada uma das armadilhas a contagem de moscas usando a função ler_sensor_mosca.
Com base na contagem de moscas, a função imprime mensagens indicando o nível de risco de presença da mosca da azeitona em cada armadilha. A classificação do está defenida como maior ou igual a 4 o risco é alto, no intervalo entre 2 e 4 o risco é moderado, menor que que 2 o risco é baixo.


**Melhorias futuras**

- Configurar a aplicação para armazenar os dados simulados na base de dados.
- Configurar a função avaliar_risco_presença_mosca para recuperar informações da base de dados e, com base nessas informações, realizar a avaliação de risco.
- Substituir os dados simulados por dados reais.
- Desenvolver a capacidade de obter dados de uma estação meteorológica e de uma armadilha inteligente.
- Criar uma aplicação completa, incluindo um front-end desenvolvido para a interação do usuário.
