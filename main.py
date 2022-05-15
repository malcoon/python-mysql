import mysql.connector
import pandas as pd
import os

conex_sql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='147258369'
)

if conex_sql.is_connected():
    conex_sql_info = conex_sql.get_server_info()
    cursor = conex_sql.cursor()

# Menu Principal
def menu():
    print ('''
    ECOLHA UMA OPÇÃO: \n
    1 → Criar um database
    2 → Criar tabela
    3 → Listar tabela
    4 → Adicionar nome
    5 → Deletar nome
    6 → Deletar tabela
    0 → Finalizar\n''')

# Criar um database
def create_database():
    os.system('cls')
    nome_db = str(input('Nome do Database: '))

    create_database = f'CREATE SCHEMA {nome_db}; USE {nome_db};'
    cursor.execute(create_database)
    conex_sql.commit()
    print(f'Database criado: {nome_db}')


def create_table():
    os.system('cls')
    nome_db = str(input('Informe o nome do Database: '))
    nome_table = str(input('Nome da tabela: '))
    nome = str(input('Coluna para nome: '))
    sexo = str(input('Coluna para sexo: '))
    email = str(input('Coluna para email: '))
    idade = str(input('Coluna para idade: '))
    telefone = str(input('Coluna para telefone: '))

    create_new_table = f'''CREATE TABLE {nome_db}.{nome_table} (
        id_{nome_table} INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        {nome} VARCHAR(45) NULL, 
        {sexo} VARCHAR(45) NULL, 
        {email} VARCHAR(45) NULL, 
        {idade} INT NULL, 
        {telefone} INT NULL);'''
    cursor.execute(create_new_table)
    conex_sql.commit()
    print(f'Tabela {nome_table} foi criada!')


# Listar tabela 
def search_table():
    os.system('cls')
    search_db_name = str(input('Nome do database: '))
    search_table_name = str(input('Nome da tabela: '))

    search_table = f'SELECT * FROM {search_db_name}.{search_table_name};'
    cursor.execute(search_table)
    result = cursor.fetchall()
    list_contact = pd.DataFrame(result, columns=['ID', 'Nome', 'Cargo', 'Email', 'Telefone', 'Salário'])
    print(list_contact)

# Novo contato
def add_contact():
    os.system('cls')
    db_name = str(input('Nome do database: '))
    table_name = str(input('Nome da tabela: '))

    name = str(input('Digite o nome: '))
    sexo = str(input('Digite o sexo: '))
    email = str(input('Digite o email: '))
    idade = int(input('Digite o idade: '))
    telefone = int(input('Digite o telefone: '))

    add_people = f'''INSERT INTO {db_name}.{table_name} (
        nome, sexo, email, idade, telefone) 
        VALUES (
        "{name}", "{sexo}", "{email}", {idade}, {telefone});'''
    cursor.execute(add_people)
    conex_sql.commit()
    print(f'{name} foi adicionado!')

def del_name():
    os.system('cls')
    db_name = str(input('Nome do database: '))
    table_name = str(input('Nome da tabela: '))
    nome_delete = str(input('Digite o nome: '))

    del_name = f'DELETE FROM {db_name}.{table_name} WHERE nome LIKE "%{nome_delete}%";'
    cursor.execute(del_name)
    conex_sql.commit()
    print(f'{nome_delete} foi deletado do banco de dados.')

def del_table():
    os.system('cls')
    print('''
Tem certeza que deseja deletar todos os dados?
    1 - Sim
    2 - Não \n''')
    del_option = int(input('Digite uma opção: '))
    
    if del_option == 1:
        name_db_del = str(input('Informe qual o Database: '))
        name_table_del = str(input('Informe qual tabela: '))
        
        del_table = f'DROP TABLE {name_db_del}.{name_table_del};'
        cursor.execute(del_table)
        conex_sql.commit()
        print(f'A tabela {name_table_del} em {name_db_del} foi deletada')
    elif del_option == 2:
        print('Nada foi deletado')
    else: 
        print('Por favor, digite uma opção válida.')
    
#
# Menu 
#
option = 0

while option != 6:
    menu()
    option = int(input('Digite uma opção: '))
    if option == 1:
        create_database()
    elif option == 2:
        create_table()
    elif option == 3:
        search_table()
    elif option == 4:
        add_contact()
    elif option == 5:
        del_name()
    elif option == 6:
        del_table()
    else:
        print('Finalizando...')
    break

# Fechar a conexao ao BD
cursor.close()
conex_sql.close()