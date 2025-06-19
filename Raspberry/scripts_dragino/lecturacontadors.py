# coding: utf-8

from datetime import datetime
import re
import subprocess
import sys
import requests
import xml.etree.ElementTree as ET
import warnings
import time
import serial

# Ignorar advertencies SSL
warnings.filterwarnings("ignore")

# Credencials
username = "service"
password = "<password>"

# URL de la càmara Bosch IP y comanda para obtenir els valores de els contadores IVA
url_iva_counter_values = "https://<direcció_ip>/rcp.xml?command=0x0b4a&type=P_OCTET&direction=READ"

# Funció per obtenir la resposta HTTP
def get_response(url):
    try:
        # Enviar solicitud HTTPS GET amb credencials
        response = requests.get(url, auth=(username, password), verify=False)
        # Verificar si la solicitud té èxit
        if response.status_code == 200:
            # Retornar la resposta en binari
            return response.content
    except requests.exceptions.ConnectionError as e:
        e 
############################################################
# Funció per a decodificar la resposta XML
def decode_xml_response(xml_response):
    try:
        # Parsear el XML
        root = ET.fromstring(xml_response)

        # Extreure la longitud i la cadena de la secció 'result'
        len_value = int(root.find("./result/len").text)
        str_value = root.find("./result/str").text
        
        # Eliminar els espais en blanc de la cadena
        str_value = str_value.replace('\n', '').replace('\r', '').replace(' ', '')

        # Verificar la longitud de la cadena
        expected_length = int(len_value)
        number_counters = str_value[:2]
        number_counters_dec = int(number_counters, 16)

        if number_counters_dec * 70 + 1 != expected_length:
            return []

        # Decodificar els contadores de dades
        counters = []

        if len_value == 1:
            counters = [0,0,0]

        else:
            offset = 2  # El primer byte representa el nombre de contadors que hi ha
            while offset < len(str_value):
                counter_data = str_value[offset:offset + 140]
                counter_value = int(counter_data[128:140], 16)
                counters.append(counter_value)
                offset += 140

        # Retornar els contadors
        return counters

    except Exception as e:
        e
        return []
    
############################################################
def set_system_time(datetime_str):
    try:
        # Executar comanda per a canviar hora a la raspberry
        subprocess.run(['sudo', 'date', '-s', datetime_str], check=True)
    except subprocess.CalledProcessError as e:
        e

############################################################
# Métode per a guardar els contadros a un arxiu de texte
def guardar_contadores_en_txt(counters):
    try:
        # Especificar el nom de l'arxiu
        nombre_archivo = "<ruta/a/fitxer.txt>"
        # Obrir arxiu en mode append
        with open(nombre_archivo, 'a') as archivo:
            # Obtenir i formatetjar data actual
            date_time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            for counter in counters:
                archivo.write("\nValor: " + str(counter) + ", Fecha: " + date_time_string)
            archivo.write("\n")

    except Exception as e:
        e

############################################################
#Métode per enviar dades pel port serie
def enviar_serie(counters,ser):

    try:

        # Construir el missatge concatenat
        separador = "FF" 
        mensaje = separador.join([str(counter) for counter in counters])  

        # Enviar el missatge concatenat
        comando = (mensaje)+"\n"  #<LF> final
        ser.write(comando.encode('utf-8'))  # Enviar 

    except serial.SerialException as e:
        e
    except Exception as e:
        e 

############################################################
#Mètode per llegir dades per serie
def escuchar_serie(ser):
    
    try:
        start_time = time.time()

        while True:
            if ser.in_waiting > 0:
                # Llegir dades
                data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
                print(data)
                # Agafar sols la informació de la finestra RX
                matches = re.findall(r'RX: "([^"]*)"', data)
                for match in matches:
                    try:
                        # Si aquesta són 4 dígits
                        if len(match) == 4:
                            # Convertir a un data time
                            dt = datetime.strptime(match, '%H%M')
                            # Obtenir la data actual
                            now = datetime.now()
                            # Combinar la data actual amb la data extreta
                            combined_dt = datetime(year=now.year, month=now.month, day=now.day, hour=dt.hour, minute=dt.minute)
                            # Formatejar en format YYYY-MM-DD hh:mm:ss
                            datetime_str = combined_dt.strftime('%Y-%m-%d %H:%M:%S')
                            # Actualitzar data
                            set_system_time(datetime_str)
                            return
                        # Si aquesta són 14 dígits 
                        if len(match) == 14:
                            # Convertir a un data time
                            dt = datetime.strptime(match, '%Y%m%d%H%M%S')
                            # Formatejar en format YYYY-MM-DD hh:mm:ss
                            datetime_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                            # Actualitzar data
                            set_system_time(datetime_str)
                            return
                        else:
                            match
                            return
                    except ValueError:
                            match
                            return
                    
            if time.time() - start_time > 15:
                return
            
    except Exception as e:
        e 
    finally:
        ser.close()

############################################################
# Obtener la resposta a la petició de la càmara
response_bytes = get_response(url_iva_counter_values)

# port serie
puerto_serial = '<port_dragino>'

# Baudrate
baudrate=115200

# Obrir port serie
ser = serial.Serial(puerto_serial, baudrate, timeout=1)

if response_bytes:

    # Decodificar la resposta como una cadena XML
    xml_response = response_bytes.decode()

    # Decodificar la resposta XML
    counters = decode_xml_response(xml_response)

else:

    # Obtenir contadors buits si la càmara no contesta
    counters = [0,0,0]

# Enviar dades per LoRa
enviar_serie(counters, ser)

# Escoltar dades per LoRa
escuchar_serie(ser) 

# Crear i escriure el arxiu txt
guardar_contadores_en_txt(counters)
    

