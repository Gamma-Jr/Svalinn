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

Futuramente será implementado um banco de dado para que o usuário possa configurar os caminhos aos modelos e ao modulo _CCMC.so através da própria interface.

——————————————————————————————————————————————————————————————————

Gamma Jr. Engenharia
gammajrengenharia@gmail.com