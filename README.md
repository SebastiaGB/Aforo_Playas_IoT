# 📍 Proyecto de Control de Aforo en Espacio Natural (Versión Técnica Demostrativa)

> ⚠️ Este repositorio documenta una **recreación técnica basada en un proyecto real** desarrollado durante mi experiencia profesional como técnico IoT en colaboración con una entidad pública.  
> Todo el contenido ha sido adaptado para proteger datos sensibles, pero representa fielmente la arquitectura y lógica funcional implementadas.

---

## 🎯 Objetivo del Proyecto

Diseñar y desplegar una solución IoT de conteo automatizado de personas y vehículos para gestionar el aforo en un entorno natural protegido.  

El sistema tenía como objetivos:

- Controlar el acceso peatonal en varios puntos de entrada.
- Monitorizar el aparcamiento de vehículos.
- Enviar datos en tiempo real a una plataforma de gestión centralizada.
- Garantizar privacidad, sostenibilidad y operatividad en condiciones remotas.

---

## 🧱 Arquitectura y Tecnologías

- **LoRaWAN** para transmisión remota eficiente.
- **Cámaras Bosch IP (7000i / 8000i)** con analítica embebida.
- **Sensores infrarrojos bidireccionales** para conteo peatonal.
- **Raspberry Pi** como gateway local + scripts en Python.
- Plataforma externa para visualización de datos (**IoTIB** en el proyecto real).
- Transmisores **Dragino** (Clase A) y **Milesight** (Clase C).

---

## ⚙️ Funcionamiento General

1. 📸 Captura de eventos mediante sensores y cámaras.
2. 🧠 Procesamiento en Raspberry Pi: recolección, filtrado, formateo.
3. 📡 Envío de datos a plataforma central vía LoRa.
4. 🌐 Visualización en tiempo real mediante interfaz web.

---

## 🗂️ Organización del Repositorio

### 📂 `Distribucion_camaras/`
Esquemas de ubicación y lógica de instalación de los dispositivos.

### 📂 `Raspberry/`
Scripts principales de operación. Subdivididos por transmisor:

- `scripts_dragino/` — comunicación vía RS485 con Dragino.
- `scripts_milesight/` — configuración y comunicación con Milesight.

### 📂 `Dragino/`
Pasos para flasheo y configuración del transmisor Dragino mediante Arduino IDE.

### 📂 `Milesight/`
Guía de configuración con la herramienta ToolBox (software oficial).

### 📂 `IR/`
Documentación técnica de sensores infrarrojos: instalación, calibración, parámetros.

---

## 🧰 Configuración Técnica

### 📷 Cámaras Bosch (7000i / 8000i)

- Configuración vía **Configuration Manager**.
- Creación de líneas de conteo con perfiles VCA.
- IP estática, acceso por interfaz web (`usuario: service`).
- Analítica embebida sin almacenamiento de vídeo.

### 🖥️ Raspberry Pi

- Sistema: Raspbian.
- Ethernet hacia red de cámaras.
- Puerto serie RS485 hacia transmisor LoRa.
- Scripts en Python para adquisición y envío programado.

### 📡 Transmisores LoRa

- **Dragino (Clase A)**: solo recibe mensajes tras enviar (uplink → downlink).
- **Milesight (Clase C)**: escucha permanente (menos en momento de envío).

---

## 🔄 Integración con Plataforma IoT

### 📤 Envío de datos (uplink)

- Formato: hexadecimal.
- Separador: `FF` (hex `4646`).
- Ejemplo: `303146463234464632` → `01 FF 24 FF 2` (personas o vehículos).

### 📥 Recepción de instrucciones (downlink)

Usado principalmente para **sincronizar la hora** de los dispositivos.

- **Milesight**: formato hexadecimal (`12:30` → `31323330`), puerto 2.
- **Dragino**: decimal (`12:30` → `1230`), puerto 1 (tras uplink).

---

## ✅ Resultados Destacados

- ✔️ Sistema instalado y funcional en condiciones reales.
- ✔️ Datos accesibles en tiempo real desde plataforma externa.
- ✔️ Anonimato garantizado (no se capturan ni almacenan imágenes).
- ✔️ Bajo consumo, autonomía solar y alta robustez operativa.
- ✔️ Mínimo mantenimiento, fácil replicabilidad.

---

## 🔐 Nota de Ética

> Este documento es una **reconstrucción técnica no confidencial** basada en mi participación real en un proyecto profesional.  
> Todo el código, documentación y arquitectura ha sido adaptado, anonimizando nombres, IPs y configuraciones específicas para proteger la privacidad del entorno y la entidad promotora.

