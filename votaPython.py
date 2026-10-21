candidatos = [
    "Promessinha",
    "Influêncio Digital",
    "Impostácio",
    "Dona Burocracia",
]

numeros = [10, 20, 30, 40]
votos = [0, 0, 0, 0]

print('=== VOTA PYTHON ===')
print('Isto é apenas uma simulação\n')

while True:
    print("=== CANDIDATOS ===")

    for i in range(len(candidatos)):
        print(f'{numeros[i]} - {candidatos[i]}')

    numero = input('\nDigite o número do seu candidato (0 para sair): ')

    if numero == '0':
        break

    if not numero.isdigit() or int(numero) not in numeros:
        print('Número inválido!')
        continue

    indice = numeros.index(int(numero))

    print(f'Candidato: {candidatos[indice]}')
    confirma = input('Confirma o voto? [S/N]: ').strip().lower()

    while confirma not in ('s', 'n'):
        print('Resposta inválida! Digite S ou N.')
        confirma = input('Confirma o voto? [S/N]: ').strip().lower()
    if confirma == 's':
        votos[indice] += 1
        print('Voto registrado!')
    else:
        print('Voto cancelado.')

    continua = input('Deseja votar novamente? [S/N]: ').strip().lower()

    while continua not in ('s', 'n'):
        print('Resposta inválida! Digite S ou N.')
        continua = input('Deseja votar novamente? [S/N]: ').strip().lower()

    if continua == 'n':
        break

print('======= APURAÇÕES ========')

total = sum(votos)

if total == 0:
    print('Nenhum voto foi registrado.')
    print('Não há resultado para apresentar.')
else: 
    print(f'Total de votos válidos: {total}')

    print('\n====== RESULTADO POR CANDIDATO ======')  
    for i in range(len(candidatos)):
        porcentagem = (votos[i] / total) * 100
        print(f'{candidatos[i]}: {votos[i]} votos ({porcentagem:.1f}%)')

    #Identifica a maior quantidade de votos
    maior_votos = max(votos)
    vencedores = []

    for i in range(len(candidatos)):
        if votos[i] == maior_votos:
            vencedores.append(candidatos[i])

    print('====== RESULTADO FINAL ======')
    if len(vencedores) == 1:
        print(f'Vencedor: {vencedores[0]}!')
        print(f'Votos recebidos: {maior_votos}')
    else:
        print(f'EMPATE NA APURAÇÃO!')
        print(f'Total de votos dos candidatos empatados: {maior_votos}')
        print('Candidatos: ')
        for candidato in vencedores:
            print(f' - {candidato}')