from fastapi.responses import HTMLResponse
from fastapi import status
from . import router

@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Learning Age Creatives</title>
            <style>
                body {
                    font-family: Arial;
                    margin: 1rem;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 90vh;
                }

                h1 {
                    margin: 0;
                    padding-top: 1.5rem;
                    font-size: 2.5rem;
                    text-align: center;
                }
                a {
                    font-weight: bold;
                    font-size: 1.5rem;
                    margin: 0;
                    padding-top: 1.5rem;
                }

            </style>
        </head>
        <body>
            <img src="https://ik.imagekit.io/learningage/site-images/learning-age-creatives-logo-small_RZZFuFora.png" alt="Learning Age Logo" />

            <h1>Welcome to Learning Age Preschool & Daycare</h1>

            <a rel="noopener noreferrer" href="https://learning-age-website.vercel.app/">Proceed to our website</a>
        </body>
    </html>    
    """