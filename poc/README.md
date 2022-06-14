# poc

## Prerequisiti

- Python
- [Docker](https://www.docker.com/get-started/) (opzionale ma estremamente consigliato, serve per invocare le *Lambda*
  localmente)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

Seguire
la [guida di SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html)
per impostare le credenziali di autenticazione ad *AWS*.

## Deploy

```shell
sam validate    # validazione di template.yaml

sam build                   # compila il template e impacchetta i sorgenti
sam build --use-container   # in alternativa, se non funziona quello sopra (serve docker)

sam deploy            # carica tutto su aws e crea le risorse
sam deploy --guided   # utile al primo deploy
```

## Testing

### Unit tests

Sono disponibili alcuni *unit tests*, per eseguirli:

```shell
python -m pytest tests/unit
```

## Strumenti consigliati

- PyCharm (con plugin [AWS Toolkit](https://aws.amazon.com/pycharm/))
