# =====================================================
# ShadowMonitor
# Real-time system monitoring utility
# =====================================================

import os
import time
import socket
from datetime import datetime

import psutil


HOSTNAME = socket.gethostname()
LOCAL_IP = socket.gethostbyname(HOSTNAME)

LOG_FILE = "shadowmonitor.log"

CPU_ALERT = 85
RAM_ALERT = 85
CONNECTION_ALERT = 200


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def write_log(timestamp, cpu, ram, connections, status):

    with open(LOG_FILE, "a") as log:

        log.write(
            f"[{timestamp}] "
            f"CPU={cpu}% | "
            f"RAM={ram}% | "
            f"CONNECTIONS={connections} | "
            f"STATUS={status}\n"
        )


def get_status(cpu, ram, connections):

    if cpu >= CPU_ALERT:
        return "[WARNING] High CPU usage detected"

    if ram >= RAM_ALERT:
        return "[WARNING] High memory usage detected"

    if connections >= CONNECTION_ALERT:
        return "[ALERT] Unusual network activity detected"

    return "[OK] System operating normally"


print("\nStarting ShadowMonitor...\n")

time.sleep(1)


while True:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    active_connections = len(psutil.net_connections())

    status = get_status(
        cpu_usage,
        ram_usage,
        active_connections
    )

    clear_terminal()

    print("====================================================")
    print("                   SHADOW MONITOR")
    print("====================================================\n")

    print(f"TIME        : {timestamp}")
    print(f"HOST        : {HOSTNAME}")
    print(f"LOCAL IP    : {LOCAL_IP}")

    print("\n---------------- SYSTEM ----------------\n")

    print(f"CPU USAGE   : {cpu_usage}%")
    print(f"RAM USAGE   : {ram_usage}%")
    print(f"CONNECTIONS : {active_connections}")

    print("\n---------------- STATUS ----------------\n")

    print(status)

    write_log(
        timestamp,
        cpu_usage,
        ram_usage,
        active_connections,
        status
    )

    print("\nLogs saved to shadowmonitor.log")
    print("Press CTRL + C to terminate")

    time.sleep(2)