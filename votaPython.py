candidatos = [
    "Promessinha",
    "Influêncio Digital",
    "Impostácio",
    "Dona Burocracia",
]

numeros = [10, 20, 30, 40]
votos = [0, 0, 0, 0]
votos_branco = 0

print('=== VOTA PYTHON ===')
print('Isto é apenas uma simulação\n')

while True:
    print("=== CANDIDATOS ===")

    for i in range(len(candidatos)):
        print(f'{numeros[i]} - {candidatos[i]}')

    print('50 - VOTOS EM BRANCO')

    numero = input('\nDigite o número do seu candidato (0 para sair): ')

    if numero == '0':
        break

    if not numero.isdigit():
        print('Número inválido!')
        continue

    numero = int(numero)

    if numero == 50:
        print('VOTO EM BRANCO')
        print('Você escolheu votar em branco')

    elif numero in numeros:
        indice = numeros.index(numero)
        print(f'\nCandidato: {candidatos[indice]}')
    else:
        print('Número inválido!')
        continue

    confirma = input('Confirma o voto? [S/N]: ').strip().lower()

    while confirma not in ('s', 'n'):
        print('Resposta inválida! Digite S ou N.')
        confirma = input('Confirma o voto? [S/N]: ').strip().lower()

    if confirma == 's':
        if numero == 50:
            votos_branco += 1
            print('Voto em branco registrado!')
        else:
            votos[indice] += 1
            print('Voto registrado!')
    else:
        print('Voto cancelado.')
        continue

    continua = input('Deseja votar novamente? [S/N]: ').strip().lower()

    while continua not in ('s', 'n'):
        print('Resposta inválida! Digite S ou N.')
        continua = input('Deseja votar novamente? [S/N]: ').strip().lower()

    if continua == 'n':
        break

print('\n======= APURAÇÕES ========')

total_candidatos = sum(votos)
total = total_candidatos + votos_branco

if total == 0:
    print('Nenhum voto foi registrado.')
    print('Não há resultado para apresentar.')
else: 
    print(f'Total de votos registrados: {total}')
    print(f'Total de votos nos candidatos: {total_candidatos}')
    print(f'Total de votos em branco: {votos_branco}')

    print('\n====== RESULTADO POR CANDIDATO ======')  
    for i in range(len(candidatos)):
        porcentagem = (votos[i] / total) * 100
        print(f'{candidatos[i]}: {votos[i]} votos ({porcentagem:.1f}%)')

    porcentagem_brancos = (votos_branco / total) * 100
    print(f'Votos em branco: {votos_branco} ({porcentagem_brancos:.1f}%)')

    #Identifica a maior quantidade de votos
    if total_candidatos > 0:
        maior_votos = max(votos)
        vencedores = []

        for i in range(len(candidatos)):
            if votos[i] == maior_votos:
                vencedores.append(candidatos[i])

        print('\n====== RESULTADO FINAL ======')
        if len(vencedores) == 1:
            print(f'Vencedor: {vencedores[0]}!')
            print(f'Votos recebidos: {maior_votos}')
        else:
            print(f'EMPATE NA APURAÇÃO!')
            print(f'Total de votos dos candidatos empatados: {maior_votos}')
            print('Candidatos: ')
            for candidato in vencedores:
                print(f' - {candidato}')
    else:
        print('\nNenhum candidato recebeu votos.')
        print('Não é possível declarar um vencedor')
