from fastapi import FastAPI

app = FastAPI(title="Name Display Service")

@app.get("/")
def home():
    return {"message": "Go to /hello?name=YourName to see it displayed!"}

# This endpoint captures the name parameter from the URL
@app.get("/hello")
def display_name(name: str = "Guest"):
    """
    Displays the name passed in the URL query parameter.
    If no name is provided, it defaults to 'Guest'.
    """
    return {
        "greeting": f"Hello, {name}!",
        "message": f"Your name was successfully processed by the web service."
    }
