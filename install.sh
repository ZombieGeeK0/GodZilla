
clear
echo ====================================================================================================
echo [?] Instalando...
echo ====================================================================================================
sudo su && sudo apt-get update && apt-get install git -y && sudo apt-get install python3 && pip3 install webbrowser && pip3 install colorama && sudo apt-get install python3-pip && git clone https://github.com/sherlock-project/sherlock && git clone https://github.com/sqlmapproject/sqlmap
echo ====================================================================================================
echo [?] Requerimientos instalados.
