from fastapi import FastAPI


app = FastAPI(title="Books API")


@app.get("/")
def read_root():
    """Return a welcome message for the API."""
    return {"message": "Welcome to the Books API"}


@app.get("/health")
def health_check():
    """Report whether the API is running."""
    return {"status": "ok"}


# Add your Pydantic models, in-memory data store, and /books endpoints here.