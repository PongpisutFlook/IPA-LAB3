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
        "S1": "172.31.124.3",
        "R2": "172.31.124.5",
        "R1": "172.31.124.4"
     }

for ip in devices:
    device_params['host'] = devices[ip]
    with ConnectHandler(**device_params) as ssh:
        result = ssh.send_config_from_file(f'./netmiko_config/{ip}.config')
        print(result)