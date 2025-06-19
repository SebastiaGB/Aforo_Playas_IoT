# 🚀 Dragino – Configuración del Transmisor LoRa

> Este directorio contiene la configuración y scripts necesarios para el funcionamiento de transmisores **Dragino** mediante **Arduino IDE**.

---

## 🔗 Documentación Oficial

Consulta las especificaciones y guía técnica del modelo en la wiki de Seeed Studio:

🔗 [Ver documentación oficial Dragino](https://wiki.seeedstudio.com/Seeeduino_LoRAWAN/)


---

## ⚙️ Parámetros de Configuración

El dispositivo Dragino ha sido configurado con los siguientes parámetros LoRaWAN:

- **Modo**: OTAA  
- **Clase**: A  
- **ADR**: Off  
- **Spreading Factor (SF)**: 12  

---

## 💻 Instalación y Configuración en Arduino IDE

Para la correcta configuración del dispositivo Dragino, se ha utilizado el entorno **Arduino IDE** siguiendo estos pasos:

1. Instalar el **Arduino IDE** desde [arduino.cc](https://www.arduino.cc/en/software).
2. Conectar el Dragino al ordenador mediante **cable USB**.
3. Instalar desde el **Board Manager**:
   - `Arduino AVR Boards`
   - `Seeed SAMD Boards`
4. En el menú `Herramientas`:
   - Seleccionar la placa: `Seeeduino LoRaWAN`.
   - Seleccionar el puerto correspondiente al dispositivo conectado.
5. Instalar la librería **LoRa** desde el `Library Manager`.
6. Cargar el script de configuración desde la carpeta del proyecto.

📁 **Ruta útil**:  
Dentro del repositorio, la carpeta `configuracion_dragino/` contiene:

- Scripts de configuración para los dispositivos Dragino.
- Guía detallada paso a paso para la carga y prueba de firmware.

---

## 🧠 Nota Técnica

Para identificar el puerto correcto en el que está conectado el dispositivo, accede al **Administrador de dispositivos** de tu sistema operativo y busca el apartado **Puertos (COM y LPT)**.


