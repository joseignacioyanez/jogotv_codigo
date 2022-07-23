import os
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/favoritos")
def favoritos():
    colorFondo = '#E58B81'
    tarjeta = "tarjeta-favoritos.png"
    playlistURL = ""
    return render_template("reproductor.html", colorFondo=colorFondo, tarjeta=tarjeta, playlistURL=playlistURL)

@app.route("/ciencia")
def ciencia():
    colorFondo = '#A8D86E'
    tarjeta = "tarjeta-ciencia.png"
    playlistURL = "PLxMv70B4NXQyNEqaws4juBgpnHGSbcsPo"
    return render_template("reproductor.html", colorFondo=colorFondo, tarjeta=tarjeta, playlistURL=playlistURL)

@app.route("/historia")
def historia():
    colorFondo = '#FFE062'
    tarjeta = "tarjeta-historia.png"
    playlistURL = "PL_Y3qbepMRoajNUpI7PqyGhtACju9Dxp5"
    return render_template("reproductor.html", colorFondo=colorFondo, tarjeta=tarjeta, playlistURL=playlistURL)

@app.route("/deportes")
def deportes():
    colorFondo = '#FFA772'
    tarjeta = "tarjeta-deportes.png"
    playlistURL = "PLq0weGgC6sGzM_iFx9k3lQifzHhDxmL_m"
    return render_template("reproductor.html", colorFondo=colorFondo, tarjeta=tarjeta, playlistURL=playlistURL)

@app.route("/arte")
def arte():
    colorFondo = '#8FA9ED'
    tarjeta = "tarjeta-arte.png"
    playlistURL = "PLtek_C8j37x8y3Aj9p2k3PBjQspMneqSD"
    return render_template("reproductor.html", colorFondo=colorFondo, tarjeta=tarjeta, playlistURL=playlistURL)

@app.route("/entretenimiento")
def entretenimiento():
    colorFondo = '#FFA5E6'
    tarjeta = "tarjeta-entretenimiento.png"
    playlistURL = "PLVI9tQggdGtHjPkCPD5X5EsOYk1rA-gew"
    return render_template("reproductor.html", colorFondo=colorFondo, tarjeta=tarjeta, playlistURL=playlistURL)

