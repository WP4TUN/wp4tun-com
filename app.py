from flask import Flask, render_template_string, send_from_directory, request, redirect, session, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-in-render")

HOME = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WP4TUN.COM | Radioafición</title>

<style>
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
    margin:0;
    font-family:Arial,Helvetica,sans-serif;
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
.logo{font-size:28px;font-weight:800}
nav{display:flex;gap:22px;align-items:center;flex-wrap:wrap}
nav a{color:white;text-decoration:none;font-weight:bold;font-size:15px}
nav a:hover{opacity:.75}

.hero{
    text-align:center;
    padding:65px 20px 55px;
    background:white;
}
.hero h1{font-size:52px;margin:0 0 12px}
.hero p{font-size:21px;color:#5d6879;margin:0}

.section{max-width:1200px;margin:auto;padding:55px 22px}
.section-title{text-align:center;font-size:38px;margin:0 0 10px}
.section-subtitle{
    text-align:center;
    color:#687386;
    margin:0 auto 35px;
    max-width:780px;
    line-height:1.6;
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
.progress-track{
    width:100%;
    height:12px;
    background:#e4e8ef;
    border-radius:20px;
    margin-top:12px;
    overflow:hidden;
}
.progress-fill{width:6%;height:100%;background:#243b63}

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
    border:1px solid #d5dae3;
}
.state.active{
    background:#243b63;
    color:white;
    cursor:pointer;
    border-color:#243b63;
    box-shadow:0 3px 8px rgba(0,0,0,.16);
}
.state.active:hover{transform:translateY(-2px)}

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
}
.state-card:hover{transform:translateY(-5px)}
.state-icon{font-size:48px}
.state-card h3{font-size:25px;margin:14px 0 8px}
.state-card p{color:#697487}
.button{
    display:inline-block;
    background:#17233b;
    color:white;
    text-decoration:none;
    padding:11px 20px;
    border-radius:8px;
    font-weight:bold;
}
.coming{text-align:center;margin:40px 0 5px;font-weight:bold;color:#566174}

.future-section{background:white}
.feature-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
    gap:20px;
}
.feature{
    background:#f5f7fa;
    padding:28px 20px;
    border-radius:15px;
    text-align:center;
}
.feature-icon{font-size:40px}
.feature h3{margin:12px 0 8px}
.feature p{color:#6b7484}

footer{
    background:#101827;
    color:white;
    text-align:center;
    padding:28px 15px;
}

@media(max-width:850px){
    header{flex-direction:column;gap:15px}
    nav{justify-content:center;gap:14px}
    .hero h1{font-size:40px}
    .us-map{grid-template-columns:repeat(6,1fr)}
}
@media(max-width:500px){
    .us-map{grid-template-columns:repeat(4,1fr)}
    .state{min-height:38px;font-size:10px}
}
</style>
</head>

<body>

<header>
<div class="logo">WP4TUN.COM</div>
<nav>
<a href="/">Inicio</a>
<a href="#states">50 STATES</a>
<a href="#encantos">ENCANTOS DE PR</a>
<a href="#autoqsl">AUTO QSL</a>
<a href="#videos">Videos</a>
<a href="/herramientas">Herramientas</a>
<a href="/panel">Mi Panel 🔐</a>
</nav>
</header>

<section class="hero">
<h1>WP4TUN</h1>
<p>Radioafición • Tecnología • Comunidad</p>
</section>

<section id="states">
<div class="section">

<h2 class="section-title">50 STATES</h2>

<p class="section-subtitle">
Una aventura de radioafición a través de los Estados Unidos.
Explora las colecciones QSL de cada estado.
</p>

<div class="progress-box">
<strong>3 de 50 estados</strong>
<div class="progress-track"><div class="progress-fill"></div></div>
</div>

<div class="map-wrapper">
<div class="map-title">MAPA DE COLECCIONES • 50 STATES</div>

<div class="us-map">
<div class="state">WA</div><div class="state">OR</div><div class="state">CA</div>
<div class="state">ID</div><div class="state">NV</div><div class="state">MT</div>
<div class="state">WY</div><div class="state">UT</div><div class="state">AZ</div>
<div class="state">ND</div><div class="state">SD</div><div class="state">NE</div>
<div class="state">CO</div><div class="state">NM</div><div class="state">KS</div>
<div class="state">OK</div><div class="state">TX</div><div class="state">MN</div>
<div class="state">IA</div><div class="state">MO</div><div class="state">AR</div>
<div class="state">LA</div><div class="state">WI</div><div class="state">IL</div>
<div class="state">MS</div><div class="state">MI</div><div class="state">IN</div>
<div class="state">KY</div><div class="state">TN</div><div class="state">AL</div>
<div class="state">OH</div><div class="state">WV</div><div class="state">VA</div>
<div class="state">NC</div><div class="state">SC</div><div class="state">GA</div>
<div class="state">FL</div><div class="state">PA</div>
<div class="state active" onclick="location.href='/new-york'">NY</div>
<div class="state">NJ</div><div class="state">DE</div><div class="state">MD</div>
<div class="state">CT</div><div class="state">RI</div>
<div class="state active" onclick="location.href='/massachusetts'">MA</div>
<div class="state">VT</div><div class="state">NH</div><div class="state">ME</div>
<div class="state active" onclick="location.href='/alaska'">AK</div>
<div class="state">HI</div>
</div>
</div>

<div class="state-grid">

<div class="state-card">
<div class="state-icon">🇺🇸</div>
<h3>New York</h3>
<p><strong>10 QSL disponibles</strong></p>
<a class="button" href="/new-york">Ver colección QSL</a>
</div>

<div class="state-card">
<div class="state-icon">🇺🇸</div>
<h3>Alaska</h3>
<p>Colección disponible</p>
<a class="button" href="/alaska">Ver colección QSL</a>
</div>

<div class="state-card">
<div class="state-icon">🇺🇸</div>
<h3>Massachusetts</h3>
<p>Colección disponible</p>
<a class="button" href="/massachusetts">Ver colección QSL</a>
</div>

</div>

<div class="coming">
Próximamente: nuevas colecciones de los 50 estados de Estados Unidos.
</div>

</div>
</section>

<section class="future-section" id="encantos">
<div class="section">

<h2 class="section-title">ENCANTOS DE PR ON THE AIR</h2>
<p class="section-subtitle">
Colecciones especiales dedicadas a Puerto Rico.
</p>

<div class="feature-grid">

<div class="feature">
<div class="feature-icon"></div>
<h3>LUGARES IMPORTANTES</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon"></div>
<h3>SABORES DE PUERTO RICO</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon"></div>
<h3>MUNICIPIOS</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon"></div>
<h3>COQUÍES</h3>
<p>Colección QSL</p>
</div>

<div class="feature">
<div class="feature-icon"></div>
<h3>NUESTRAS MASCOTAS</h3>
<p>Colección QSL</p>
</div>

</div>
</div>
</section>

<section class="section" id="autoqsl">
<h2 class="section-title">📨 AUTO QSL ONLINE</h2>
<p class="section-subtitle">
Próximamente: herramienta para preparar y enviar tus QSL desde WP4TUN.COM.
</p>
</section>

<section class="future-section" id="videos">
<div class="section">
<h2 class="section-title">🎥 Aprende Radioafición</h2>
<p class="section-subtitle">
Videos educativos, tutoriales y contenido para radioaficionados.
</p>
</div>
</section>

<section class="section" id="recursos">
<h2 class="section-title">🌐 Recursos</h2>
<p class="section-subtitle">
Accesos a QRZ, eQSL, YouTube, Google y otros recursos para radioaficionados.
</p>
</section>

<footer>
© 2026 WP4TUN.COM • Raymond Vega-Ramos • Amateur Radio
</footer>

</body>
</html>
"""


NEW_YORK = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>New York on the Air | WP4TUN.COM</title>

<style>
*{box-sizing:border-box}
body{
    margin:0;
    font-family:Arial,Helvetica,sans-serif;
    background:#f4f7fb;
    color:#172033;
}
header{
    background:#101827;
    color:white;
    padding:22px 6%;
    display:flex;
    justify-content:space-between;
    align-items:center;
}
header a{color:white;text-decoration:none;font-weight:bold}

.hero{text-align:center;background:white;padding:45px 20px}
.hero .icon{font-size:58px}
.hero h1{font-size:42px;margin:8px 0}
.hero p{color:#697487;font-size:18px}

.gallery{
    max-width:1300px;
    margin:auto;
    padding:40px 22px 60px;
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:28px;
}
.qsl{
    background:white;
    border-radius:16px;
    overflow:hidden;
    box-shadow:0 7px 24px rgba(0,0,0,.10);
}
.qsl img{
    width:100%;
    display:block;
    cursor:pointer;
}
.qsl-info{
    padding:14px 18px 18px;
    text-align:center;
}
.qsl-info strong{font-size:17px}

.back{text-align:center;padding-bottom:45px}
.back a{
    display:inline-block;
    background:#17233b;
    color:white;
    text-decoration:none;
    padding:12px 22px;
    border-radius:8px;
    font-weight:bold;
}

footer{
    background:#101827;
    color:white;
    text-align:center;
    padding:25px;
}

.modal{
    display:none;
    position:fixed;
    z-index:2000;
    left:0;
    top:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,.92);
    padding:25px;
}
.modal img{
    max-width:95%;
    max-height:90vh;
    position:absolute;
    left:50%;
    top:50%;
    transform:translate(-50%,-50%);
}
.close{
    position:absolute;
    right:30px;
    top:15px;
    color:white;
    font-size:45px;
    cursor:pointer;
    z-index:2001;
}

@media(max-width:800px){
    .gallery{grid-template-columns:1fr}
    header{flex-direction:column;gap:10px}
}
</style>
</head>

<body>

<header>
<strong>WP4TUN.COM • 🇺🇸 50 STATES</strong>
<a href="/#states">← Regresar</a>
</header>

<section class="hero">
<div class="icon">🇺🇸</div>
<h1>New York on the Air</h1>
<p>Colección completa • 10 QSL • WP4TUN</p>
</section>

<div class="gallery">

<div class="qsl">
<img src="/qsl/I.jpg" onclick="openImage(this.src)" alt="Serie 1 - Estatua de la Libertad">
<div class="qsl-info"><strong>Serie 1/10</strong> • Estatua de la Libertad</div>
</div>

<div class="qsl">
<img src="/qsl/II.jpg" onclick="openImage(this.src)" alt="Serie 2 - Times Square">
<div class="qsl-info"><strong>Serie 2/10</strong> • Times Square</div>
</div>

<div class="qsl">
<img src="/qsl/III.jpg" onclick="openImage(this.src)" alt="Serie 3 - Puente de Brooklyn">
<div class="qsl-info"><strong>Serie 3/10</strong> • Puente de Brooklyn</div>
</div>

<div class="qsl">
<img src="/qsl/IV.jpg" onclick="openImage(this.src)" alt="Serie 4 - Parque Central">
<div class="qsl-info"><strong>Serie 4/10</strong> • Parque Central</div>
</div>

<div class="qsl">
<img src="/qsl/V.jpg" onclick="openImage(this.src)" alt="Serie 5 - Empire State">
<div class="qsl-info"><strong>Serie 5/10</strong> • Empire State</div>
</div>

<div class="qsl">
<img src="/qsl/VI.jpg" onclick="openImage(this.src)" alt="Serie 6 - Teatros de Broadway">
<div class="qsl-info"><strong>Serie 6/10</strong> • Teatros de Broadway</div>
</div>

<div class="qsl">
<img src="/qsl/VII.jpg" onclick="openImage(this.src)" alt="Serie 7 - Memorial y Museo del 11 de Septiembre">
<div class="qsl-info"><strong>Serie 7/10</strong> • Memorial y Museo del 11 de Septiembre</div>
</div>

<div class="qsl">
<img src="/qsl/VIII.jpg" onclick="openImage(this.src)" alt="Serie 8 - Museo Metropolitano de Arte">
<div class="qsl-info"><strong>Serie 8/10</strong> • Museo Metropolitano de Arte</div>
</div>

<div class="qsl">
<img src="/qsl/IX.jpg" onclick="openImage(this.src)" alt="Serie 9 - High Line">
<div class="qsl-info"><strong>Serie 9/10</strong> • High Line</div>
</div>

<div class="qsl">
<img src="/qsl/X.jpg" onclick="openImage(this.src)" alt="Serie 10 - Coney Island">
<div class="qsl-info"><strong>Serie 10/10</strong> • Coney Island</div>
</div>

</div>

<div class="back">
<a href="/#states">← Regresar a 50 STATES</a>
</div>

<div id="imageModal" class="modal" onclick="closeImage()">
<span class="close">&times;</span>
<img id="largeImage">
</div>

<footer>
© 2026 WP4TUN.COM • New York on the Air
</footer>

<script>
function openImage(src){
    document.getElementById("largeImage").src=src;
    document.getElementById("imageModal").style.display="block";
}
function closeImage(){
    document.getElementById("imageModal").style.display="none";
}
</script>

</body>
</html>
"""


def state_placeholder(state):
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{state} | WP4TUN.COM</title>
    <style>
    body{{
        font-family:Arial,Helvetica,sans-serif;
        text-align:center;
        margin:0;
        background:#f4f7fb;
        color:#172033
    }}
    header{{
        background:#101827;
        color:white;
        padding:22px
    }}
    main{{padding:70px 20px}}
    .flag{{font-size:65px}}
    h1{{font-size:42px}}
    a{{
        display:inline-block;
        margin-top:25px;
        background:#17233b;
        color:white;
        text-decoration:none;
        padding:12px 22px;
        border-radius:8px
    }}
    </style>
    </head>
    <body>
    <header><strong>WP4TUN.COM • 🇺🇸 50 STATES</strong></header>
    <main>
    <div class="flag">🇺🇸</div>
    <h1>{state}</h1>
    <p>La colección QSL será añadida próximamente.</p>
    <a href="/#states">← Regresar a 50 STATES</a>
    </main>
    </body>
    </html>
    """



TOOLS_PAGE = """
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Herramientas | WP4TUN.COM</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:Arial;background:#f4f7fb;color:#172033}
header{background:#101827;color:#fff;padding:20px 6%;display:flex;justify-content:space-between;align-items:center}
header a{color:#fff;text-decoration:none;font-weight:bold}.wrap{max-width:1100px;margin:auto;padding:45px 22px}
h1{text-align:center;font-size:40px}.sub{text-align:center;color:#687386;margin-bottom:35px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:20px}
.card{background:#fff;border-radius:16px;padding:25px;box-shadow:0 6px 20px rgba(0,0,0,.08)}
.card h2{margin-top:0}.card p{color:#687386;min-height:62px}.btn{display:inline-block;background:#17233b;color:#fff;text-decoration:none;padding:11px 16px;border-radius:8px;font-weight:bold;margin:4px 4px 4px 0}
</style></head><body>
<header><strong>WP4TUN.COM • HERRAMIENTAS</strong><a href="/">← Inicio</a></header>
<div class="wrap"><h1>Herramientas de Radioafición</h1><p class="sub">Accesos y descargas para radioaficionados.</p>
<div class="grid">
<div class="card"><h2>EchoLink</h2><p>Acceso web oficial y descarga del programa.</p><a class="btn" href="https://webapp.echolink.org" target="_blank">Abrir EchoLink Web</a><a class="btn" href="https://secure.echolink.org/download.htm" target="_blank">Descargar</a></div>
<div class="card"><h2>Peanut</h2><p>Proyecto Peanut de PA7LIM, dashboard y software oficial.</p><a class="btn" href="https://peanut.pa7lim.nl" target="_blank">Dashboard</a><a class="btn" href="https://www.pa7lim.nl/peanut/" target="_blank">Peanut oficial</a></div>
<div class="card"><h2>Cliente Peanut</h2><p>Información del Cliente Peanut de LW6EMN.</p><a class="btn" href="https://www.lw6emn.ar/" target="_blank">Abrir sitio</a></div>
<div class="card"><h2>VoxDMR</h2><p>DMR desde Windows, Linux y Android.</p><a class="btn" href="https://www.voxdmr.com/" target="_blank">Abrir VoxDMR</a><a class="btn" href="https://www.voxdmr.com/docs/installation/" target="_blank">Instalar</a></div>
<div class="card"><h2>Zello</h2><p>Aplicaciones oficiales de Zello para escritorio y móvil.</p><a class="btn" href="https://zello.com/downloads/" target="_blank">Descargar Zello</a></div>
</div></div></body></html>
"""

LOGIN_PAGE = """
<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mi Panel | WP4TUN.COM</title><style>
body{margin:0;font-family:Arial;background:#f4f7fb;color:#172033}.box{max-width:420px;margin:90px auto;background:#fff;padding:35px;border-radius:18px;box-shadow:0 8px 28px rgba(0,0,0,.12)}
h1{text-align:center}input{width:100%;padding:13px;margin:8px 0;border:1px solid #ccd3dd;border-radius:8px;font-size:16px}
button{width:100%;padding:13px;margin-top:12px;background:#17233b;color:#fff;border:0;border-radius:8px;font-weight:bold;font-size:16px;cursor:pointer}
.error{color:#b00020;text-align:center}.back{text-align:center;margin-top:18px}.back a{color:#17233b}
</style></head><body><div class="box"><h1>🔐 Mi Panel</h1><p style="text-align:center">Acceso privado de WP4TUN.COM</p>
{% if error %}<p class="error">{{ error }}</p>{% endif %}
<form method="post"><input name="username" placeholder="Usuario" required autocomplete="username"><input type="password" name="password" placeholder="Contraseña" required autocomplete="current-password"><button type="submit">ENTRAR</button></form>
<div class="back"><a href="/">← Regresar a WP4TUN.COM</a></div></div></body></html>
"""

PANEL_PAGE = """
<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mi Panel | WP4TUN.COM</title><style>
*{box-sizing:border-box}body{margin:0;font-family:Arial;background:#f4f7fb;color:#172033}
header{background:#101827;color:#fff;padding:20px 6%;display:flex;justify-content:space-between;align-items:center;gap:15px}header a{color:#fff;text-decoration:none;font-weight:bold}
.wrap{max-width:1150px;margin:auto;padding:42px 22px}h1{text-align:center;font-size:40px;margin-bottom:8px}.sub{text-align:center;color:#687386;margin-bottom:35px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}.card{background:#fff;border-radius:16px;padding:25px;box-shadow:0 6px 20px rgba(0,0,0,.08)}
.card h2{margin-top:0}.card p{color:#687386;min-height:72px}.btn{display:inline-block;background:#17233b;color:#fff;text-decoration:none;padding:11px 16px;border-radius:8px;font-weight:bold;margin:4px 4px 4px 0}
.note{background:#fff8dd;border-radius:12px;padding:16px;margin:0 0 28px}
</style></head><body>
<header><strong>WP4TUN.COM • MI PANEL 🔐</strong><div><a href="/">Inicio</a> &nbsp; | &nbsp; <a href="/logout">Cerrar sesión</a></div></header>
<p><b>Acceso privado del administrador.</b></p>

<div style="background:#fff3cd;padding:15px;border-radius:10px;margin:18px 0;">
<b>Centro de comunicaciones WP4TUN</b><br>
Desde este panel puedes acceder a tus sistemas de radioafición.
</div>

<div style="display:flex;flex-wrap:wrap;gap:20px;">

<div style="background:white;padding:22px;border-radius:14px;width:250px;">
<h2>EchoLink Web</h2>
<p>Acceso directo mediante el navegador.</p>
<a class="btn" href="https://webapp.echolink.org" target="_blank">ABRIR ECHOLINK WEB</a>
</div>

<div style="background:white;padding:22px;border-radius:14px;width:250px;">
<h2>Peanut Global</h2>
<p>Dashboard y estaciones activas de Peanut.</p>
<a class="btn" href="https://peanut.pa7lim.nl" target="_blank">ABRIR PEANUT GLOBAL</a>
</div>

<div style="background:white;padding:22px;border-radius:14px;width:250px;">
<h2>Cliente Peanut</h2>
<p>Abrir Cliente Peanut instalado en esta computadora.</p>
<a class="btn" href="http://127.0.0.1:8765/peanut" target="_blank">ABRIR CLIENTE PEANUT</a>
</div>

<div style="background:white;padding:22px;border-radius:14px;width:250px;">
<h2>VoxDMR</h2>
<p>Abrir VoxDMR instalado en esta computadora.</p>
<a class="btn" href="http://127.0.0.1:8765/voxdmr" target="_blank">ABRIR VOXDMR</a>
</div>

<div style="background:white;padding:22px;border-radius:14px;width:250px;">
<h2>Zello</h2>
<p>Abrir Zello instalado en esta computadora.</p>
<a class="btn" href="http://127.0.0.1:8765/zello" target="_blank">ABRIR ZELLO</a>
</div>

</div>
</div></div></body></html>
"""

@app.route("/")
def inicio():
    return render_template_string(HOME)


@app.route("/new-york")
def new_york():
    return render_template_string(NEW_YORK)


@app.route("/alaska")
def alaska():
    return state_placeholder("Alaska")


@app.route("/massachusetts")
def massachusetts():
    return state_placeholder("Massachusetts")



@app.route("/herramientas")
def herramientas():
    return render_template_string(TOOLS_PAGE)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("admin"):
        return redirect(url_for("panel"))
    error = None
    if request.method == "POST":
        admin_user = os.environ.get("ADMIN_USER", "wp4tun")
        admin_pass = os.environ.get("ADMIN_PASSWORD")
        if not admin_pass:
            error = "El administrador todavía no ha configurado la contraseña en Render."
        elif request.form.get("username") == admin_user and request.form.get("password") == admin_pass:
            session["admin"] = True
            return redirect(url_for("panel"))
        else:
            error = "Usuario o contraseña incorrectos."
    return render_template_string(LOGIN_PAGE, error=error)


@app.route("/panel")
def panel():
    if not session.get("admin"):
        return redirect(url_for("login"))
    return render_template_string(PANEL_PAGE)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("inicio"))


@app.route("/qsl/<path:filename>")
def qsl_images(filename):
    return send_from_directory(".", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
