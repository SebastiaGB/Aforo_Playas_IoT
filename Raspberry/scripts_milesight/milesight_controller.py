# 📡 Sistema de lectura y envío de contadores vía API y puerto serie

> ⚠️ Este script es una **recreación técnica anónima y adaptada** con fines demostrativos. No incluye contraseñas, direcciones IP ni configuraciones reales utilizadas en entornos de producción.

---

## 📝 Descripción general

Este script está diseñado para ejecutarse en un sistema tipo **Raspberry Pi**, y su objetivo es:

- Obtener valores de contadores desde una **cámara con API HTTP/XML** (por ejemplo, Bosch).
- Decodificar la respuesta XML y procesar los datos.
- Enviar los datos por **puerto serie** a otro dispositivo (por ejemplo, un nodo LoRa o Gateway).
- Sincronizar la hora del sistema en función de datos recibidos externamente.
- Guardar un histórico en un archivo `.txt`.

---

## ⚙️ Componentes principales

### 🔐 Conexión a la cámara

- Se realiza una petición HTTPS a una API local utilizando autenticación básica.
- Se ignoran advertencias de SSL (útil para entornos con certificados autofirmados).
- Se procesa la respuesta XML para extraer los contadores codificados.

### 📤 Envío por puerto serie

- El script configura el puerto serie (puerto + baudrate).
- Cada cierto intervalo (10 min), recoge los contadores y los convierte en un mensaje binario.
- Si no hay datos válidos, se envía un código de error (`0xFF 0xFF`).

### 💾 Guardado en archivo local

- Cada lectura válida se almacena en `counters.txt`, con fecha y hora.

### 🧭 Sincronización de hora

- Si se recibe una cadena de 14 dígitos (ej. `20240619120500`), el sistema actualiza su fecha y hora.
- Si se recibe una cadena de 4 dígitos (ej. `1205`), actualiza solo la hora del sistema.

### 🔁 Automatización y multitarea

- Se usa la librería `schedule` para ejecutar tareas periódicas.
- Todo el funcionamiento (escucha + envío) se realiza en hilos (`threads`) paralelos.
- Se implementa un **semaforo** para evitar colisiones de lectura/escritura en el puerto serie.

---

## 🛠️ Requisitos

- Python 3
- Raspberry Pi (u otro equipo con Linux y acceso a serie)
- Librerías: `requests`, `schedule`, `serial`, `xml`, `subprocess`, `threading`, etc.

Instalación de dependencias (ejemplo):

```bash
pip install pyserial schedule requests
