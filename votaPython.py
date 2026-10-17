candidatos = [
    "Promessinha",
    "Influêncio Digital",
    "Impostácio",
    "Dona Burocracia",
]

numeros = [10, 20, 30, 40]

votos_promessinha = 0
votos_influencio = 0
votos_impostacio = 0
votos_burocracia = 0

print('=== VOTA PYTHON ===')
print('Isto é apenas uma simulação\n')

while True:
    print("\n=== CANDIDATOS ===")
    print('10 - Promessinha\n20 - Influêncio Digital\n30 - Impostácio\n40 - Dona Burocrácia')

    numero = input('\nDigite o número do seu candidato: ')
    if numero == '0':
        break
    elif numero == '10':
        candidato = candidatos[0]
        print(f'Candidado: {candidato}')
        confirma = input('Confirma o voto? [S/N]: ').lower()
        if confirma == 's':
            votos_promessinha += 1
            print('Voto registrado!')
        else:
            print('Voto cancelado.')
    elif numero == '20':
        candidato = candidatos[1]
        print(f'Candidato: {candidato}')
        confirma = input('Confirma o voto? [S/N]: ').lower()
        if confirma == 's':
            votos_influencio += 1
            print('Voto registrado!')
        else:
            print('Voto cancelado.')
    elif numero == '30':
        candidato = candidatos[2]
        print(f'Candidato: {candidato}')
        confirma = input('Confirma o voto? [S/N]: ').lower()
        if confirma == 's':
            votos_impostacio += 1
            print('Voto registrado!')
        else:
            print('Voto cancelado.')
    elif numero == '40':
        candidato = candidatos[3]
        print(f'Candidato: {candidato}')
        confirma = input('Confirma o voto? [S/N]: ').lower()
        if confirma == 's':
            votos_burocracia += 1
            print('Voto registrado')
        else:
            print('Voto cancelado.')
    else:
        print('Número inválido!')

#Apurações
total = (votos_promessinha + votos_influencio + votos_impostacio + votos_burocracia)

print('======= APURAÇÕES ========')

if total == 0:
    print('Nenhum voto foi registrado.')
    print('Não há resultado para apresentar.')
else: 
    print(f'Total de votos válidos: {total}')
    
    print('\n====== RESULTADO POR CANDIDATOS ======')
    #próximo
