from netmiko import ConnectHandler

device_params = {
    'device_type': 'cisco_ios',
    'host': '',
    'username': 'cisco',
    'use_keys': True,
    'key_file': r'C:\Users\PONGPISUT\.ssh\id_rsa',
    'session_log': 'netmiko_debug.log',
    'conn_timeout': 60,
    "disabled_algorithms": { "pubkeys": ["rsa-sha2-256","rsa-sha2-512"]}
}

devices = {
        "R0": "172.31.124.1",
        "S0": "172.31.124.2",
        "S1": "172.31.124.3",
        "R1": "172.31.124.4",
        "R2": "172.31.124.5"
     }

for ip in devices:
    device_params['host'] = devices[ip]
    with ConnectHandler(**device_params) as ssh:
        commands = ["banner motd ^", " ____  _ _  __", "|  _ \( ) |/ /___  _ __   __ _", "| |_) |/| ' // _ \| '_ \ / _` |", "|  __/  | . \ (_) | | | | (_| |", "|_|     |_|\_\___/|_| |_|\__, |", "                         |___/", "welcome to P'kong network", "^"]
        result = ssh.send_config_set(commands)
        print(result)