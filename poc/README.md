# Scoring Service

Attualmente la scoring service è configurata per rispondere all'evento di creazione di un file all'interno di swe-bucket-bugsbunny in "comprehend/input/".
Questo servizio legge il file, fa un'analisi del sentimento con *Comprehend* e mette la risposta in "comprehend/output/" all'interno dello stesso bucket.
