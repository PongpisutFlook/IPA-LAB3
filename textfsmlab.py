import textfsm

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

def config(ip):
    """textfsmlab"""
    interface = ''
    title = ''
    cmd = [f'int {interface}', f'description {title}']
    des_all = []    
    device_params['host'] = f'{ip}'
    with ConnectHandler(**device_params) as ssh:
        cdp = ssh.send_command('sh cdp neighbor')
        with open('./venv/Lib/site-packages/ntc_templates/templates/cisco_ios_show_cdp_neighbors.textfsm') as template:
            fsm = textfsm.TextFSM(template)
            result = fsm.ParseText(cdp)
            for subset in result:
                description = f'Connect to {subset[3][0]}{subset[4]} of {subset[0].split('.')[0]}'
                interface = f'{subset[1]}'
                title = f'{description}'
                res = ssh.send_config_set(cmd)
                des_all.append(f'{subset[1]}:{description}')
            
            if (ip == devices['R2']):
                # refactor later
                res = ssh.send_config_set([f'interface Gig 0/3', 'description Connect to WAN']);
                des_all.append('Gig 0/3:Connect to WAN')
            if (ip == devices['S1']):
                # refactor later
                res = ssh.send_config_set([f'interface Gig 0/2', 'description Connect to PC']);
                des_all.append('Gig 0/2:Connect to PC')
            if (ip == devices['R1']):
                # refactor later
                res = ssh.send_config_set([f'interface Gig 0/1', 'description Connect to PC']);
                des_all.append('Gig 0/1:Connect to PC')
            
            result = {}
    
            for line in des_all:
                key, value = line.split(":")
                result[key.strip()] = value.strip()
            return result

def main():
    """main"""
    for ip in devices:
        config(devices[ip])
main()