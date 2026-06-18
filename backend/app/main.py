from fastapi import FastAPI
from app.services.db_connection import DatabaseManager


from app.routes.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router
from app.routes.book_routes import router as book_router
from app.routes.category_routes import router as category_router


app = FastAPI(title="Atsiskaitymas API")    


db = DatabaseManager()


@app.get("/health")
def health_check():
    return {"status": "ok"}



app.include_router(auth_router)
app.include_router(user_router)
app.include_router(book_router)
app.include_router(category_router)
