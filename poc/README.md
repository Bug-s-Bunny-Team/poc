# poc

## Prerequisiti

- Python
- [Docker](https://www.docker.com/get-started/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

Seguire
la [guida di SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html)
per impostare le credenziali di autenticazione ad *AWS*.

## Database locale

Per avviare un database locale, sono necessari *Docker* e *docker-compose*.

Il seguente comando avvia un'istanza di *Postgres* e di *pgadmin* dentro i rispettivi container:

```shell
docker-compose up -d
```

Per fermare e distruggere i container:

```shell
docker-compose down
```

### pgadmin

pgadmin fornisce una interfaccia web per gestire il database localmente.
È disponibile in [http://localhost:8080](http://localhost:8080) con credenziali:

- **username**: `admin@admin.com`
- **password**: `password`

Se viene richiesta, la password del database server è `password`.

### Variabili d'ambiente

| Nome        | Valore        |
|-------------|---------------|
| DB_USER     | `user`        |
| DB_PASSWORD | `password`    |
| DB_HOST     | `172.18.0.10` |
| DB_NAME     | `poc`         |

### Invocazione locale

Ricordarsi di impostare il parametro `docker-network` per rendere visibile il
database dentro l'ambiente di esecuzione della *Lambda*. 

```shell
sam local invoke ... --docker-nextwork sam_local
```

## Testing

### Unit tests

Sono disponibili alcuni *unit tests*, per eseguirli:

```shell
python -m pytest tests/unit
```

## Deploy

```shell
sam validate    # validazione di template.yaml

sam build                   # compila il template e impacchetta i sorgenti
sam build --use-container   # in alternativa, se non funziona quello sopra (serve docker)

sam deploy            # carica tutto su aws e crea le risorse
sam deploy --guided   # utile al primo deploy
```

## Strumenti consigliati

- PyCharm (con plugin [AWS Toolkit](https://aws.amazon.com/pycharm/))
