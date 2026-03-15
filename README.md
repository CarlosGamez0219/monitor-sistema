# 🖥️ Monitor del Sistema

Aplicación web desarrollada con Django y psutil que muestra en tiempo real el estado del sistema: CPU, RAM, disco duro y sistema operativo.

---

## 👥 Integrantes del Grupo 3

| Nombre Completo | Número de Cuenta |
|----------------|-----------------|
| Carlos Gámez   | 202310010912    |
| Elsa Meza      | 202220010096    |
| Nabil Reyes    | 202210010831    |

---

## 📋 Requisitos

- Python 3.11+
- pip
- Docker

---

## 🚀 Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/CarlosGamez0219/monitor-sistema.git
cd monitor-sistema
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor

```bash
python manage.py runserver
```

### 5. Abrir en el navegador

```
http://127.0.0.1:8000
```

---

## 🐳 Ejecución con Docker

```bash
docker-compose up --build
```

Luego abrir: http://localhost:8000

---

## 📁 Estructura del proyecto

```
monitor-sistema/
├── monitor/
│   ├── settings.py       # Configuración del proyecto Django
│   ├── urls.py           # URLs principales
│   └── wsgi.py
├── sistema/
│   ├── views.py          # Lógica de recolección con psutil
│   ├── urls.py           # URLs de la app
│   └── templates/
│       └── sistema/
│           └── index.html  # Interfaz web
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧩 Componentes principales

### views.py
Contiene la función `obtener_datos_sistema()` que usa psutil para recolectar CPU, RAM, disco y datos del sistema operativo. Maneja errores con try/except para evitar fallos si psutil no puede obtener algún dato.

### index.html
Plantilla Django que muestra los datos en tarjetas con barras de progreso. Se actualiza automáticamente cada 30 segundos con JavaScript y también cuenta con un botón de actualización manual.

### psutil
Librería externa de Python que permite acceder a información del sistema como uso de CPU, memoria, disco y red.