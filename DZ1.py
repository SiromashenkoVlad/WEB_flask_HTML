from flask import Flask

app = Flask(__name__)


@app.route('/')
def page():
    return "Отбор астронавтов"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/choice/<string:planet>')
def choice_planet(planet):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet}</h1>
                        
                        <div class="alert alert-light" role="alert">
                          Эта планета близка к земле;
                        </div>

                        <div class="alert alert-success" role="alert">
                          На ней много необходимых ресурсов; 
                        </div>

                        <div class="alert alert-secondary" role="alert">
                          На ней есть вода и атмосфера;
                        </div>

                        <div class="alert alert-warning" role="alert">
                          На ней есть небольшое магнитное поле;
                        </div>

                        <div class="alert alert-danger" role="alert">
                          Наконец, она просто красива!
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
