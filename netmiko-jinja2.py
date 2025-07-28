from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import yaml

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

template_dir = "templates"
template_file = "template.txt"
vars_file = 'data_file/devices.yml'

env = Environment(
    loader=FileSystemLoader(template_dir),trim_blocks=True, lstrip_blocks=True)
template = env.get_template(template_file)

with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)

for device in vars_dict['devices']:
    device_params['host'] = devices[device['name']]
    config_command = (template.render(device)).split('\n')
    
    with ConnectHandler(**device_params) as ssh:
        result = ssh.send_config_set(config_command)

    print(f'-----Send config to {device['name']} success------\n')
