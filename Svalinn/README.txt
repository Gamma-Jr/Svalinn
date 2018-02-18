REPOSITÓRIO DE DESENVOLVIMENTO DA PLATAFORMA DE SIMULAÇÃO SVALINN
——————————————————————————————————————————————————————————————————

É recomendado que as mudanças do layout sejam feitas em um outro branch antes de que seja mesclado com o branch master.

Mudanças nos arquivos .html deverão ser feitas nos arquivos contidos no diretório library/templates.

Mudanças no layout (Imagem de fundo, logo, créditos, etc…) da página deverá ser feita no arquivo layout.html

Mudanças no navegador deverá ser feita no arquivo _navbar.html no diretório library/templates/includes

MUDANÇAS DEVEM SER FEITAS APENAS NOS CAMPOS CONTIDOS ENTRE OS MARCADORES {%block head%},{%endblock%}/{%block body%},{%endblock%}

——————————————————————————————————————————————————————————————————

Biblioteca do Kameleon e dependências podem ser instaladas diretamente pelos instaladores no link https://ccmc.gsfc.nasa.gov/Kameleon/Quick_start.html

A configuração da biblioteca utilizada para simulação (_CCMC.so) deve ser feita no módulo config.py na função kameleon_lib_path(). Para a configuração de um determinado diretório  path/to/kameleon/lib/python2.7/site-packages/ccmc/ , a função deverá ser

def kameleon_lib_path():
    kameleon_path = 'path/to/kameleon/lib/python2.7/site-packages/ccmc/‘
    return kameleon_path

A configuração para acesso aos modelos deverá ser feita no modulo config.py na função models_path(). Para a configuração de um determinado diretório path/to/models , a função deverá ser

def models_path():
    models_path = 'path/to/models'
    return models_path

Atualmente o banco de dados está implementado em MySQL e configurado no arquivo app.py, indicado por #Config MySQL. No momento há de ser criado duas tabelas dentro de um Databank: users e dados

- users: Banco de dados de registro de usuários. Nele contém as colunas:
	- id: INT(11), PRIMARYKEY, AUTO_INCREMENT
	- name: VARCHAR(100), NULL
	- email: VARCHAR(100), NULL
	- username: VARCHAR(30), NULL
	- password: VARCHAR(100), NULL
	- register_date: TIMESTAMP, NOT NULL, CURRENT_TIMESTAMP

- dados: Banco de dados de registros de simulações. Nele contém as colunas:
	- id: INT(11), NOT NULL, PRIMARYKEY, AUTO_INCREMENT
	- title: VARCHAR(255), NULL
	- type: VARCHAR(100), NULL
	- user: VARCHAR(100), NULL
	- body: TEXT, NULL
	- create_date: TIMESTAMP, NOT NULL, CURRENT_TIMESTAMP
	- dados: TEXT, NULL
	- modelo: VARCHAR(50), NULL
	- IMAGE: blob, NULL

A configuração de nome de usuário e senha devem ser feitas nas máquinas e então configuradas em app.py. Para a criação da tabela dados, entrar o comando:
CREATE TABLE dados (id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), type VARCHAR(100), user VARCHAR(100), body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, dados TEXT, modelo VARCHAR(50), IMAGE BLOB);
Para a criação da tabela users: 
CREATE TABLE dados (id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
——————————————————————————————————————————————————————————————————

Gamma Jr. Engenharia
gammajrengenharia@gmail.com