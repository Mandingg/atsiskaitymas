# Knygų katalogo ir vertinimo sistema

Tai REST API pagrindu sukurta knygų katalogo ir vertinimo sistema, leidžianti vartotojams kurti, peržiūrėti, redaguoti ir šalinti savo sukurtus knygų įrašus.

Sistemoje realizuotas JWT autentifikavimas, vartotojų rolės (USER ir ADMIN), knygų kategorijų valdymas bei prieigos kontrolė.

## Pagrindinės funkcijos

* Vartotojų registracija ir prisijungimas
* JWT autentifikacija
* Knygų kūrimas, peržiūra, redagavimas ir šalinimas
* Knygų filtravimas pagal kategoriją
* Knygų rikiavimas pagal įvertinimą
* Kategorijų valdymas (tik ADMIN)
* Prieigos kontrolė pagal vartotojo rolę
* Duomenų validacija
* Automatizuoti verslo logikos testai naudojant Mock mechanizmus

## Naudotos technologijos

* Python
* FastAPI
* MySQL
* Docker
* JWT
* Pytest
* Pydantic

# VARTOTOJO INSTRUKCIJA:

## Sistemos paleidimas

### 1. Atidarykite projekto katalogą

```bash
bash start-dev.sh
```
## arba eikit step-by-step:

```bash
cd backend
```

### 2. Aktyvuokite virtualią aplinką


```bash
venv\Scripts\activate
```

### 3. Įdiekite reikalingas bibliotekas

```bash
pip install -r requirements.txt
```

### 4. Paleiskite MySQL duomenų bazę

```bash
docker compose up -d
```

Patikrinkite ar konteineris veikia:

```bash
docker ps
```

### 5. Paleiskite FastAPI serverį

```bash
uvicorn app.main:app --reload
```

Sėkmingai paleidus sistemą, API bus pasiekiamas adresu:

```txt
http://127.0.0.1:8000
```

Swagger dokumentacija:

```txt
http://127.0.0.1:8000/docs
```

---

