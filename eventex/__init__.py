"""o comando heroku apps: create eventex-heitorscalon vai criar a nossa aplicação no
 heroku, mandando ela pro ar.
 heroku open vai abrir o arquivo no heroku.
 feito tudo isso, precisamos configurar as variaveis de ambiente do projeto, que estão
 dentro do .env. assim, a primeira coisa é configurar nossa secret key, com o comando
 heroku config:set SECRET_KEY='valor da nossa secret_key dentro do env'. depois disso
 precisamos configurar o debug tambem: heroku config:set DEBUG=True. depois é só dar um
 push no nosso projeto para o heroku: git push heroku main --force.
"""