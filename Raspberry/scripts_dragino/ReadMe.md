# 📊 Lectura, envío y reinicio de contadores Bosch vía API y puerto serie

> ⚠️ Este proyecto es una **versión demostrativa y anonimizada** basada en una solución real.  
> No contiene datos confidenciales, contraseñas ni endpoints reales.  
> Ideal para entornos IoT con Raspberry Pi + dispositivos serie (como gateways Dragino).

---

## 📁 Estructura general

Este repositorio incluye dos scripts principales:

- `lecturacontadors.py`: se conecta a una cámara Bosch IP, lee los contadores vía API y los envía por puerto serie a otro dispositivo.
- `reiniciarcontadors.py`: reinicia remotamente los contadores de la cámara mediante una petición HTTP.

Además, es necesario un archivo `.txt` donde se almacenarán los valores históricos de los contadores.

---

## 🛠️ Requisitos previos

Antes de ejecutar los scripts:

1. Crea un archivo `.txt` en la Raspberry Pi para guardar los datos de los contadores.
2. Copia la **ruta completa** del archivo y pégala en el lugar del código donde se indique `ruta/a/fitxer.txt`.
3. Asegúrate de que las cámaras Bosch estén accesibles desde la red local.

---

## ⚙️ Parámetros a configurar

### 🔧 En `lecturacontadors.py`

- **Línea 12:** `usuario` – nombre de usuario de acceso a la cámara.
- **Línea 13:** `contraseña` – contraseña de acceso a la cámara.
- **Línea 16:** `direccion_ip` – IP de la cámara Bosch.
- **Línea 85:** `ruta_fichero` – ruta al archivo donde guardar los valores.
- **Línea 161:** `puerto_serie` – puerto serie al que se conecta el gateway.

### 🔧 En `reiniciarcontadors.py`

- **Línea 8:** `usuario` – nombre de usuario de acceso a la cámara.
- **Línea 9:** `contraseña` – contraseña de acceso.
- **Línea 12:** `direccion_ip` – IP de la cámara Bosch.

---

## 🧠 Descripción de funcionamiento

### `lecturacontadors.py`

Script principal para adquisición y envío de datos:

#### 🔹 `get_response(url)`
Hace una petición HTTPS GET autenticada a la cámara.  
Incluye esta línea para desactivar advertencias de certificados SSL autofirmados:

      warnings.filterwarnings("ignore")

### 🔹 `decode_xml_response(xml_response)`
- Extrae y limpia la cadena XML.
- Determina el número de contadores.
- Verifica su integridad.
- Convierte cada contador de hexadecimal a decimal.
- Retorna una lista de contadores.

### 🔹 `set_system_time(datetime_str)`
- Actualiza la hora del sistema de la Raspberry usando una cadena de fecha/hora.

### 🔹 `guardar_contadores_en_txt(counters)`
- Abre el archivo `.txt` en modo append.
- Guarda cada contador con marca de tiempo.

### 🔹 `enviar_serie(counters, ser)`
- Convierte los contadores en cadena codificada.
- Añade separadores y final de línea.
- Envía el mensaje por el puerto serie.

### 🔹 `escuchar_serie(ser)`
- Escucha el puerto serie hasta 15 segundos.
- Si recibe una cadena de **4 caracteres** (`HHMM`): actualiza la hora.
- Si recibe **14 caracteres** (`YYYYMMDDHHMMSS`): actualiza la fecha completa.

### 🔹 Bucle principal
- Se obtiene respuesta desde la cámara.
- Se abre el puerto serie.
- Se decodifican contadores (o se definen como `[0, 0, 0]` si falla).
- Se envían por puerto serie.
- Se escuchan respuestas.
- Se guardan en el archivo `.txt`.

---

### 🔄 `reiniciarcontadors.py`

Este script realiza una solicitud HTTP autenticada a la cámara Bosch para reiniciar los contadores a `0`.  
Usa el comando `0x0b4a` sobre el endpoint correspondiente a través de la API RCP.

---

### 📌 Observaciones

- Este sistema fue pensado para ejecutarse de forma autónoma y periódica en una **Raspberry Pi**.
- Compatible con cámaras **Bosch IP** que soporten comandos **RCP**.
- El puerto serie puede conectarse a un dispositivo como **Dragino** o cualquier módulo **LoRa/RS-485** compatible.

---

### 🔐 Seguridad

> Este código está adaptado con fines educativos y de portfolio.  
> No incluye IPs, contraseñas ni referencias a proyectos privados.  
> Los datos reales deben ser reemplazados por configuraciones personalizadas según el entorno de despliegue.

