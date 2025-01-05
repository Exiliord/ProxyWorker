# ProxyWorker

**ProxyWorker** es una herramienta diseñada para permitir que los trabajadores superen las limitaciones de acceso a Internet impuestas por proxies empresariales, facilitando la minería de criptomonedas, desde equipos detrás de un proxy corporativo. Este proyecto brinda la oportunidad de aprovechar recursos disponibles para generar un ingreso extra.

## Características principales

- **Compatibilidad con proxies corporativos:** Soporte para proxies HTTP (SOCKS5 proximamente)con o sin autenticación.
- **Personalización completa:** Configuración sencilla a través de un archivo `config.json`.
- **Registro detallado:** Todos los eventos y salidas del programa, incluida la salida del Minero, se registran en un archivo de log.
- **Soporte robusto:** Manejo de errores para conexiones al proxy y el software Minero.
- **Pruebas de conectividad:** Verifica automáticamente la conexión al proxy y a Internet antes de iniciar la minería.
- **Facilidad de uso:** Configuración automatizada y soporte para detener el proceso fácilmente con `Ctrl+C`.

## Requisitos

- Python 3.7 o superior.
- Sistema operativo Windows/Linux.
- Proxies HTTP funcionales (con o sin autenticación).
- SOCKS5 proximamente


## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Exiliord/proxyworker.git
   cd proxyworker
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura el archivo `config.json` con los detalles de tu proxy, pool de minería y usuario. Un ejemplo del archivo:

   ```json
   {
    "hellminer_path": "hellminer.exe",
    "pool_url": "stratum+tcp://pool.brandify.cu:4444",
    "username": "RGhdbKhismgKotV9KrVKq6VbkNkYrCJugm.DONATIONS",
    "password": "x",
    "cpu_count": 1,
    "proxy": {
        "host": "IP",
        "port": "PORT",
        "user": "USERNAME",
        "password": "PASSWORD",
        "auth_required": 0
    },
    "log_file": "output.log"
}

   ```

4. Ejecuta el programa:
   ```bash
   python3 proxyworker.py
   ```



## ¿Cómo funciona?

1. **Carga la configuración:** Lee los datos desde `config.json`.
2. **Verifica la conectividad:** Comprueba la conexión a Google a través del proxy configurado.
3. **Configura y ejecuta Hellminer:** Utiliza el proxy para iniciar el software de minería y redirige todas las salidas a un archivo `.log`.
4. **Registra eventos:** Todo lo que ocurre, desde la prueba de conexión hasta la ejecución de Hellminer, se guarda en un archivo de registro detallado.

## Uso responsable

ProxyWorker está diseñado para fines educativos y personales. Es responsabilidad del usuario asegurarse de cumplir con las políticas y normativas de su entorno laboral. El uso indebido de esta herramienta podría tener consecuencias negativas.

## Contribuciones

Contribuciones son bienvenidas. Si tienes ideas para mejorar la herramienta, no dudes en crear un **pull request** o abrir un **issue**.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Compatibilidad

De momento solo testeado con HellMiner

---

¡Disfruta usando ProxyWorker y saca el máximo provecho a tus recursos disponibles!

- BTC: 18RSWopSGwskjt7wrgWCjaAPz7HxDz2Kye
- VRSC:RGhdbKhismgKotV9KrVKq6VbkNkYrCJugm
- USDT: 0x5729f7B671C2F44f70bD6d58CF67d8fdc0687Dfd

