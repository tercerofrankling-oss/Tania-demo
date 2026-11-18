from pathlib import Path

archivo = Path("index.html")
html = archivo.read_text(encoding="utf-8")

MARCA = "ANIMACION-ARBOL-TANIA-V2"

if MARCA in html:
    print("La nueva animación ya está instalada.")
    raise SystemExit

css = r"""
<!-- ANIMACION-ARBOL-TANIA-V2 -->
<style>
#animacionTania {
    position: fixed;
    inset: 0;
    z-index: 99999;
    display: none;
    overflow: hidden;
    background: #fff3df;
    color: #743c56;
    font-family: Georgia, serif;
    text-align: center;
}

#animacionTania.visible {
    display: block;
}

.escena-tania {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 25px;
    opacity: 0;
    visibility: hidden;
    transition: opacity 1.2s ease;
}

.escena-tania.mostrar {
    opacity: 1;
    visibility: visible;
}

#escenaCorazon {
    background:
        radial-gradient(circle, #fffaf0, #f9e8d2 75%);
}

.corazon-brillante {
    font-size: 100px;
    animation: latidoBrillante 1.1s infinite;
    filter: drop-shadow(0 0 15px #ff729d)
            drop-shadow(0 0 35px #ff8eaa);
}

@keyframes latidoBrillante {
    0%, 100% {
        transform: scale(1);
        filter: drop-shadow(0 0 12px #ff729d);
    }
    50% {
        transform: scale(1.2);
        filter: drop-shadow(0 0 35px #ff3e83);
    }
}

.texto-corazon {
    color: #a85c72;
    font-size: 20px;
    margin-top: 25px;
    animation: aparecerTexto 2s ease;
}

#circuloTransicion {
    position: absolute;
    width: 30px;
    height: 30px;
    left: 50%;
    top: 50%;
    border-radius: 50%;
    background: #ed719f;
    transform: translate(-50%, -50%) scale(0);
    z-index: 10;
}

#animacionTania.transicion #circuloTransicion {
    animation: expandirCirculo 1.4s ease-in forwards;
}

@keyframes expandirCirculo {
    to {
        transform: translate(-50%, -50%) scale(55);
    }
}

#escenaArbol {
    background:
        radial-gradient(ellipse at center, #fff9ec, #f5e5d0);
}

.titulo-cumple {
    position: relative;
    z-index: 5;
    color: #bd587c;
    font-size: clamp(34px, 9vw, 58px);
    text-shadow: 0 3px 12px #eeb5c5;
    margin-bottom: 5px;
    opacity: 0;
    transform: scale(.6);
}

#escenaArbol.mostrar .titulo-cumple {
    animation: tituloCumple 1.5s ease forwards;
}

@keyframes tituloCumple {
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.subtitulo-cumple {
    color: #a46a70;
    font-size: 18px;
    margin-bottom: 5px;
    opacity: 0;
    animation: aparecerTexto 2s 1s forwards;
}

.arbol-contenedor {
    position: relative;
    width: min(95vw, 440px);
    height: min(65vh, 490px);
    margin-top: 5px;
}

#arbolSVG {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    overflow: visible;
}

.rama-arbol {
    fill: none;
    stroke: #956044;
    stroke-width: 9;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 700;
    stroke-dashoffset: 700;
}

#escenaArbol.mostrar .rama-arbol {
    animation: crecerRama 4s ease forwards;
}

.rama-fina {
    stroke: #a87952;
    stroke-width: 4;
}

@keyframes crecerRama {
    to {
        stroke-dashoffset: 0;
    }
}

#floresTania {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

.flor-tania {
    position: absolute;
    opacity: 0;
    transform: scale(0) rotate(-40deg);
    font-size: clamp(17px, 5vw, 27px);
    filter: drop-shadow(0 2px 4px #d99a9a);
    animation: florecer .8s ease forwards;
}

@keyframes florecer {
    60% {
        transform: scale(1.3) rotate(15deg);
    }
    100% {
        opacity: 1;
        transform: scale(1) rotate(0);
    }
}

.mensaje-arbol {
    color: #a54e72;
    font-size: clamp(20px, 5vw, 27px);
    margin-top: 3px;
    opacity: 0;
    transform: translateY(15px);
}

#escenaArbol.mensaje-visible .mensaje-arbol {
    animation: mensajeFinal 1.5s ease forwards;
}

@keyframes mensajeFinal {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.continuar-arbol {
    position: absolute;
    bottom: 25px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, #c65e88, #ed9bb3);
    color: white;
    border: 1px solid #fff;
    border-radius: 30px;
    padding: 13px 25px;
    font-size: 16px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 1s;
    white-space: nowrap;
}

.continuar-arbol.disponible {
    opacity: 1;
    pointer-events: auto;
}

@keyframes aparecerTexto {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}

@media(max-height:650px) {
    .arbol-contenedor {
        height: 53vh;
    }
    .titulo-cumple {
        font-size: 34px;
    }
    .continuar-arbol {
        bottom: 8px;
    }
}
</style>
"""

cuerpo = r"""
<!-- ANIMACION-ARBOL-TANIA-V2 -->
<div id="animacionTania">

    <div id="escenaCorazon" class="escena-tania mostrar">
        <div class="corazon-brillante">❤️</div>
        <p class="texto-corazon">
            Un pequeño detalle hecho con mucho cariño...
        </p>
    </div>

    <div id="circuloTransicion"></div>

    <div id="escenaArbol" class="escena-tania">
        <h1 class="titulo-cumple">Happy Birthday</h1>

        <p class="subtitulo-cumple">
            Para alguien muy especial ❤️
        </p>

        <div class="arbol-contenedor">

            <svg id="arbolSVG" viewBox="0 0 400 460"
                 preserveAspectRatio="xMidYMid meet">

                <!-- Tronco principal -->
                <path class="rama-arbol"
                    d="M200 450
                       C195 390 205 340 200 285
                       C198 240 200 195 200 160"/>

                <!-- Ramas grandes -->
                <path class="rama-arbol"
                    d="M200 300
                       C155 260 125 220 90 175"/>

                <path class="rama-arbol"
                    d="M200 285
                       C245 245 275 210 315 170"/>

                <path class="rama-arbol"
                    d="M200 230
                       C165 195 145 165 135 120"/>

                <path class="rama-arbol"
                    d="M200 220
                       C230 185 255 145 265 110"/>

                <!-- Ramas pequeñas -->
                <path class="rama-arbol rama-fina"
                    d="M145 225 Q105 210 75 200"/>

                <path class="rama-arbol rama-fina"
                    d="M120 210 Q130 175 105 150"/>

                <path class="rama-arbol rama-fina"
                    d="M265 225 Q300 205 335 195"/>

                <path class="rama-arbol rama-fina"
                    d="M280 205 Q275 165 305 140"/>

                <path class="rama-arbol rama-fina"
                    d="M170 185 Q145 150 160 105"/>

                <path class="rama-arbol rama-fina"
                    d="M230 180 Q255 145 240 95"/>

                <path class="rama-arbol rama-fina"
                    d="M200 160 Q180 120 200 80"/>

            </svg>

            <div id="floresTania"></div>

        </div>

        <p class="mensaje-arbol">
            ¡Felices 15 años, Tania! 🎂❤️
        </p>

        <button class="continuar-arbol" id="continuarArbol"
                onclick="terminarAnimacionTania()">
            Descubrir mi sorpresa 💌
        </button>

    </div>

</div>
"""

javascript = r"""
/* ANIMACION-ARBOL-TANIA-V2 */

let animacionIniciada = false;

function iniciarAnimacionTania() {

    if (animacionIniciada) return;

    animacionIniciada = true;

    const contenedor = document.getElementById("animacionTania");
    const escenaCorazon = document.getElementById("escenaCorazon");
    const escenaArbol = document.getElementById("escenaArbol");
    const botonContinuar = document.getElementById("continuarArbol");

    contenedor.classList.add("visible");

    // Primera escena: corazón brillante
    setTimeout(() => {

        escenaCorazon.classList.remove("mostrar");
        contenedor.classList.add("transicion");

    }, 2800);

    // Transición circular rosa
    setTimeout(() => {

        contenedor.classList.remove("transicion");
        escenaArbol.classList.add("mostrar");

        crearFloresTania();

    }, 4300);

    // Mensaje final
    setTimeout(() => {

        escenaArbol.classList.add("mensaje-visible");

    }, 8500);

    // Mostrar botón para continuar
    setTimeout(() => {

        botonContinuar.classList.add("disponible");

    }, 10500);

}

function crearFloresTania() {

    const contenedor = document.getElementById("floresTania");

    if (contenedor.children.length > 0) return;

    const flores = ["🌸", "🌷", "🌺", "💗", "🌼", "❤️"];

    // Puntos que forman una copa de árbol con silueta de corazón
    const posiciones = [
        [50, 5], [39, 8], [61, 8],
        [29, 15], [71, 15],
        [20, 25], [35, 23], [50, 19], [65, 23], [80, 25],
        [14, 36], [28, 34], [42, 32], [58, 32], [72, 34], [86, 36],
        [20, 47], [35, 44], [50, 42], [65, 44], [80, 47],
        [30, 56], [42, 54], [58, 54], [70, 56],
        [40, 63], [50, 61], [60, 63]
    ];

    posiciones.forEach((posicion, indice) => {

        const flor = document.createElement("span");

        flor.className = "flor-tania";

        flor.textContent = flores[indice % flores.length];

        flor.style.left = posicion[0] + "%";
        flor.style.top = posicion[1] + "%";

        flor.style.animationDelay = (indice * 0.13) + "s";

        contenedor.appendChild(flor);

    });

}

function terminarAnimacionTania() {

    const contenedor = document.getElementById("animacionTania");

    contenedor.style.transition = "opacity 1.2s ease";
    contenedor.style.opacity = "0";

    setTimeout(() => {

        contenedor.classList.remove("visible");
        contenedor.style.opacity = "";
        contenedor.style.transition = "";

        // La pantalla original de inicio permanece intacta.

    }, 1300);

}
"""

# Insertar estilos antes del cierre de HEAD
if "</head>" not in html:
    raise SystemExit("No se encontró </head>.")

html = html.replace("</head>", css + "\n</head>", 1)

# Insertar la animación antes del cierre de BODY
if "</body>" not in html:
    raise SystemExit("No se encontró </body>.")

html = html.replace("</body>", cuerpo + "\n</body>", 1)

# Insertar JavaScript antes del cierre del SCRIPT original
# Se añade justo antes de </script> para mantener todo en el mismo bloque.
if "</script>" not in html:
    raise SystemExit("No se encontró </script>.")

html = html.replace("</script>", javascript + "\n</script>", 1)

# Ejecutar la animación cuando termina el reto del corazón.
busqueda = """acceso.classList.add("oculto");

                activarMusica();"""

reemplazo = """acceso.classList.add("oculto");

                activarMusica();

                iniciarAnimacionTania();"""

if busqueda not in html:
    raise SystemExit(
        "No se encontró el punto de activación. "
        "No se modificó el archivo."
    )

html = html.replace(busqueda, reemplazo, 1)

archivo.write_text(html, encoding="utf-8")

print("¡Animación del árbol instalada correctamente!")
print("Tu diseño original y tus demás pantallas se conservaron.")
