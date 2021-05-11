from musha.api import API
from store import BookStore


app = API()
book_store = BookStore()
book_store.create(name="Great Book", author="KtechHub")

@app.route('/', allowed_methods=["get"])
def index(req, res):
    books = book_store.all()
    res.html = app.template("index.html", context={"books": books})