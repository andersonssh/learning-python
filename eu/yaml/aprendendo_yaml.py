import yaml

with open('primeiro-teste.yaml', 'r') as f:
    print(yaml.safe_load(f))


