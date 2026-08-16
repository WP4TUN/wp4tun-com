from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
    <head>
        <title>WP4TUN.COM</title>
    </head>
    <body style="font-family:Arial; text-align:center; padding:60px;">
        <h1>WP4TUN.COM</h1>
        <h2>Radioafición • Tecnología • Comunidad</h2>
        <p>Bienvenidos a WP4TUN.COM</p>
        <p>Estamos construyendo un nuevo espacio para la comunidad de radioaficionados.</p>
        <hr>
        <p>📻 AUTO QSL | 🎓 Aprende | 🎥 Videos | 🌐 Recursos | 📅 Actividades | 🖼️ Galería</p>
        <p><strong>Muy pronto...</strong></p>
    </body>
    </html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
