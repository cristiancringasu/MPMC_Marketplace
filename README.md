Nume:  Cringasu Cristian-Marius
Grupă: 336CB

# Tema 1

Organizare
-
1. Explicație pentru soluția aleasă:

***Obligatoriu:*** 


Tema a fost rezolvata prin implementarea tuturor functiilor din skelet :)
Adica?
Am pornit cu implementarea market placeului:
	- am decis ca ar fi necesar retinerea unei variabile pentru id-uri pentru :
									* producatori
									* cart-uri
	- am decis ca ar fi necesar retinerea unui dictionar de cozi de produse asociate producatorilor
	- am decis ca ar fi necesar retinerea unei liste de cart-uri, dar ulterior am realizat
		ca se poate stabili cart-ul unui client fara lista de cart-uri folosind un
		mecanism de rezervare al produselor in coada de produse a producatorilor
	- new_cart -> returneaza self.cart_id, incrementeaza si il pregateste pentru noua cerere
	- register_producer -> idem new_cart, alte variabile
	- publish -> verifica lungimea cozii producatorului, returneaza True si adauga produsul
		daca mai e loc ca fiind un tuplu de produs + BOOKER (initial None), False daca e plin
	- add_to_cart -> cauta prin toate cozile producatorilor produsul "X", daca il gaseste
		marcheaza al doilea camp din tuplul entry-ului ca fiind cart_id (BOOKER)
	- remove_from_cart -> cauta prin toate cozile producatorilor produsul "X" cu cart_id-ul "C",
		marcheaza BOOKER-ul ca None, daca e gasit
	- place_order -> cauta prin toate cozile producatorilor produsul "X" cu cart_id-ul "C",
		face append in order_list daca entry-ul se potriveste cerintelor

Consumer:
	- am decis ca ar fi necesar retinerea unei variabile pentru id-uri pentru :
									* cart-uri
									* marketplace
									* retry_wait_time
	- run -> iterez prin lista de carturi, apelez marketplace.new_cart() pentru fiecare cart
		pentru a tine minte id-ul, pentru fiecare operatie se realizeaza add sau remove (type)
		daca avem o operatie de tip add, luam in considerare si cazul de fail in care
		trebuie sa mai asteptam pana la urmatorul retry, deasemenea operatia se executa de N ori
		specificat de 'quantity' | la final se printeaza lista returnata de place_order

Producer:
	- am decis ca ar fi necesar retinerea unei variabile pentru id-uri pentru :
									* products
									* marketplace
									* republish_wait_time
	- run -> iterez prin lista de produse in permanenta, apelez marketplace.register_producer()
		pentru a tine minte id-ul, pentru fiecare produs se asteapta un timp T specificat in campul 3
		apoi se incearca publish, luam in considerare si cazul de fail in care
		trebuie sa mai asteptam pana la urmatorul retry, deasemenea operatia se executa de N ori
		specificat de campul 2

***Opțional:***


* De menționat cazuri speciale, nespecificate în enunț și cum au fost tratate.


Implementare
-

* De specificat dacă întregul enunț al temei e implementat
* Dacă există funcționalități extra, pe lângă cele din enunț - descriere succintă + motivarea lor
* De specificat funcționalitățile lipsă din enunț (dacă există) și menționat dacă testele reflectă sau nu acest lucru
* Dificultăți întâmpinate
* Lucruri interesante descoperite pe parcurs


Resurse utilizate
-

* Resurse utilizate - toate resursele publice de pe internet/cărți/code snippets, chiar dacă sunt laboratoare de ASC

Git
-
1. Link către repo-ul de git

Ce să **NU**
-
* Detalii de implementare despre fiecare funcție/fișier în parte
* Fraze lungi care să ocolească subiectul în cauză
* Răspunsuri și idei neargumentate
* Comentarii (din cod) și *TODO*-uri

Acest model de README a fost adaptat după [exemplul de README de la SO](https://github.com/systems-cs-pub-ro/so/blob/master/assignments/README.example.md).