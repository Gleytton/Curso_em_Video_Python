times = ('Flamengo', 'Internacional', 'Atlético-MG','São Paulo','Fluminense','Grêmio','Palmeiras','Santos','Atlético-PA','Bragantino','Ceará','Corinthians','Atlético Goianiense','Bahina','Sport','Fortaleza','Vasco','Goiás','Coritiba','Botafogo')

for i in range(0,5):
    print('O time da {}° posicao é:{}'.format(i,times[i]))

print('Os quatro últimos times são:')
for i in range(16,20):
    print(times[i])

print('Os times em ordem alfabética:{}'.format(sorted(times)))

print(' O chapecoense está na posição: {}'.format(times.index('Vasco')+1))