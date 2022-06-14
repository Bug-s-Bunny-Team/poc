# Intro

Questo documento ha lo scopo di descrivere con ragionevole dettaglio, le strategie adottate per dare uno score ai vari post ottenuti dal servizio di scraping.

# Rekognition

Il primo step è l'uso di *AWS Rekognition* per estrarre l'informazione testuale all'interno del post, che esso sia in formato immagine oppure video.

# Comprehend

Il secondo step è l'uso di *AWS Comprehend* per ottenere uno score sul sentimento di ogni informazione testuale presente nel post, per esempio caption del post, testo all'interno del post (proveniente dall'analisi di *Rekognition*) e eventualmente hastags.

# Scoring

L'ultimo step cerca di dare una valutazione unica in floating point ad un post considerando i risultati dell'analisi fatta con *Comprehend*. Questo valore viene poi inserito nel Database scelto.
