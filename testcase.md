# Testavimo scenarijai

## TC-01 Registruoti naują vartotoją

**Tikslas:** Patikrinti, ar galima sėkmingai sukurti naują vartotoją.

**Veiksmai:**

1. Iškviesti `POST /auth/register`.
2. Pateikti teisingus vartotojo duomenis.

**Tikėtinas rezultatas:**

* Vartotojas sukuriamas.
* Grąžinamas sėkmės pranešimas.

---

## TC-02 Prisijungti su registruotu vartotoju

**Tikslas:** Patikrinti prisijungimo funkcionalumą.

**Veiksmai:**

1. Iškviesti `POST /auth/login`.
2. Pateikti teisingą el. paštą ir slaptažodį.

**Tikėtinas rezultatas:**

* Grąžinamas JWT prieigos raktas.

---

## TC-03 Gauti prisijungusio vartotojo informaciją

**Tikslas:** Patikrinti autentifikaciją.

**Veiksmai:**

1. Iškviesti `/users/me`.
2. Pateikti galiojantį JWT.

**Tikėtinas rezultatas:**

* Grąžinami vartotojo duomenys ir rolė.

---

## TC-04 Gauti kategorijų sąrašą

**Tikslas:** Patikrinti kategorijų peržiūrą.

**Veiksmai:**

1. Iškviesti `GET /categories`.

**Tikėtinas rezultatas:**

* Grąžinamas kategorijų sąrašas.

---

## TC-05 USER bando sukurti kategoriją

**Tikslas:** Patikrinti administratoriaus teisių kontrolę.

**Veiksmai:**

1. Prisijungti kaip USER.
2. Iškviesti `POST /categories`.

**Tikėtinas rezultatas:**

* Veiksmas atmetamas.
* Grąžinama klaida apie nepakankamas teises.

---

## TC-06 ADMIN sukuria naują kategoriją

**Tikslas:** Patikrinti kategorijos sukūrimą.

**Veiksmai:**

1. Prisijungti kaip ADMIN.
2. Iškviesti `POST /categories`.

**Tikėtinas rezultatas:**

* Kategorija sukuriama.

---

## TC-07 ADMIN bando sukurti pasikartojančią kategoriją

**Tikslas:** Patikrinti dublikatų kontrolę.

**Veiksmai:**

1. Sukurti kategoriją.
2. Bandyti sukurti tokią pačią dar kartą.

**Tikėtinas rezultatas:**

* Grąžinama klaida.

---

## TC-08 ADMIN redaguoja kategoriją

**Tikslas:** Patikrinti kategorijos atnaujinimą.

**Veiksmai:**

1. Iškviesti `PUT /categories/{id}`.

**Tikėtinas rezultatas:**

* Kategorija atnaujinama.

---

## TC-09 ADMIN ištrina kategoriją

**Tikslas:** Patikrinti kategorijos šalinimą.

**Veiksmai:**

1. Iškviesti `DELETE /categories/{id}`.

**Tikėtinas rezultatas:**

* Kategorija pašalinama.

---

## TC-10 Kurti knygą su neegzistuojančia kategorija

**Tikslas:** Patikrinti kategorijos validaciją.

**Veiksmai:**

1. Iškviesti `POST /books`.
2. Nurodyti neegzistuojančią kategoriją.

**Tikėtinas rezultatas:**

* Grąžinama klaida „Tokios kategorijos nėra“.

---

## TC-11 Sukurti knygą su egzistuojančia kategorija

**Tikslas:** Patikrinti knygos sukūrimą.

**Veiksmai:**

1. Iškviesti `POST /books`.
2. Pateikti teisingus duomenis.

**Tikėtinas rezultatas:**

* Knyga sukuriama.

---

## TC-12 Sukurti knygą su tuščiu pavadinimu

**Tikslas:** Patikrinti pavadinimo validaciją.

**Veiksmai:**

1. Iškviesti `POST /books`.
2. Pavadinimo lauke pateikti tuščią reikšmę.

**Tikėtinas rezultatas:**

* Grąžinama validacijos klaida.

---

## TC-13 Sukurti knygą be autoriaus

**Tikslas:** Patikrinti autoriaus validaciją.

**Veiksmai:**

1. Iškviesti `POST /books`.
2. Nepateikti autoriaus.

**Tikėtinas rezultatas:**

* Grąžinama validacijos klaida.

---

## TC-14 Sukurti knygą su neteisingu įvertinimu

**Tikslas:** Patikrinti rating ribojimus.

**Veiksmai:**

1. Iškviesti `POST /books`.
2. Nurodyti rating < 1 arba > 5.

**Tikėtinas rezultatas:**

* Grąžinama validacijos klaida.

---

## TC-15 Gauti visų knygų sąrašą

**Tikslas:** Patikrinti knygų sąrašo gavimą.

**Veiksmai:**

1. Iškviesti `GET /books`.

**Tikėtinas rezultatas:**

* Grąžinamos visos knygos.

---

## TC-16 Gauti konkrečią knygą pagal ID

**Tikslas:** Patikrinti vienos knygos gavimą.

**Veiksmai:**

1. Iškviesti `GET /books/{id}`.

**Tikėtinas rezultatas:**

* Grąžinama pasirinkta knyga.

---

## TC-17 Gauti neegzistuojančią knygą

**Tikslas:** Patikrinti klaidos apdorojimą.

**Veiksmai:**

1. Iškviesti `GET /books/{id}` su neegzistuojančiu ID.

**Tikėtinas rezultatas:**

* Grąžinama klaida „Knyga nerasta“.

---

## TC-18 Filtruoti knygas pagal kategoriją

**Tikslas:** Patikrinti filtravimo funkciją.

**Veiksmai:**

1. Iškviesti `GET /books?category=Fantasy`.

**Tikėtinas rezultatas:**

* Grąžinamos tik pasirinktos kategorijos knygos.

---

## TC-19 Rikiuoti knygas pagal įvertinimą didėjančia tvarka

**Tikslas:** Patikrinti rikiavimą ASC.

**Veiksmai:**

1. Iškviesti `GET /books?sort=asc`.

**Tikėtinas rezultatas:**

* Knygos išrikiuojamos nuo mažiausio įvertinimo.

---

## TC-20 Rikiuoti knygas pagal įvertinimą mažėjančia tvarka

**Tikslas:** Patikrinti rikiavimą DESC.

**Veiksmai:**

1. Iškviesti `GET /books?sort=desc`.

**Tikėtinas rezultatas:**

* Knygos išrikiuojamos nuo didžiausio įvertinimo.

---

## TC-21 USER redaguoja savo knygą

**Tikslas:** Patikrinti savininko teises.

**Veiksmai:**

1. Prisijungti kaip knygos savininkas.
2. Iškviesti `PUT /books/{id}`.

**Tikėtinas rezultatas:**

* Knyga atnaujinama.

---

## TC-22 USER redaguoja tik vieną lauką

**Tikslas:** Patikrinti dalinį atnaujinimą.

**Veiksmai:**

1. Iškviesti `PUT /books/{id}`.
2. Pakeisti tik rating.

**Tikėtinas rezultatas:**

* Atnaujinamas tik rating.

---

## TC-23 USER bando redaguoti svetimą knygą

**Tikslas:** Patikrinti prieigos kontrolę.

**Veiksmai:**

1. Prisijungti kaip kitas vartotojas.
2. Iškviesti `PUT /books/{id}`.

**Tikėtinas rezultatas:**

* Grąžinama klaida apie nepakankamas teises.

---

## TC-24 USER ištrina savo knygą

**Tikslas:** Patikrinti knygos šalinimą.

**Veiksmai:**

1. Prisijungti kaip savininkas.
2. Iškviesti `DELETE /books/{id}`.

**Tikėtinas rezultatas:**

* Knyga pašalinama.

---

## TC-25 USER bando ištrinti svetimą knygą

**Tikslas:** Patikrinti prieigos kontrolę.

**Veiksmai:**

1. Prisijungti kaip kitas vartotojas.
2. Iškviesti `DELETE /books/{id}`.

**Tikėtinas rezultatas:**

* Grąžinama klaida apie nepakankamas teises.

---

## TC-26 ADMIN redaguoja svetimą knygą

**Tikslas:** Patikrinti administratoriaus teises.

**Veiksmai:**

1. Prisijungti kaip ADMIN.
2. Iškviesti `PUT /books/{id}`.

**Tikėtinas rezultatas:**

* Knyga atnaujinama.

---

## TC-27 ADMIN ištrina svetimą knygą

**Tikslas:** Patikrinti administratoriaus teises.

**Veiksmai:**

1. Prisijungti kaip ADMIN.
2. Iškviesti `DELETE /books/{id}`.

**Tikėtinas rezultatas:**

* Knyga pašalinama.

---

## TC-28 Kurti knygą neprisijungus

**Tikslas:** Patikrinti autentifikaciją.

**Veiksmai:**

1. Iškviesti `POST /books` be JWT.

**Tikėtinas rezultatas:**

* Grąžinama autentifikacijos klaida.

---

## TC-29 Redaguoti knygą neprisijungus

**Tikslas:** Patikrinti autentifikaciją.

**Veiksmai:**

1. Iškviesti `PUT /books/{id}` be JWT.

**Tikėtinas rezultatas:**

* Grąžinama autentifikacijos klaida.

---

## TC-30 Ištrinti knygą neprisijungus

**Tikslas:** Patikrinti autentifikaciją.

**Veiksmai:**

1. Iškviesti `DELETE /books/{id}` be JWT.

**Tikėtinas rezultatas:**

* Grąžinama autentifikacijos klaida.
