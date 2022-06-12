# Scoring Service

Attualmente la scoring service è configurata per rispondere all'evento di creazione di un file all'interno di swe-bucket-bugsbunny in "comprehend/input/".
Questo servizio legge il file, che deve essere un file json nel formato 

{
    "id": str
    "caption": str
    "labels" : { "0": str, ... }
    "hashtags" : { "0": str, ... }
} 

e fa un'analisi del sentimento di ogni campo tramite *AWS Comprehend* e mette la risposta in "comprehend/output/" all'interno dello stesso bucket, in un file json con formato

{
    "id": str
    "caption": result
    "labels" : { "0": result, ... }
    "hashtags" : { "0": result, ... }
} 
