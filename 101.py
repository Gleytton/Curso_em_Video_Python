import datetime


def voto(a):

    anoAtual = datetime.datetime.now().year

    status = anoAtual - a

    if(status < 16 ):

        msg = 'VOTO NEGADO'

    if (status >= 16 and status < 18):

        msg = "VOTO OPCIONAL"

    if (status >= 18 and status < 65 ):

        msg = 'VOTO OBRIGATORIO'

    if (status >= 65):

        msg = 'VOTO FACULTATIVO'

    return msg

nascimento = int(input('Digite o ano do seu nascimento: '))

resultado = voto(nascimento)

print(resultado)