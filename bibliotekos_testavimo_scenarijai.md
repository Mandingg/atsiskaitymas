# Bibliotekos knygų išdavimo sistemos testavimo scenarijai

## TC-01 Vartotojo registracija

**Tikslas:** patikrinti, ar vartotojas gali užsiregistruoti.

**Endpoint:** `POST /auth/register`

**Body pavyzdys:**
```json
{
  "name": "Testas",
  "surname": "Testaitis",
  "email": "testas@testas.com",
  "password": "Testas123!"
}
```

**Tikėtinas rezultatas:**
- HTTP `201 Created`
- Vartotojas sukuriamas duomenų bazėje

---

## TC-02 Vartotojo prisijungimas

**Tikslas:** patikrinti, ar vartotojas gali prisijungti ir gauti JWT tokeną.

**Endpoint:** `POST /auth/login`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- Grąžinamas `access_token`
- Tokeną galima naudoti per Swagger `Authorize`

---

## TC-03 USER bando sukurti knygą

**Tikslas:** patikrinti, ar paprastas vartotojas negali kurti knygų.

**Endpoint:** `POST /books`

**Body pavyzdys:**
```json
{
  "title": "Python pagrindai",
  "author": "Jonas Jonaitis",
  "category": "Programavimas",
  "status": "AVAILABLE"
}
```

**Tikėtinas rezultatas:**
- HTTP `400 Bad Request` arba `403 Forbidden`
- Klaida: `Tik administratorius gali kurti knygas.`

---

## TC-04 Sukurti ADMIN vartotoją

**Tikslas:** paruošti administratoriaus vartotoją knygų valdymui.

**Veiksmas DB:**
```sql
UPDATE users
SET role = 'ADMIN'
WHERE email = 'admin@email.lt';
```

**Tikėtinas rezultatas:**
- Vartotojo rolė pakeičiama į `ADMIN`
- Prisijungus jo JWT payload turi turėti `role = ADMIN`

---

## TC-05 ADMIN sukuria knygą

**Tikslas:** patikrinti, ar administratorius gali sukurti knygą.

**Endpoint:** `POST /books`

**Body pavyzdys:**
```json
{
  "title": "Python pagrindai",
  "author": "Jonas Jonaitis",
  "category": "Programavimas",
  "status": "AVAILABLE"
}
```

**Tikėtinas rezultatas:**
- HTTP `201 Created`
- Knyga sukuriama
- Grąžinamas knygos `id` ir sėkmės žinutė

---

## TC-06 Gauti knygų sąrašą

**Tikslas:** patikrinti, ar prisijungęs vartotojas gali matyti knygų sąrašą.

**Endpoint:** `GET /books`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- Grąžinamas knygų sąrašas
- Sąraše yra sukurta knyga

---

## TC-07 Paieška pagal knygos pavadinimą

**Tikslas:** patikrinti paiešką pagal `title`.

**Endpoint:** `GET /books?search_by_title=Python`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- Grąžinamos tik knygos, kurių pavadinime yra `Python`

---

## TC-08 Filtravimas pagal kategoriją

**Tikslas:** patikrinti filtravimą pagal `category`.

**Endpoint:** `GET /books?category_filter=Programavimas`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- Grąžinamos tik `Programavimas` kategorijos knygos

---

## TC-09 USER pasiima knygą

**Tikslas:** patikrinti knygos pasiėmimo funkcionalumą.

**Endpoint:** `POST /book-loans`

**Body pavyzdys:**
```json
{
  "book_id": 1
}
```

**Tikėtinas rezultatas:**
- HTTP `201 Created`
- Sukuriamas įrašas `book_loans` lentelėje
- `book_loans.status = BORROWED`
- `books.status = UNAVAILABLE`

---

## TC-10 USER bando pasiimti tą pačią knygą dar kartą

**Tikslas:** patikrinti, ar negalima pasiimti jau paimtos knygos.

**Endpoint:** `POST /book-loans`

**Body pavyzdys:**
```json
{
  "book_id": 1
}
```

**Tikėtinas rezultatas:**
- HTTP `400 Bad Request`
- Klaida: `Knyga šiuo metu jau paimta.` arba panaši

---

## TC-11 USER mato savo knygų išdavimus

**Tikslas:** patikrinti, ar vartotojas mato savo pasiskolintas knygas.

**Endpoint:** `GET /book-loans`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- USER mato tik savo `book_loans`
- Atsakyme matosi knygos informacija:
  - `title`
  - `author`
  - `borrowed_at`
  - `returned_at`
  - `status`

---

## TC-12 USER grąžina knygą

**Tikslas:** patikrinti knygos grąžinimą.

**Endpoint:** `PUT /book-loans/{loan_id}/return`

**Pavyzdys:** `PUT /book-loans/1/return`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- `book_loans.status = RETURNED`
- `book_loans.returned_at` užsipildo
- `books.status = AVAILABLE`

---

## TC-13 USER bando grąžinti tą pačią knygą antrą kartą

**Tikslas:** patikrinti, ar negalima antrą kartą grąžinti jau grąžintos knygos.

**Endpoint:** `PUT /book-loans/{loan_id}/return`

**Pavyzdys:** `PUT /book-loans/1/return`

**Tikėtinas rezultatas:**
- HTTP `400 Bad Request`
- Klaida: `Knyga jau grąžinta.`

---

## TC-14 ADMIN mato visų vartotojų knygų išdavimus

**Tikslas:** patikrinti administratoriaus teises matyti visus išdavimus.

**Endpoint:** `GET /book-loans`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- ADMIN mato visų vartotojų `book_loans`
- Atsakyme matosi vartotojo informacija:
  - `user_id`
  - `name`
  - `email`

---

## TC-15 USER negali grąžinti kito vartotojo knygos

**Tikslas:** patikrinti, ar vartotojas negali atlikti veiksmo su svetimu `loan`.

**Veiksmai:**
1. Sukurti antrą USER.
2. Antras USER pasiima knygą.
3. Prisijungti pirmu USER.
4. Bandyt grąžinti antro USER `loan`.

**Endpoint:** `PUT /book-loans/{kito_user_loan_id}/return`

**Tikėtinas rezultatas:**
- HTTP `400 Bad Request` arba `403 Forbidden`
- Klaida: `Neturite teisės grąžinti šios knygos.`

---

## TC-16 ADMIN gali redaguoti knygą

**Tikslas:** patikrinti, ar administratorius gali atnaujinti knygos informaciją.

**Endpoint:** `PUT /books/{book_id}`

**Body pavyzdys:**
```json
{
  "title": "Python pagrindai atnaujinta",
  "author": "Jonas Jonaitis",
  "category": "Programavimas",
  "status": "AVAILABLE"
}
```

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- Knygos duomenys atnaujinami

---

## TC-17 USER negali redaguoti knygos

**Tikslas:** patikrinti, ar paprastas vartotojas negali redaguoti knygų.

**Endpoint:** `PUT /books/{book_id}`

**Tikėtinas rezultatas:**
- HTTP `400 Bad Request` arba `403 Forbidden`
- Klaida: `Tik administratorius gali redaguoti knygas.`

---

## TC-18 ADMIN gali ištrinti knygą

**Tikslas:** patikrinti, ar administratorius gali pašalinti knygą.

**Endpoint:** `DELETE /books/{book_id}`

**Tikėtinas rezultatas:**
- HTTP `200 OK`
- Knyga pašalinama
- Grąžinama sėkmės žinutė

---

## TC-19 USER negali ištrinti knygos

**Tikslas:** patikrinti, ar paprastas vartotojas negali trinti knygų.

**Endpoint:** `DELETE /books/{book_id}`

**Tikėtinas rezultatas:**
- HTTP `400 Bad Request` arba `403 Forbidden`
- Klaida: `Tik administratorius gali trinti knygas.`

---

## Galutinė išvada

Jeigu visi testai praeina, sistema atitinka pagrindinius reikalavimus:

- registracija
- prisijungimas
- JWT autentifikacija
- USER / ADMIN rolės
- knygų CRUD su ADMIN apsauga
- knygų paieška, filtravimas ir puslapiavimas
- knygos pasiėmimas
- knygos grąžinimas
- vartotojo ir administratoriaus teisių atskyrimas
