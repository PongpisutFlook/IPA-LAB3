from netmiko import ConnectHandler
import re

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
        "R2": "172.31.124.5",
        "R1": "172.31.124.4"
}

for ip in devices:
    device_params['host'] = devices[ip]
    print(f"----------- Router {ip} -----------")
    print(" * All the active interfaces")
    with ConnectHandler(**device_params) as ssh:
        result = ssh.send_command('show ip interface brief')
        active_if = []
        for i in result.split('\n'):
            match = re.search(r'^(\S+).*up\s*up', i)
            if match:
                print(f'   - {match.group(1)}')

        result = ssh.send_command('show version')
        for i in result.split('\n'):
            match = re.search(r'.*uptime.*', i)
            if match:
                print(f' * {i}')

    print(f"---------------------------------"+"\n")
      