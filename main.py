import mysql.connector
import pandas as pd

conex_sql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234567890'
)

if conex_sql.is_connected():
    conex_sql_info = conex_sql.get_server_info()
    cursor = conex_sql.cursor()
    print('Você está conectado!')

# Menu Principal
def menu():
    print ('''
    ECOLHA UMA OPÇÃO:

    1 → Criar um database
    2 → Criar tabela
    3 → Listar tabela
    4 → Adicionar funcionario
    0 → Finalizar\n''')

# Criar um database
def create_database():

    nome_db = str(input('Nome do Database: '))

    create_database = f'CREATE SCHEMA {nome_db}'
    cursor.execute(create_database)
    conex_sql.commit()
    print(f'Database criado: {nome_db}')

def create_table():

    nome_db = str(input('Informe o nome do Database: '))
    nome_table = str(input('Nome da tabela: '))
    nome_func = str(input('Coluna para nome: '))
    cargo_func = str(input('Coluna para cargo: '))
    email_func = str(input('Coluna para email: '))
    tel_func = str(input('Coluna para telefone: '))
    sal_func = str(input('Coluna para salario: '))

    create_new_table = f'''CREATE TABLE {nome_db}.{nome_table} (
        id_func INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        {nome_func} VARCHAR(45) NULL, 
        {cargo_func} VARCHAR(45) NULL, 
        {email_func} VARCHAR(45) NULL, 
        {tel_func} INT NULL, 
        {sal_func} INT NULL);'''
    cursor.execute(create_new_table)
    conex_sql.commit()
    print(f'Tabela {nome_table} foi criada!')


# Listar tabela 
def search_table():

    search_db_name = str(input('Nome do database: '))
    search_table_name = str(input('Nome da tabela: '))

    search_table = f'SELECT * FROM {search_db_name}.{search_table_name};'
    cursor.execute(search_table)
    result = cursor.fetchall()
    list_contact = pd.DataFrame(result, columns=['ID', 'Nome', 'Cargo', 'Email', 'Telefone', 'Salário'])
    print(list_contact)

# Novo contato
def add_contact():

    db_name = str(input('Nome do database: '))
    table_name = str(input('Nome da tabela: '))

    name = str(input('Digite o nome do funcionario: '))
    cargo = str(input('Digite o cargo do funcionario: '))
    email = str(input('Digite o email do funcionario: '))
    phone = int(input('Digite o telefone do funcionario: '))
    salario = int(input('Digite o salario do funcionario: '))

    add_people = f'''INSERT INTO {db_name}.{table_name} (
        nome_fun, cargo_fun, email_fun, tel_fun, sal_fun) 
        VALUES (
        "{name}", "{cargo}", "{email}", {phone}, {salario});'''
    cursor.execute(add_people)
    conex_sql.commit()
    print(f'O funcionário {name} foi adicionado!')

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
    else:
        print('Finalizando...')
    break

# Fechar a conexao ao BD
cursor.close()
conex_sql.close()