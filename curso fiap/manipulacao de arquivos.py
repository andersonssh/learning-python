with open('sla.txt', 'r') as sl:
    for i in sl:
        s = i

        nome = s[:s.find(';')]
        s = s[s.find(';') + 1:]

        raca = s[:s.find(';')]
        s = s[s.find(';') + 1:]

        serial = s[:s.find(';')]
        s = s[s.find(';') + 1:]

        print(f'nome: "{nome}" raca: "{raca}" serial: "{serial}"')
