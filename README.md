# HashTable Class in Python

## Overview

This is a basic implementation of a **Hash Table** in Python, which provides efficient storage and retrieval of data through hashing. The class allows you to store key-value pairs in an array-like structure where keys are hashed using a custom hash function. The class also includes methods for printing the table's contents.

## Features

- **Customizable table size**: The size of the table can be specified during initialization (default is 7).
- **Custom hash function**: A simple hash function is used to map keys (strings) to indices in the table.
- **Collision handling**: Uses separate chaining (list of key-value pairs) to handle collisions.
- **Print table**: A method to print the entire table with its indexes and values.
- **Retrieve values**: Fetch values associated with keys using `get_item`.
- **List all keys**: Retrieve a list of all keys currently stored in the table.

## Methods

### `__init__(self, value = 7)`
Initializes the hash table with a specified size. By default, the size is set to 7.

#### Parameters:
- `value` (int): The size of the hash table (default is 7).

---

### `__hash(self, key)`
Private method that generates a hash value for a given key (string). It calculates a hash by iterating through the letters of the key, using a basic algorithm (ord of each letter * 23) and taking modulo of the table size.

#### Parameters:
- `key` (str): The key to be hashed.

#### Returns:
- An integer that represents the index in the `data_map` array.

---

### `set_item(self, key, value)`
Inserts a key-value pair into the hash table. If a collision occurs, the pair is added to a list at that index.

#### Parameters:
- `key` (str): The key associated with the value.
- `value` (any): The value to store.

---

### `get_item(self, key)`
Retrieves the value associated with a given key.

#### Parameters:
- `key` (str): The key to look up.

#### Returns:
- The value associated with the key, or `None` if the key is not found.

---

### `print_table(self)`
Prints the contents of the hash table. It shows the index and the associated value at that index.

---

### `keys(self)`
Returns a list of all keys stored in the hash table.

#### Returns:
- `list[str]`: A list of all keys in the table.

------------------------------------

# Classe HashTable em Python

## Visão Geral

Esta é uma implementação básica de uma **Tabela de Dispersão (Hash Table)** em Python, que fornece armazenamento e recuperação eficiente de dados através de hashing. A classe permite armazenar pares chave-valor numa estrutura semelhante a um array, onde as chaves são transformadas usando uma função de dispersão personalizada. A classe também inclui métodos para imprimir o conteúdo da tabela.

## Funcionalidades

- **Tamanho personalizável da tabela**: O tamanho da tabela pode ser especificado durante a inicialização (o padrão é 7).
- **Função de dispersão personalizada**: Uma função simples é utilizada para mapear chaves (strings) para índices na tabela.
- **Tratamento de colisões**: Utiliza encadeamento separado (lista de pares chave-valor) para lidar com colisões.
- **Imprimir tabela**: Um método para imprimir toda a tabela com os seus índices e valores.
- **Recuperar valores**: Buscar valores associados às chaves usando `get_item`.
- **Listar todas as chaves**: Recupera uma lista de todas as chaves atualmente armazenadas na tabela.

## Métodos

### `__init__(self, value = 7)`
Inicializa a tabela de dispersão com um tamanho especificado. Por padrão, o tamanho é definido como 7.

#### Parâmetros:
- `value` (int): O tamanho da tabela de dispersão (o padrão é 7).

---

### `__hash(self, key)`
Método privado que gera um valor de dispersão para uma dada chave (string). Calcula o hash iterando pelas letras da chave, usando um algoritmo básico (ord de cada letra * 23) e aplicando o módulo do tamanho da tabela.

#### Parâmetros:
- `key` (str): A chave a ser transformada.

#### Retorna:
- Um inteiro que representa o índice no array `data_map`.

---

### `set_item(self, key, value)`
Insere um par chave-valor na tabela de dispersão. Se ocorrer uma colisão, o par é adicionado a uma lista nesse índice.

#### Parâmetros:
- `key` (str): A chave associada ao valor.
- `value` (qualquer tipo): O valor a ser armazenado.

---

### `get_item(self, key)`
Recupera o valor associado a uma dada chave.

#### Parâmetros:
- `key` (str): A chave a ser pesquisada.

#### Retorna:
- O valor associado à chave, ou `None` se a chave não for encontrada.

---

### `print_table(self)`
Imprime o conteúdo da tabela de dispersão. Mostra o índice e os valores associados a esse índice.

---

### `keys(self)`
Retorna uma lista de todas as chaves armazenadas na tabela.

#### Retorna:
- `list[str]`: Uma lista de todas as chaves na tabela.
