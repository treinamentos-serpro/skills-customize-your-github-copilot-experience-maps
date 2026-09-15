from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Book Shelf")
templates = Jinja2Templates(directory="templates")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley", "year": 1818},
]


@app.get("/", response_class=HTMLResponse)
def book_list(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"books": books, "error": None},
    )


@app.post("/books")
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
):
    raise NotImplementedError("Implemente o cadastro e a validação do livro")
