# pasiruosimas

## Testavimo scenarijus

### TC-01 Vartotojo registracija

**Tikslas:** patikrinti, ar vartotojas gali užsiregistruoti.

**Veiksmai:**

1. Atidaryti Swagger (`/docs`)
2. Vykdyti `POST /auth/register`
3. Įvesti:

   * vardą
   * pavardę
   * el. paštą
   * slaptažodį

**Tikėtinas rezultatas:**

* Grąžinamas HTTP 201
* Sukuriamas naujas vartotojas

---

### TC-02 Prisijungimas

**Tikslas:** patikrinti, ar vartotojas gali prisijungti.

**Veiksmai:**

1. Vykdyti `POST /auth/login`
2. Įvesti registruoto vartotojo duomenis

**Tikėtinas rezultatas:**

* Grąžinamas HTTP 200
* Grąžinamas JWT token

---

### TC-03 Autorizacija

**Tikslas:** patikrinti, ar autorizuotas vartotojas gali pasiekti apsaugotus endpointus.

**Veiksmai:**

1. Swagger paspausti `Authorize`
2. Prisijungti naudojant vartotojo duomenis
3. Vykdyti `GET /users/me`

**Tikėtinas rezultatas:**

* Grąžinamas prisijungusio vartotojo profilis
* HTTP 200

---

### TC-04 Rezervacijos sukūrimas

**Tikslas:** patikrinti rezervacijos kūrimą.

**Veiksmai:**

1. Vykdyti `POST /reservations`
2. Užpildyti rezervacijos duomenis

**Tikėtinas rezultatas:**

* HTTP 201
* Rezervacija sukuriama

---

### TC-05 Rezervacijų paieška

**Tikslas:** patikrinti paieškos funkcionalumą.

**Veiksmai:**

1. Sukurti kelias rezervacijas
2. Vykdyti:

`GET /reservations?search=test`

**Tikėtinas rezultatas:**

* Grąžinamos tik paieškos kriterijų atitinkančios rezervacijos

---

### TC-06 Rezervacijos atnaujinimas

**Tikslas:** patikrinti redagavimo funkcionalumą.

**Veiksmai:**

1. Vykdyti `PUT /reservations/{id}`
2. Pakeisti rezervacijos duomenis

**Tikėtinas rezultatas:**

* HTTP 200
* Duomenys atnaujinami

---

### TC-07 Rezervacijos ištrynimas

**Tikslas:** patikrinti šalinimo funkcionalumą.

**Veiksmai:**

1. Vykdyti `DELETE /reservations/{id}`

**Tikėtinas rezultatas:**

* HTTP 200
* Rezervacija pašalinama

