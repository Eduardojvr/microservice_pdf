<p align="center"><a href="https://imgur.com/LbrJ2e6" target="_blank"><img width="500"src="https://imgur.com/LbrJ2e6"></a></p>
<p align="center">
        
## ℹ️ Sobre
O Gerencia Report é um micro serviço desenvolvido para oferecer suporte a aplicações que necessitam relatorios nos formatos pdf ou xlsx, de forma em que os dados são mostrados de forma tabelar.

## ℹ️ Uso

Ha duas formas de se utilizar o serviço, uma com a função de gerar pdf e outra para gerar xlsx:

* ***Para a geração de PDF deve ser feita uma requisição pra o microserviço no formato:***

```Terminal

curl --header "Content-Type:  application/x-www-form-urlencoded" \
  --request POST \
  --data '[{"nome":"João","cpf":"123123123"},{"nome":"Eduardo","dwdwd":"112323345"}]' \
  https://gerencia-report.herokuapp.com/report/all_doctors > asd.pdf

```

* ***Para a geração de XSLX deve ser feita uma requisição pra o microserviço no formato:***

```Terminal

curl --header "Content-Type:  application/x-www-form-urlencoded" \
  --request POST \
  --data '[{"nome":"Caio","cpf":"234234234234"},{"nome":"Rafael","cpf":"434343555"}]' \
  https://gerencia-report.herokuapp.com//report/xsml_all_doctors > asd.pdf

```

***Obs*** O fomato do json a ser enviado deve sempre estar dentro de uma lista com objetos iguaus dentro dele

* ***Exemplo:***


```Terminal
  [
    {"nome":"Caio","cpf":"12312312334"},
    {"nome":"Eduardo","cpf":"23423423434"},
    {"nome":"João","cpf":"34534534534"},
    {"nome":"Rafael","cpf":"56756756787"},
    {"nome":"Ulysses","cpf":"09898709867"} 
  ]

```



ℹ️ URL para PDF: https://gerencia-report.herokuapp.com/report/all_doctors

ℹ️ URL para xlxs: https://gerencia-report.herokuapp.com/report/xsml_all_doctors

## 🐳 Guia de Uso do Docker

* ### Instalação
Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Instalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

* ### Comandos básicos 

 &emsp;&emsp; Para a utilização do ambiente em background, basta dar o comando abaixo e ele irá ligar o container:
 
 ```terminal
  docker-compose up -d
 ```
 &emsp;&emsp; Caso queira utilizar o ambiente com logs:

 ```terminal
  docker-compose up 
 ```
 &emsp;&emsp; Para a visualização dos logs quando em modo de execução background, use o comando abaixo:

 ```terminal
  docker-compose logs -f
 ```

 &emsp;&emsp; Para pausar o container:

  ```terminal
  docker-compose stop
 ```
 &emsp;&emsp; E para religar um container parado use o comando: 
 
 ```terminal
  docker-compose start 
 ```

 &emsp;&emsp; Para listar os containers que estão em execução:
 
 ```terminal
  docker ps
 ```
 &emsp;&emsp; Para listar todos os containers já executados na sua máquina:
 
 ```terminal
  docker ps -a
 ```
 &emsp;&emsp; Para executar comandos dentro do container:
 
 ```terminal
  docker-compose exec -it  "id do container"  "comandos"
 ```
 Para acessar o [bash](https://www.gnu.org/software/bash/) do container, substitua "comandos" por "bash".

* ## Rodando a aplicação no localhost

Para rodar a aplicação, entre na pasta do projeto em que está localizado o __docker-compose__ e digite no terminal:

```
  docker-compose up -d
```
Espere até que todos os serviços estejam disponíveis, acesse a página inicial do projeto com o seguinte endereço: https://0.0.0.0:9000/report/all_doctors ou  https://0.0.0.0:9000/report/xsml_all_doctors

Para utilizar o serviço siga o passo "Uso" substituindo a url aprensentada pelo endereço apresentado neste tópico.
