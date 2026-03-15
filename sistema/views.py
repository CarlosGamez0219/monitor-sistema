import platform
import psutil
from django.shortcuts import render


def obtener_datos_sistema():
    datos = {}

    # CPU
    try:
        datos['cpu_porcentaje'] = psutil.cpu_percent(interval=1)
        datos['cpu_nucleos'] = psutil.cpu_count(logical=True)
    except Exception:
        datos['cpu_porcentaje'] = 'No disponible'
        datos['cpu_nucleos'] = 'No disponible'

    # RAM
    try:
        ram = psutil.virtual_memory()
        datos['ram_total'] = round(ram.total / (1024 ** 3), 2)
        datos['ram_usado'] = round(ram.used / (1024 ** 3), 2)
        datos['ram_libre'] = round(ram.available / (1024 ** 3), 2)
        datos['ram_porcentaje'] = ram.percent
    except Exception:
        datos['ram_total'] = datos['ram_usado'] = datos['ram_libre'] = datos['ram_porcentaje'] = 'No disponible'

    # Disco
    try:
        disco = psutil.disk_usage('/')
        datos['disco_total'] = round(disco.total / (1024 ** 3), 2)
        datos['disco_usado'] = round(disco.used / (1024 ** 3), 2)
        datos['disco_libre'] = round(disco.free / (1024 ** 3), 2)
        datos['disco_porcentaje'] = disco.percent
    except Exception:
        datos['disco_total'] = datos['disco_usado'] = datos['disco_libre'] = datos['disco_porcentaje'] = 'No disponible'

    # Sistema operativo
    try:
        datos['sistema_os'] = platform.system()
        datos['version_os'] = platform.version()
        datos['arquitectura'] = platform.machine()
    except Exception:
        datos['sistema_os'] = datos['version_os'] = datos['arquitectura'] = 'No disponible'

    return datos


def index(request):
    datos = obtener_datos_sistema()
    return render(request, 'sistema/index.html', {'datos': datos})