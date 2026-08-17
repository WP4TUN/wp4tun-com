from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WP4TUN.COM | Radioafición</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #f4f7fb;
            color: #172033;
        }

        header {
            background: #101827;
            color: white;
            padding: 24px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 30px;
            font-weight: bold;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 25px;
            font-weight: bold;
        }

        .hero {
            text-align: center;
            padding: 70px 20px 55px;
            background: white;
        }

        .hero h1 {
            font-size: 52px;
            margin: 0 0 15px;
        }

        .hero p {
            font-size: 21px;
            color: #5a6475;
        }

        .states {
            max-width: 1100px;
            margin: 45px auto;
            padding: 0 20px;
        }

        .states h2 {
            text-align: center;
            font-size: 36px;
            margin-bottom: 10px;
        }

        .states-intro {
            text-align: center;
            color: #687386;
            margin-bottom: 35px;
        }

        .state-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 22px;
        }

        .state-card {
            background: white;
            border-radius: 16px;
            padding: 35px 20px;
            text-align: center;
            box-shadow: 0 6px 22px rgba(0,0,0,.08);
            transition: .2s;
        }

        .state-card:hover {
            transform: translateY(-5px);
        }

        .state-icon {
            font-size: 48px;
        }

        .state-card h3 {
            font-size: 25px;
            margin: 15px 0 8px;
        }

        .state-card p {
            color: #6b7484;
        }

        .coming {
            text-align: center;
            margin: 45px 0 60px;
            font-weight: bold;
            color: #566174;
        }

        footer {
            background: #101827;
            color: white;
            text-align: center;
            padding: 25px;
        }
    </style>
</head>

<body>

<header>
    <div class="logo">WP4TUN.COM</div>

    <nav>
        <a href="/">Inicio</a>
        <a href="#states">50 States</a>
        <a href="#">Encantos de PR</a>
        <a href="#">AUTO QSL</a>
        <a href="#">Mi Panel 🔐</a>
    </nav>
</header>

<section class="hero">
    <h1>WP4TUN</h1>
    <p>Radioafición • Tecnología • Comunidad</p>
</section>

<section class="states" id="states">

    <h2>🇺🇸 50 STATES</h2>

    <p class="states-intro">
        Una aventura de radioafición a través de los Estados Unidos.
        Explora las colecciones QSL de cada estado.
    </p>

    <div class="state-grid">

        <div class="state-card">
            <div class="state-icon">🗽</div>
            <h3>New York</h3>
            <p>Ver colección QSL</p>
        </div>

        <div class="state-card">
            <div class="state-icon">🏔️</div>
            <h3>Alaska</h3>
            <p>Ver colección QSL</p>
        </div>

        <div class="state-card">
            <div class="state-icon">🏙️</div>
            <h3>Massachusetts</h3>
            <p>Ver colección QSL</p>
        </div>

    </div>

    <div class="coming">
        Próximamente: el mapa interactivo de los 50 estados 🇺🇸
    </div>

</section>

<footer>
    © 2026 WP4TUN.COM • Raymond Vega-Ramos • Amateur Radio
</footer>

</body>
</html>
"""
