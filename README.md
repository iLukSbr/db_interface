# Interface de Bancos de Dados
Ferramenta de visualização de bancos de dados.

Download:
git pull https://github.com/iLukSbr/db_interface

# Versões de programas necessários
- MySQL Community Server 8.4.0 LTS;
- PostgreSQL 16.3;
- Node.js 20.14.0;
- Python 3.12.

# Instalações no Linux (terminal):
- Node:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install 20

- PostgreSQL:
sudo apt install postgresql

- MySQL:
sudo apt install mysql-server

- apt-get:
sudo apt-get install zenity libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamerplugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

- apt:
sudo apt install wine libmpv1 

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
