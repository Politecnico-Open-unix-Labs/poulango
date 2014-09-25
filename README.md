Robba Djangosa per il POuL
========

Questo repo raccoglie varie applicazioni Django scritte per il POuL

Manifesti
=========

Tieni traccia di chi ha attaccato i manifesti dove.

Il funzionamento è estremamente semplice: chi attacca il manifesto clicca sul punto
nella mappa e inserisce il token che gli è stato fornito. Il sistema verifica il token
e aggiorna la data dell'ultima visita.

Al momento, l'unico modo per resettare i token è cambiare la chiave HMAC, magari ci si
può lavorare di più :)

Il token è la firma HMAC-SHA1 dell'ID della bacheca, encodata con base64.

L'applicazione ha 2 pagine:

* `/` è la radice, pubblica
* `/admin` è la sezione per aggiungere bachece e gestire gli utenti in un futuro (forse lontano).
