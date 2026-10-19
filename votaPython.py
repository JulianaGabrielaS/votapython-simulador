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
    print("=== CANDIDATOS ===")
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
    continua = input('Deseja votar novamente? [S/N]: ').lower()
    if continua == 'n':
        break

#Apurações
total = (votos_promessinha + votos_influencio + votos_impostacio + votos_burocracia)

print('======= APURAÇÕES ========')

if total == 0:
    print('Nenhum voto foi registrado.')
    print('Não há resultado para apresentar.')
else: 
    print(f'Total de votos válidos: {total}')
    print('\n====== RESULTADO POR CANDIDATOS ======')    
    print(f'Promessinha: {votos_promessinha} votos.')
    print(f'Influêncio Digital: {votos_influencio} votos.')
    print(f'Impostácio: {votos_impostacio} votos.')
    print(f'Dona burocracia: {votos_burocracia} votos.')

    #porcentagem de votos
    porcentagem_promessinha = (votos_promessinha/total) * 100
    porcentagem_influencio = (votos_influencio/total) * 100
    porcentagem_impostacio = (votos_impostacio/total) * 100
    porcentagem_burocracia = (votos_burocracia/total) * 100

    print('====== PORCENTAGEM DE VOTOS ======')
    print(f'Promessinha: {porcentagem_promessinha:.1f}%')
    print(f'Influêncio Digital: {porcentagem_influencio:.1f}%')
    print(f'Impostácio: {porcentagem_impostacio:.1f}%')
    print(f'Dona burocracia: {porcentagem_burocracia:.1f}%')
