from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Static Web Page Service")

@app.get("/", response_class=HTMLResponse)
def read_root():
    """
    Returns a static HTML webpage directly to the browser.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Python Web Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                display: inline-block;
            }
            h1 { color: #4F46E5; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello World!</h1>
            <p>This static page is served directly using Python and FastAPI.</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
