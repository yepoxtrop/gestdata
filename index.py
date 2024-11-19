from app import crear_app;
from flask import render_template;
from waitress import serve

app = crear_app()  

@app.errorhandler(404)
def error404(error):
    return render_template("Error404.html", error=error)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000, threads=4)  


