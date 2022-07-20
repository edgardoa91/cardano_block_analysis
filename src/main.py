from fastapi import FastAPI
from pywebcopy import save_webpage
from bs4 import BeautifulSoup

def save_page(url: str, name: str):
    page = save_webpage(
      url=url,
      project_folder="/tmp/pywebcopy",
      project_name=name,
      bypass_robots=True,
      debug=True,
      open_in_browser=True,
      delay=None,
      threaded=False,
    )
    return page

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/latest_hash")
async def get_latest_hashes():
    # Try to get the latest hashes from the website
    try:
        save_page("https://cardanoscan.io/transactions", "latest_hash")
    except:
        return "Error: Could not save page"
    

    hashes = []
    with open("/tmp/pywebcopy/cardano/cardanoscan.io/transactions.html", "r") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    for i in range(1, 50):
        hash = soup.find_all("a", class_="text-truncate-middle")[0].text
        hashes.append(hash)

    return hashes

@app.get("/transaction/{hash}")
async def get_tansaction(hash: str):
    try:
        with open("/tmp/pywebcopy/"+hash+"/cardanoscan.io/transaction/" + hash + ".html", "r") as f:
            html = f.read()
        # If page has not been saved yet, save it
        if html is None:
            save_page("https://cardanoscan.io/transaction/" + hash, hash)
            with open("/tmp/pywebcopy/"+hash+"/cardanoscan.io/transaction/" + hash + ".html", "r") as f:
                html = f.read()

    except:
        return "Error: Could not save page"
   
    soup = BeautifulSoup(html, "html.parser")
    info = soup.find_all("span", class_="adaAmount")[0].text
    return info


