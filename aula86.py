produtos = [
    {'nome': 'Iphone 11', 'preço': 2700},
    {'nome': 'Iphone 12', 'preço': 3600},
    {'nome': 'Iphone 12 pro', 'preço': 2700},
    {'nome': 'Iphone 13', 'preço': 2700},
    {'nome': 'Iphone 13 pro', 'preço': 2700},
    {'nome': 'Iphone 13 pro max', 'preço': 2700}
]

novos_preços = [
    {**item, 'preço': item['preço'] * 1.05} 
    for item in produtos
]

print(*novos_preços, sep='\n')