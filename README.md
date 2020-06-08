# Case_LuizCarlos
Instruções
1.	Escolha um dos cases abaixo: Twitter ou Cats API
    1.2. O Twitter, às vezes, demora para enviar as chaves de acesso. Se isso travar seu progresso, você tem a API de gatos para consumir.
2.	Utilize o github ou afins para versionar seu projeto
3.	Você tem até 7 dias corridos para concluir as atividades. (O Resultado deverá ser enviando após os 7 dias, independente do ponto do desenvolvimento);
3.1. Foque 1o em sua zona de conhecimento, e progrida o máximo que puder. Caso não consiga concluir todas as atividades, por favor, entregue o que foi feito até a data solicitada.
4.	Fique à vontade para utilizar tecnologias, frameworks e técnicas não citadas nas atividades.
5.	Recomendamos a utilização do docker (http://www.docker.com) para montagem do ambiente por facilitar a nossa execução e validação, mas fique à vontade para usar outras coisas, como cloud publica por exemplo, contanto que nós consigamos executar e validar sua infra/código.
5.1 Caso opte pela utilização do docker, publique os Dockerfiles no repositório do projeto ou deixe a imagem publicada no Dockerhub.
6.	Critérios de avaliação:
a.	Código: 25%
b.	Logging: 25%
c.	Métricas: 25%
d.	Facilidade de Deploy: 25%
Obs.: Para todos os itens iremos considerar a documentação como parte da entrega. 

 
Case Twitter

1.	Crie uma aplicação na linguagem que desejar para coletar as últimas postagens do Twitter, dada uma determinada #tag.
a.	Por padrão o Twitter disponibiliza as 100 últimas postagens.
b.	Caso não tenha 100 twittes, colete todas que vierem.
c.	Não há necessidade de coletar mais do que 100 twittes, dada um #tag.
d.	Atente-se a limites e timeouts

2.	Use uma base de dados para armazenar as informações.

3.	Colete e armazene as mensagens, na base de dados, para as #tags listadas abaixo:
#openbanking, #remediation, #devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing

4.	Utilizando uma linguagem de sua preferência, sumarize e grave os dados para conseguir listar as informações:
a.	Quais são os 5 (cinco) usuários, da amostra coletada, que possuem mais seguidores?
b.	Qual o total de postagens, agrupadas por hora do dia (independentemente da #hashtag)? 
c.	Qual o total de postagens para cada uma das #tag por idioma/país do usuário que postou;

5.	Crie uma API REST que permita o consumo dos três itens anteriores. A API deverá expor métricas de execução. 

6.	Crie uma coleção no postman para consumir as APIs criadas.

7.	Envie seus logs para uma ferramenta de logging (exemplos: Elastic Search, Splunk, Graylog ou similar) e crie uma query que mostre em tempo real os eventos que acontecem na execução da API criada acima, exemplos (Warning, Erro, Debug, Info, etc).

8.	Utilize uma ferramenta de métricas para sua infraestrutura (exemplos: Prometheus, Zabbix, cloudwatch ou similar) e também crie 3 dashboards que mostrem em tempo real a quantidade de execução, a latência (tempo de execução) e quantidade de erros da API criada acima.

 
9.	Publique o projeto no Github e documente no README.md os itens abaixo:
a.	Documentação do projeto
b.	Documentação das APIs 
c.	Documentação de arquitetura
d.	Documentação de como podemos subir uma cópia deste ambiente
e.	Manual com prints dos Logs (item 7) e os Dashboards (item 9) explicando cada um deles.

10. Bônus. Se você chegou até aqui e quiser, pode criar um frontend para sua aplicação para facilitar a experiencia do usuário.

