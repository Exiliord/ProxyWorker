import os
import subprocess
import sys
import time
import json
from datetime import datetime
import requests
from colorama import Fore, init

init(autoreset=True)

class LogStream:
    def __init__(self, log_file):
        self.log_file = log_file

    def write(self, message):
        if message.strip():  
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"{timestamp} - {message.strip()}"
            with open(self.log_file, 'a') as f:
                f.write(log_message + '\n')
        sys.__stdout__.write(message)

    def flush(self):
        pass


config_file = "config.json"

try:
    with open(config_file, "r") as f:
        config = json.load(f)
        print(Fore.GREEN + f"Configuración cargada desde {config_file}.")
except Exception as e:
    print(Fore.RED + f"Error al cargar el archivo de configuración: {e}")
    exit(1)


proxy_host = config.get("proxy", {}).get("host")
proxy_port = config.get("proxy", {}).get("port")
proxy_user = config.get("proxy", {}).get("user")
proxy_password = config.get("proxy", {}).get("password")
proxy_auth_required = config.get("proxy", {}).get("auth_required", 1)

hellminer_path = config.get("hellminer_path")
pool_url = config.get("pool_url")
username = config.get("username")
password = config.get("password")
cpu_count = config.get("cpu_count")
log_file_path = config.get("log_file")


if not all([proxy_host, proxy_port, hellminer_path, pool_url, username, password, cpu_count]):
    print(Fore.RED + "Faltan valores esenciales en la configuración.")
    exit(1)

sys.stdout = LogStream(log_file_path)

try:

    print(Fore.YELLOW + "Probando la conexión a Google a través del proxy...")

    proxy_url = f"http://{proxy_host}:{proxy_port}"
    session = requests.Session()

    if proxy_auth_required == 1 and proxy_user and proxy_password:
        session.proxies = {
            "http": f"http://{proxy_user}:{proxy_password}@{proxy_host}:{proxy_port}",
            "https": f"http://{proxy_user}:{proxy_password}@{proxy_host}:{proxy_port}",
        }
        print(Fore.YELLOW + f"Conectando al proxy {proxy_host}:{proxy_port} con autenticación...")
    else:
        session.proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }
        print(Fore.YELLOW + f"Conectando al proxy {proxy_host}:{proxy_port} sin autenticación...")

    response = session.get("http://www.google.com", timeout=10)
    print(Fore.GREEN + f"Conexión exitosa al proxy. Código de estado: {response.status_code}")

    command = [
        hellminer_path,
        "-c", pool_url,
        "-u", username,
        "-p", password,
        "--cpu", str(cpu_count)
    ]

    print(Fore.YELLOW + "Iniciando Minero a través del proxy...")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Iniciando Minero a través del proxy...\n")

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    while True:
        stdout_line = process.stdout.readline()
        stderr_line = process.stderr.readline()

        if stdout_line:
            print(Fore.CYAN + f"STDOUT: {stdout_line.strip()}")
            with open(log_file_path, "a") as log_file:
                log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - STDOUT: {stdout_line.strip()}\n")

        if stderr_line:
            print(Fore.RED + f"STDERR: {stderr_line.strip()}")
            with open(log_file_path, "a") as log_file:
                log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - STDERR: {stderr_line.strip()}\n")

        return_code = process.poll()
        if return_code is not None:
            break

    if return_code == 0:
        print(Fore.GREEN + "Minero ejecutado correctamente.")
    else:
        print(Fore.RED + f"Minero terminó con errores. Código de retorno: {return_code}")

except KeyboardInterrupt:
    print(Fore.YELLOW + "\nInterrupción detectada. Finalizando ejecución...")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Interrupción detectada. Ejecución finalizada.\n")
    sys.exit(0)

except Exception as e:
    print(Fore.RED + f"Error: {e}")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Error: {e}\n")
