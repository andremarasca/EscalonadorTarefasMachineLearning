# Escalonador de Tarefas utilizando Machine Learning

Sugestão para escalonamento de tarefas, implementei um regressor que define o retorno do callback de um método de ordenação.

O callback do método de ordenação segue o mesmo princípio que o qsort da stdlib em C: http://www.cplusplus.com/reference/cstdlib/qsort/
- recebe dois itens A e B
- retorno -1 se o item A deve vir a esquerda do item B
- retorno 0 se ambos tem valores iguais
- retorno 1 se o item B deve vir a esquerda do item A

No exemplo eu crio uma base de dados que tem comparações entre 2 pessoas, pessoa1 e pessoa2, gerando os atributos:
- altura1, peso1, altura2, peso2, retorno_do_callback_desejado
- A base de dados é gerada automaticamente, e apenas na construção eu calculo o IMC, mas apenas para saber qual é o retorno desejado para o callback, ou seja, para saber qual pessoa tem maior IMC.

O modelo regressor da rede neural recebe a base descrita acima e aprende a retornar o valor correto do callback, então, para ordenação, na chamada do callback do método de ordenação eu retorno o valor predito pelo MLPRegressor, e com isso é feita a ordenação de pessoas pelo IMC.

O exemplo é didático, mas em lugar de pessoas poderiam vir tarefas. Neste caso, para usar o programa, basta criar uma base de dados conforme o formato especificado, decidindo qual tarefa é mais prioritária.

