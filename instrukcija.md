# Vartotojo instrukcija

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

