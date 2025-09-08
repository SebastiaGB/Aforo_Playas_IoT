# Lectura y sincronización de contadores Bosch vía API y puerto serie

> ⚠️ Este proyecto es una recreación técnica con fines demostrativos basada en una solución desarrollada profesionalmente. No contiene información confidencial ni enlaces reales.

---

## 📁 Estructura general

Este repositorio incluye dos scripts en Python para:

- Obtener datos de cámaras Bosch mediante su API RCP.
- Guardar y reenviar esos datos a través del puerto serie a un dispositivo externo.
- Permitir tareas como sincronizar la hora del sistema o reiniciar contadores remotamente.

Además, requiere un archivo `.txt` (cuyo nombre y ruta puedes definir) que actuará como base de datos local para guardar los registros.

---

## ⚙️ Configuración necesaria

### `milesight_controller.py`

- `puerto_serie`: puerto serie donde está conectado el dispositivo
- `usuario`: nombre de usuario de acceso a la cámara
- `contraseña`: contraseña de acceso a la cámara
- `direccion_ip`: dirección IP del dispositivo Bosch
- `ruta_fichero`: ruta al archivo local `.txt` donde guardar los contadores

### `reiniciarcontadors.py`

- `usuario`: nombre de usuario de acceso a la cámara
- `contraseña`: contraseña de acceso a la cámara
- `direccion_ip`: dirección IP del dispositivo

---

## ¿Qué hace cada script?

### `milesight_controller.py`

Este script realiza las siguientes funciones:

1. **Conexión a la cámara**
   - Realiza una petición HTTPS autenticada para obtener la respuesta XML.
   - Extrae los contadores a partir de una cadena codificada.

2. **Decodificación de contadores**
   - Analiza la respuesta XML, calcula cuántos contadores hay y verifica su integridad.
   - Convierte cada uno en decimal y los guarda en una lista.

3. **Guardado en archivo**
   - Escribe los valores con marca de fecha/hora en un archivo `.txt`.

4. **Comunicación por puerto serie**
   - Envío periódico de contadores al dispositivo conectado.
   - Gestión de errores (envía `0xFF 0xFF` si no hay datos válidos).
   - Sistema de semáforos para sincronizar envíos y lecturas.

5. **Recepción por puerto serie**
   - Escucha continua del puerto serie.
   - Si se reciben ciertos comandos (fechas u horas), sincroniza la hora del sistema.

6. **Automatización**
   - Usa `schedule` para ejecutar el envío cada 10 minutos.
   - Utiliza hilos (`threads`) para ejecutar el scheduler y la escucha en paralelo.

---

### `reiniciarcontadors.py`

- Realiza una petición HTTPS autenticada a la API de la cámara para **resetear los contadores a cero**.

---

## 🖥️ Requisitos

- Raspberry Pi con Python 3 instalado
- Acceso a red con las cámaras Bosch
- Archivo `.txt` donde se guardarán los registros

---

## ✅ Conclusión

Este sistema permite:

- Monitorización periódica de contadores en cámaras Bosch
- Envío fiable por puerto serie
- Automatización en Raspberry Pi
- Sincronización remota del reloj del sistema

Está optimizado para ejecutarse en segundo plano de forma autónoma y segura.

---

> ⚠️ Esta es una versión modificada y despersonalizada del código original utilizado en un proyecto real. No contiene datos ni configuraciones privadas.
