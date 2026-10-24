from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Book(BaseModel):
    title: str
    author: str
    is_borrowed: bool = False
fake_db =[]
@app.get("/")
def read_root():
    return {"message": "Welcome to the Liberary API"}
@app.post("/Book/")
def add_book(book:Book):
    fake_db.append(book)
    return {"message": "successfull added book", "book_data": book}
    