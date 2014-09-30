Robba Djangosa per il POuL
========

Questo repo raccoglie varie applicazioni Django scritte per il POuL

Manifesti
=========

Tieni traccia di chi ha attaccato i manifesti e dove.

Il funzionamento è estremamente semplice: chi attacca il manifesto clicca sul 
punto nella mappa e inserisce il token che gli è stato fornito. Il sistema 
verifica il token e aggiorna la data dell'ultima visita.

Il token è generato leggendo 20 bytes da `/dev/urandom` o equivalente,
viene fornito base64-encoded e memorizzato nel database.

Pagine
------

L'applicazione ha 2 pagine:

* `/` è la radice, pubblica
* `/admin` è la sezione per aggiungere e gestire le bacheche (generare token etc.)

Installazione
------------

**AL MOMENTO DELL'INSTALLAZIONE, RIVEDERE E COMPLETARE `poulango/settings.py`**

La cartella `nginx/` contiene vari script utili per il deploy dietro NGINX+uWSGI.
