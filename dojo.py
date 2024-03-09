import os
import requests

def get_package_config(package_name: str, branch='main', dojo_conf='DOJO.json'):
    base = 'https://raw.githubusercontent.com/'
    url = f'{base}{package_name}/{branch}/{dojo_conf}'
    response = requests.get(url)
    config = response.json()
    return config

def get_package(package_name: str, branch='main', dojo_conf='DOJO.json'):
   config = get_package_config(package_name, branch, dojo_conf)
   base = 'https://raw.githubusercontent.com/'
   url = f'{base}{package_name}/{branch}/{config.get("packaged_module", None)}'
   response = requests.get(url)
   return response.content

def save_package(package_bytes: bytes, path):
    with open(path, 'wb') as f:
        f.write(package_bytes)

def install_package(package_name: str, branch='main', dojo_conf='DOJO.json'):
    config = get_package_config(package_name)

    packge = get_package(package_name)
    save_package(packge, config.get('packaged_module'))
    print(f'Installed package: "{config.get("name")}"  {config.get("version")}')

def print_all_packages(dir='.'):
    entries = os.listdir(dir)

    for entry in entries:
        if os.path.isfile(os.path.join('.', entry)):
            if entry.endswith('.mojopkg'):
                print(''.join(entry.split('.')[:-1]))
                # print(os.path.getsize(entry))

if __name__ == '__main__':
    install_package('HeavyLvy/testingDojo')
    print_all_packages()
