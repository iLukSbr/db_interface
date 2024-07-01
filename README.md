# Database Interface
MySQL/PostgreSQL database GUI with credentials save/encryption, database/table selector, table exporter to .csv or .json, query field, .sql dump, .dbml generator and ERD diagram .svg visualizer and exporter.

# Funcionalidades
- Visualização de tabelas;
- Digitação de consultas SQL em DML (Data Manipulation Language);
- Dump das tabelas para arquivos .sql;
- Conversão .sql para .dbml;
- Geração de diagrama físico das tabelas;
- Exportação das tabelas para .csv e .json;
- Exportação do diagrama para .svg.

# Download (terminal)

git pull https://github.com/iLukSbr/db_interface

# Versões de programas necessários
- MySQL Community Server 8.4.0 LTS;
- PostgreSQL 16.3;
- Node.js 20.14.0;
- Python 3.12.

# Instalações no Linux (terminal):
- Python:

apt install software-properties-common -y

add-apt-repository ppa:deadsnakes/ppa

apt update

apt install python3.12

curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12 

sudo apt-get install libpython3.12-dev

- Node:

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

nvm install 20

- PostgreSQL:

sudo apt install postgresql

- MySQL:

sudo apt install mysql-server

- apt-get:

sudo apt-get install zenity libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

- apt:

sudo apt install wine libmpv1

# Instaladores para Windows:
- Node: https://nodejs.org/en/download/prebuilt-installer
- Python: https://www.python.org/downloads/
- MySQL: https://dev.mysql.com/downloads/mysql/
- PostgreSQL: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

# Instalações em ambos, Linux e Windows (terminal):
- Pip:

pip install flet cryptography pymysql psycopg2-binary pandas pyinstaller cffi datetime

- Node packages (antes mova o diretório ativo para a pasta do projeto):

npm install @dbml/core @softwaretechnik/dbml-renderer

# Compilação no Linux (terminal):
pyinstaller --onefile --add-data "mysql2dbml.js:." --add-data "postgres2dbml.js:." main.py

cp postgres2dbml.js dist

cp mysql2dbml.js dist

# Compilação no Windows (terminal):
pyinstaller --onefile --add-data "mysql2dbml.js;." --add-data "postgres2dbml.js;." main.py

copy postgres2dbml.js dist

copy mysql2dbml.js dist

# Execução em ambos, Linux e Windows (terminal):
cd dist

./main
