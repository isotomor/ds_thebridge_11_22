from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My third API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/v0/books', methods=['GET'])
def all_books():
    return jsonify(books)
    
# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
@app.route('/v0/book_id', methods=['GET'])
def book_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        results = [book for book in books if book['id']==id]
        if results == []:
            return "Book id not found"
        else:
            return jsonify(results)
    else:
        return "Id not found in the request"
    
@app.route('/v0/book_id_list', methods=['GET'])
def book_id_list():
    if 'id' in request.args:
        results = []
        id_list = list(request.args['id'][1:-1])
        print(id_list)
        for id in id_list:
            try:
                id = int(id)
            except:
                continue
            for book in books:
                if book['id']==id:
                    results.append(book)
        if results == []:
            return "Book id not found"
        else:
            return jsonify(results)
    else:
        return "Id not found in the request"



# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada de otra forma
@app.route('/v0/book/<string:title>', methods=["GET"])
def book_title(title):
    results = [book for book in books if book['title']==title]
    if results == []:
        return "Book title not found"
    else:
        return jsonify(results)



# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada  
@app.route('/v1/book', methods=["GET"])
def book_title_body():
    title = request.get_json()['title']
    results = [book for book in books if book['title']==title]
    if results == []:
        return "Book title not found"
    else:
        return jsonify(results)

# 5.Ruta para añadir un libro mediante un json en la llamada



# 6.Ruta para añadir un libro mediante parámetros

 

# 7.Ruta para modificar un libro



# 8.Ruta para eliminar un libro



app.run()