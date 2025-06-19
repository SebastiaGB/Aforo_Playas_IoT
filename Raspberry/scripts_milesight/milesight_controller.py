> ⚠️ Este script es una **recreación técnica anónima y adaptada** con fines demostrativos. No incluye contraseñas, direcciones IP ni configuraciones reales utilizadas en entornos de producción.

import requests 
import xml.etree.ElementTree as ET
import threading
import time
import warnings
import serial
import schedule
import subprocess
from datetime import datetime

# Serial port configuration
SERIAL_PORT = '<puerto_serie>'
BAUDRATE = ...

# Camera credentials and URL
USERNAME = "<usuario>"
PASSWORD = "contraseña"
URL_IVA_COUNTER_VALUES = "https://<dirección_ip>/rcp.xml?command=0x0b4a&type=P_OCTET&direction=READ"

# Ignore SSL warnings
warnings.filterwarnings("ignore")

# Semaphore to synchronize send and listen operations
semaphore = threading.Semaphore(1)

# File path to store counters
FILE_PATH = "counters.txt"

# Function to get current time
def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Function to get data from the camera
def get_camera_data():
    try:
        response = requests.get(URL_IVA_COUNTER_VALUES, auth=(USERNAME, PASSWORD), verify=False)
        if response.status_code == 200:
            xml_response = response.content.decode()
            return decode_xml_response(xml_response)
        else:
            print(f"[{get_current_time()}] Error obtaining data from camera: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"[{get_current_time()}] Exception in camera request: {e}")
        return []

# Function to decode XML response from the camera
def decode_xml_response(xml_response):
    try:
        root = ET.fromstring(xml_response)
        len_value = int(root.find("./result/len").text)
        str_value = root.find("./result/str").text.replace('\n', '').replace('\r', '').replace(' ', '')
        expected_length = int(len_value)
        number_counters = str_value[:2]
        number_counters_dec = int(number_counters, 16)

        if number_counters_dec * 70 + 1 != expected_length:
            return []

        counters = []
        offset = 2
        while offset < len(str_value):
            counter_data = str_value[offset:offset + 140]
            counter_value = int(counter_data[128:140], 16)
            counters.append(counter_value)
            offset += 140
        return counters
    except Exception as e:
        print(f"[{get_current_time()}] Error decoding XML: {e}")
        return []

# Function to save counters into a text file
def save_counters_to_txt(counters):
    try:
        with open(FILE_PATH, 'a') as file:
            date_time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            for counter in counters:
                file.write(f"Value: {str(counter)}, Date: {date_time_string}\n")
    except Exception as e:
        print(f"[{get_current_time()}] Error saving data to file: {e}")

# Function to send data
def send_data(ser):
    try:
        semaphore.acquire()
        counters = get_camera_data()
        if counters:
            message = b''.join([bytes.fromhex(f'{counter:02x}') for counter in counters])
        else:
            message = b'\xFF\xFF'

        ser.write(message)
        print(f"[{get_current_time()}] Data sent: {message.hex()}")

        if counters:
            save_counters_to_txt(counters)  # Save to file

    except serial.SerialException as e:
        print(f"[{get_current_time()}] Error sending data: {e}")
    finally:
        semaphore.release()

# Function to run scheduled tasks
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Function to listen for data continuously
def listen_for_data(ser):
    while True:
        try:
            if semaphore.acquire(blocking=False):
                if ser.in_waiting > 0:
                    data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore').strip()
                    print(f"[{get_current_time()}] Data received: {data}")
                    process_data(data)
            semaphore.release()
        except serial.SerialException as e:
            print(f"[{get_current_time()}] Error receiving data: {e}")
        except Exception as e:
            print(f"[{get_current_time()}] Unexpected error: {e}")
        finally:
            time.sleep(1)

# Function to process received data
def process_data(data):
    try:
        if len(data) == 14 and data.isdigit():
            dt = datetime.strptime(data, '%Y%m%d%H%M%S')
            print(f"[{get_current_time()}] Date/time received: {dt}")
            new_time = dt.strftime('%Y-%m-%d %H:%M:%S')
            subprocess.run(['sudo', 'date', '-s', new_time], check=True)
            print(f"[{get_current_time()}] System time updated to: {new_time}")

        elif len(data) == 4 and data.isdigit():
            dt = datetime.strptime(data, '%H%M')
            now = datetime.now()
            combined_dt = datetime(year=now.year, month=now.month, day=now.day, hour=dt.hour, minute=dt.minute)
            print(f"[{get_current_time()}] Hour received: {combined_dt}")
            new_time = combined_dt.strftime('%Y-%m-%d %H:%M:%S')
            subprocess.run(['sudo', 'date', '-s', new_time], check=True)
            print(f"[{get_current_time()}] System time updated to: {new_time}")

        else:
            print(f"[{get_current_time()}] Unrecognized data: {data}")
    
    except ValueError as e:
        print(f"[{get_current_time()}] Error processing data: {e}")

# Serial port configuration
try:
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
except serial.SerialException as e:
    print(f"[{get_current_time()}] Error opening serial port: {e}")
    ser = None

if ser:
    # Schedule send_data to run every 'X' minutes
    schedule.every('X').minutes.do(send_data, ser)

    # Start scheduler thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # Start send and listen threads
    listen_thread = threading.Thread(target=listen_for_data, args=(ser,), daemon=True)
    listen_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"[{get_current_time()}] Program terminated by user.")
        ser.close()
