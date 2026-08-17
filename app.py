from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>WP4TUN.COM | Radioafición</title>

<style>

*{
    box-sizing:border-box;
}

html{
    scroll-behavior:smooth;
}

body{
    margin:0;
    font-family:Arial, Helvetica, sans-serif;
    background:#f4f7fb;
    color:#172033;
}

header{
    background:#101827;
    color:white;
    padding:20px 6%;
    display:flex;
    justify-content:space-between;
    align-items:center;
    position:sticky;
    top:0;
    z-index:1000;
}

.logo{
    font-size:28px;
    font-weight:800;
    letter-spacing:.5px;
}

nav{
    display:flex;
    gap:24px;
    align-items:center;
}

nav a{
    color:white;
    text-decoration:none;
    font-weight:bold;
    font-size:15px;
}

nav a:hover{
    opacity:.75;
}

.hero{
    text-align:center;
    padding:65px 20px 55px;
    background:white;
}

.hero h1{
    font-size:52px;
    margin:0 0 12px;
}

.hero p{
    font-size:21px;
    color:#5d6879;
    margin:0;
}

.section{
    max-width:1200px;
    margin:auto;
    padding:55px 22px;
}

.section-title{
    text-align:center;
    font-size:38px;
    margin:0 0 10px;
}

.section-subtitle{
    text-align:center;
    color:#687386;
    margin:0 auto 35px;
    max-width:750px;
    line-height:1.6;
}

/* 50 STATES */

.states-area{
    background:#f4f7fb;
}

.progress-box{
    max-width:700px;
    margin:0 auto 35px;
    background:white;
    padding:18px 22px;
    border-radius:14px;
    box-shadow:0 5px 18px rgba(0,0,0,.07);
    text-align:center;
}

.progress-box strong{
    font-size:20px;
}

.progress-track{
    width:100%;
    height:12px;
    background:#e4e8ef;
    border-radius:20px;
    margin-top:12px;
    overflow:hidden;
}

.progress-fill{
    width:6%;
    height:100%;
    background:#243b63;
}

/* MAPA VISUAL */

.map-wrapper{
    max-width:1050px;
    margin:0 auto 38px;
    background:white;
    border-radius:20px;
    padding:28px;
    box-shadow:0 8px 28px rgba(0,0,0,.08);
}

.map-title{
    text-align:center;
    font-weight:bold;
    margin-bottom:22px;
    color:#4e596b;
}

.us-map{
    display:grid;
    grid-template-columns:repeat(12,1fr);
    gap:6px;
}

.state{
    min-height:42px;
    border-radius:7px;
    background:#e2e6ed;
    color:#7a8391;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:11px;
    font-weight:bold;
    cursor:default;
    border:1px solid #d5dae3;
}

.state.active{
    background:#243b63;
    color:white;
    cursor:pointer;
    border-color:#243b63;
    box-shadow:0 3px 8px rgba(0,0,0,.16);
}

.state.active:hover{
    transform:translateY(-2px);
}

/* cards */

.state-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:22px;
}

.state-card{
    background:white;
    border-radius:18px;
    padding:32px 20px;
    text-align:center;
    box-shadow:0 6px 22px rgba(0,0,0,.08);
    transition:.2s;
    cursor:pointer;
}

.state-card:hover{
    transform:translateY(-5px);
    box-shadow:0 10px 28px rgba(0,0,0,.12);
}

.state-icon{
    font-size:48px;
}

.state-card h3{
    font-size:25px;
    margin:14px 0 8px;
}

.state-card p{
    color:#697487;
    margin-bottom:18px;
}

.button{
    display:inline-block;
    background:#17233b;
    color:white;
    text-decoration:none;
    padding:11px 20px;
    border-radius:8px;
    font-weight:bold;
}

.coming{
    text-align:center;
    margin:40px 0 5px;
    font-weight:bold;
    color:#566174;
}

/* FUTURE SECTIONS */

.future-section{
    background:white;
}

.feature-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
}

.feature{
    background:#f5f7fa;
    padding:28px 20px;
    border-radius:15px;
    text-align:center;
}

.feature-icon{
    font-size:40px;
}

.feature h3{
    margin:12px 0 8px;
}

.feature p{
    color:#6b7484;
    line-height:1.5;
}

/* FOOTER */

footer{
    background:#101827;
    color:white;
    text-align:center;
    padding:28px 15px;
}

/* MOBILE */

@media(max-width:850px){

    header{
        flex-direction:column;
        gap:15px;
    }

    nav{
        flex-wrap:wrap;
        justify-content:center;
        gap:14px;
    }

    .hero h1{
        font-size:40px;
    }

    .us-map{
        grid-template-columns:repeat(6,1fr);
    }
}

@media(max-width:500px){

    .us-map{
        grid-template-columns:repeat(4,1fr);
    }

    .state{
        min-height:38px;
        font-size:10px;
    }
}

</style>
</head>

<body>

<header>

<div class="logo">WP4TUN.COM</div>

<nav>
<a href="/">Inicio</a>
<a href="#states">50 States</a>
<a href="#encantos">Encantos de PR</a>
<a href="#autoqsl">AUTO QSL</a>
<a href="#videos">Videos</a>
<a href="#recursos">Recursos</a>
<a href="#panel">Mi Panel 🔐</a>
</nav>

</header>


<section class="hero">

<h1>WP4TUN</h1>

<p>Radioafición • Tecnología • Comunidad</p>

</section>


<section class="states-area" id="states">

<div class="section">

<h2 class="section-title">🇺🇸 US 50 STATES</h2>

<p class="section-subtitle">
Una aventura de radioafición a través de los Estados Unidos.
Explora las colecciones QSL de cada estado y acompáñame
en el camino hacia los 50 estados.
</p>


<div class="progress-box">

<strong>3 de 50 estados</strong>

<div class="progress-track">
<div class="progress-fill"></div>
</div>

</div>


<div class="map-wrapper">

<div class="map-title">
MAPA DE COLECCIONES • US 50 STATES
</div>

<div class="us-map">

<div class="state">WA</div>
<div class="state">MT</div>
<div class="state">ND</div>
<div class="state">MN</div>
<div class="state">WI</div>
<div class="state">MI</div>
<div class="state active" onclick="location.href='/new-york'">NY</div>
<div class="state">VT</div>
<div class="state">NH</div>
<div class="state">ME</div>

<div class="state">RI</div>

<div class="state">OR</div>
<div class="state">ID</div>
<div class="state">WY</div>
<div class="state">SD</div>
<div class="state">IA</div>
<div class="state">IL</div>
<div class="state">IN</div>
<div class="state">OH</div>
<div class="state">PA</div>
<div class="state">NJ</div>
<div class="state">CT</div>
<div class="state active" onclick="location.href='/massachusetts'">MA</div>

<div class="state">CA</div>
<div class="state">NV</div>
<div class="state">UT</div>
<div class="state">CO</div>
<div class="state">NE</div>
<div class="state">MO</div>
<div class="state">KY</div>
<div class="state">WV</div>
<div class="state">VA</div>
<div class="state">MD</div>
<div class="state">DE</div>
<div class="state">DC</div>

<div class="state">AZ</div>
<div class="state">NM</div>
<div class="state">KS</div>
<div class="state">OK</div>
<div class="state">AR</div>
<div class="state">TN</div>
<div class="state">NC</div>
<div class="state">SC</div>
<div class="state">GA</div>
<div class="state">AL</div>
<div class="state">MS</div>
<div class="state">LA</div>

<div class="state active" onclick="location.href='/alaska'">AK</div>
<div class="state">HI</div>
<div class="state">TX</div>
<div class="state">FL</div>

</div>

</div>


<div class="state-grid">

<div class="state-card" onclick="location.href='/new-york'">

<div class="state-icon">🗽</div>

<h3>New York</h3>

<p>Colección disponible</p>

<a class="button" href="/new-york">
Ver colección QSL
</a>

</div>


<div class="state-card" onclick="location.href='/alaska'">

<div class="state-icon">🏔️</div>

<h3>Alaska</h3>

<p>Colección disponible</p>

<a class="button" href="/alaska">
Ver colección QSL
</a>

</div>


<div class="state-card" onclick="location.href='/massachusetts'">

<div class="state-icon">🏙️</div>

<h3>Massachusetts</h3>

<p>Colección disponible</p>

<a class="button" href="/massachusetts">
Ver colección QSL
</a>

</div>

</div>


<div class="coming">

Próximamente: nuevas colecciones de US 50 STATES 🇺🇸

</div>

</div>

</section>


<section class="future-section" id="encantos">

<div class="section">

<h2 class="section-title">🇵🇷 Encantos de PR on the Air</h2>

<p class="section-subtitle">
Colecciones especiales dedicadas a Puerto Rico.
</p>

<div class="feature-grid">

<div class="feature">
<div class="feature-icon">🏝️</div>
<h3>Lugares Turísticos</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon">🍽️</div>
<h3>Sabores</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon">🏘️</div>
<h3>Municipios</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon">🐸</div>
<h3>Coquí</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon">🎭</div>
<h3>La Mascota</h3>
<p>Colección QSL</p>
</div>

</div>

</div>

</section>


<section class="section" id="autoqsl">

<h2 class="section-title">📨 AUTO QSL ONLINE</h2>

<p class="section-subtitle">
Próximamente: herramienta para preparar y enviar tus QSL
desde WP4TUN.COM.
</p>

</section>


<section class="future-section" id="videos">

<div class="section">

<h2 class="section-title">🎥 Aprende Radioafición</h2>

<p class="section-subtitle">
Videos educativos, tutoriales y contenido para aprender
y disfrutar más de la radioafición.
</p>

</div>

</section>


<section class="section" id="recursos">

<h2 class="section-title">🌐 Recursos</h2>

<p class="section-subtitle">
Accesos a QRZ, eQSL, YouTube, Google y otros recursos
para radioaficionados.
</p>

</section>


<section class="future-section" id="panel">

<div class="section">

<h2 class="section-title">🔐 Mi Panel</h2>

<p class="section-subtitle">
Área privada de administración de WP4TUN.COM.
</p>

</div>

</section>


<footer>

© 2026 WP4TUN.COM • Raymond Vega-Ramos • Amateur Radio

</footer>

</body>
</html>
"""


@app.route("/")
def inicio():
    return render_template_string(PAGE)


def state_page(state, icon):

    return f"""
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{state} | WP4TUN.COM</title>

<style>

body{{
    margin:0;
    font-family:Arial, Helvetica, sans-serif;
    background:#f4f7fb;
    color:#172033;
}}

header{{
    background:#101827;
    color:white;
    padding:22px;
    text-align:center;
}}

main{{
    max-width:1100px;
    margin:auto;
    padding:50px 20px;
    text-align:center;
}}

h1{{
    font-size:42px;
}}

.icon{{
    font-size:65px;
}}

.gallery{{
    margin-top:35px;
    background:white;
    padding:45px 20px;
    border-radius:18px;
    box-shadow:0 7px 25px rgba(0,0,0,.08);
}}

a{{
    display:inline-block;
    margin-top:30px;
    text-decoration:none;
    background:#17233b;
    color:white;
    padding:12px 22px;
    border-radius:8px;
    font-weight:bold;
}}

</style>

</head>

<body>

<header>
<strong>WP4TUN.COM • US 50 STATES</strong>
</header>

<main>

<div class="icon">{icon}</div>

<h1>{state}</h1>

<p>Colección QSL • WP4TUN</p>

<div class="gallery">

<h2>Galería QSL</h2>

<p>
Aquí colocaremos las QSL de la colección de {state}.
</p>

</div>

<a href="/#states">
← Regresar a US 50 STATES
</a>

</main>

</body>
</html>
"""


@app.route("/new-york")
def new_york():
    return state_page("New York", "🗽")


@app.route("/alaska")
def alaska():
    return state_page("Alaska", "🏔️")


@app.route("/massachusetts")
def massachusetts():
    return state_page("Massachusetts", "🏙️")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
