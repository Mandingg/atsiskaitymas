from fastapi import FastAPI
from app.services.db_connection import DatabaseManager
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router
from app.routes.book_routes import router as book_router


app = FastAPI(title="Atsiskaitymas API")    

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DatabaseManager()


@app.get("/health")
def health_check():
    return {"status": "ok"}


# @app.get("/db-test")
# def db_test():
#     users = db.fetch_all("SELECT * FROM users")
#     return users


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(book_router)
