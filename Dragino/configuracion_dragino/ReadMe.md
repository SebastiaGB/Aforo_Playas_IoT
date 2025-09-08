# Configuración del Transmisor Dragino con Arduino

Este repositorio contiene el código y recursos necesarios para configurar un transmisor **Dragino LoRaWAN** como parte de un sistema de conteo de personas y vehículos en entornos naturales, integrando dispositivos IoT con la plataforma IoTIB.

> 🔐 **Nota:** Todo el contenido aquí incluido está adaptado con fines técnicos y educativos. No contiene credenciales privadas.

---
## ⚙️ Configuración del Dispositivo

Parámetros usados para configurar el Dragino:

- **Modo:** OTAA
- **Clase:** A
- **ADR (Adaptative Data Rate):** OFF
- **SF (Spreading Factor):** 12 – máximo alcance

---

## 🛠️ Instalación del Entorno (Arduino IDE)

1. Instalar [Arduino IDE](https://www.arduino.cc/en/software).
2. Conectar el Dragino al PC mediante USB.
3. Desde el *Board Manager*:
   - Instalar `Arduino AVR Boards`
   - Instalar `Seeed SAMD Boards`
4. Seleccionar en `Herramientas > Placa`: **Seeeduino LoRaWAN**
5. Seleccionar en `Herramientas > Puerto` el puerto donde esté conectado (ver en "Administrador de dispositivos" del sistema operativo).
6. Instalar la librería **LoRaWAN** desde el *Library Manager* o incluir las de la carpeta `libraries/`.

---

## 🔑 Configuración del Código (`script_dragino.ino`)

### 🧩 setup()

Se ejecuta al iniciar el dispositivo:

- Inicia el puerto serie a ... baudios.
- Define claves OTAA: `DevEUI`, `AppEUI`, `AppKey`.
- Establece:
  - Data Rate 0 (SF12)
  - ADR desactivado
  - Región EU868
  - Clase A
- Intenta unirse a la red (`join`), reintentando cada 10 segundos si falla.

### 🔄 loop()

- Escucha datos del puerto serie.
- Si recibe una línea (`\n`), la transmite por LoRa (`lora.transferPacket()`).
- Permite también recibir **downlinks**.
- Limpia el buffer tras cada envío para evitar desbordamientos.

---


