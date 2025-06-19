# **Proyecto de Control de Aforo en la Playa de Es Trenc**

## **Resumen Ejecutivo**

Este documento describe el desarrollo e implementación de un sistema inteligente de control de aforo para la Playa de Es Trenc (Mallorca), como solución tecnológica orientada a la gestión de espacios naturales protegidos con gran afluencia de visitantes.

## **Objetivo del Proyecto**

El objetivo principal ha sido diseñar e implementar un sistema IoT de conteo automatizado que permite:

- Controlar el aforo en accesos de personas a la playa.
- Monitorizar la ocupación del aparcamiento de vehículos.
- Ofrecer datos en tiempo real a través de una plataforma IoT centralizada (IoTIB).
- Garantizar sostenibilidad, privacidad y operatividad a largo plazo en entornos naturales.

---

## **Tecnologías y Arquitectura Utilizadas**

- **LoRa (Long Range Radio)** para la transmisión eficiente de datos desde ubicaciones remotas.
- **Dispositivos Bosch 7000i y 8000i** para videovigilancia inteligente con analítica embebida.
- **Sensores infrarrojos** para detección bidireccional de paso humano.
- **Raspberry Pi** como unidad de procesamiento local.
- **Plataforma IoTIB** para visualización y gestión remota de datos.
- Scripts y lógica personalizados desarrollados en Python.

---

## **Infraestructura Instalación**

Se han desplegado los siguientes dispositivos en puntos estratégicos:

- **Colònia de Sant Jordi (entrada Na Tirapel)**: Cámaras Bosch para conteo de personas.
- **Aparcamiento de la Salinera**: Cámaras Bosch para conteo de vehículos.
- **Acceso de Ses Covetes**: Doble sensor infrarrojo para conteo de peatones en ambos sentidos.

El sistema no almacena imágenes ni identifica personas o vehículos, garantizando un tratamiento completamente anónimo de los datos.

---

## **Funcionamiento General del Sistema**

1. **Captura de datos** mediante cámaras con analítica de vídeo y sensores infrarrojos.
2. **Procesamiento local** a través de Raspberry Pi.
3. **Envío de datos** a la plataforma IoTIB vía transmisores LoRa (Dragino y Milesight).
4. **Visualización en tiempo real** del aforo y estadísticas mediante interfaz web.

---

## **Componentes del Sistema y Carpetas Asociadas**

### 📂 `Distribució_camares/`  
Contiene el esquema de ubicación y distribución de las cámaras en el entorno.

### 📂 `Raspberry/`  
Incluye toda la lógica de scripts para recogida y transmisión de datos, subdividida por tipo de transmisor.

- **`Raspberry/scripts_dragino/`**  
  Scripts específicos para la comunicación con transmisores Dragino vía RS485.

- **`Raspberry/scripts_milesight/`**  
  Scripts de envío para dispositivos Milesight configurados con ToolBox.

### 📂 `Dragino/`  
Guía paso a paso para la configuración y carga del firmware a transmisores Dragino mediante Arduino IDE.

### 📂 `Milesight/`  
Documentación y configuraciones necesarias para la puesta en marcha de transmisores Milesight a través de ToolBox.

### 📂 `IR/`  
Documentación técnica sobre los sensores infrarrojos instalados: principios de funcionamiento, instalación y parámetros de calibración.

---

## **Configuración Técnica: Dispositivos y Software**

### **Cámaras Bosch (7000i / 8000i)**

- Herramientas: **Configuration Manager** y **Project Manager**.
- Calibración precisa de altura, dirección y creación de líneas de conteo mediante perfiles VCA.
- Sistema inteligente de analítica de vídeo con 32 perfiles editables.
- Acceso por interfaz web mediante IP estática (usuario: `service`).

### **Raspberry Pi**

- Sistema operativo: Raspbian.
- Interfaz Ethernet para conexión con cámaras.
- Comunicación serial RS485 con el transmisor LoRa.
- Scripts en Python para recolección y envío de datos periódicos.

### **Transmisores LoRa**

- **Dragino** (Clase A): Recibe downlinks solo tras enviar uplinks (cada 10 minutos).
- **Milesight** (Clase C): Comunicación continua. Puede recibir instrucciones en cualquier momento excepto durante uplink.

---

## **Integración con la Plataforma IoTIB**

### **Envío de Datos (Uplink)**

- Formato de datos: hexadecimal.
- Separador entre valores: `FF` (hex: 4646).
- Ejemplo de trama: `303146463234464632` → Datos útiles: `01 FF 24 FF 2`.

El sistema puede interpretar estos valores y asociarlos al número de personas o vehículos según la ubicación del dispositivo.

### **Recepción de Instrucciones (Downlink)**

- Usado exclusivamente para **actualización horaria del sistema**.
- Formato:
  - **Milesight**: hexadecimal (ej. `12:30` → `31323330`), puerto 2.
  - **Dragino**: decimal (`12:30` → `1230`), puerto 1 (efectivo tras uplink).

---

## **Resultados Obtenidos**

✅ Instalación funcional y operativa.  
✅ Datos en tiempo real accesibles desde plataforma IoTIB.  
✅ Sistema no intrusivo ni invasivo, totalmente anónimo.  
✅ Bajo mantenimiento y alta escalabilidad.  

