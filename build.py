"""Genera el sitio estático de Family Health: `python build.py`. Todo el contenido vive en este archivo.

Escribe index.html, una página por especialidad (<slug>/index.html), sitemap.xml, robots.txt y llms.txt.
"""
import datetime
import json
import pathlib

BASE = "https://familyhealth-gye.github.io"  # si algún día hay dominio propio, cambiar solo esta línea y volver a generar
OUT = pathlib.Path(__file__).parent

NOMBRE = "Centro de Especialidades Family Health"
TEL_VISIBLE = "096 291 2170"
TEL = "+593962912170"
WA = "https://wa.me/593962912170"
DIRECCION = "Mucho Lote 2, Villa España 2, Mz. 2833, Villa 15, Guayaquil"
MAPA = "https://www.google.com/maps/search/?api=1&query=Centro+de+especialidades+Family+Health+Guayaquil"
REDES = [
    ("Instagram", "https://www.instagram.com/familyhealth.gye/"),
    ("Facebook", "https://www.facebook.com/familyhealthgye"),
    ("TikTok", "https://www.tiktok.com/@familyhealth.gye"),
]
HORARIO = [("Lunes a viernes", "8:30 a. m. – 7:00 p. m."), ("Sábado", "8:30 a. m. – 4:00 p. m."), ("Domingo", "Cerrado")]
AVISO = "Este sitio es informativo y no reemplaza una consulta médica. En una emergencia llama al 911."

# slug, nombre corto, título H1, descripción meta, introducción, servicios, valor de schema.org `specialty` (o None)
ESPECIALIDADES = [
    ("odontologia", "Odontología", "Dentista en Mucho Lote, Guayaquil",
     "Odontología en Mucho Lote, norte de Guayaquil: valoración, limpieza, extracciones, ortodoncia, endodoncia, periodoncia e implantes. Agenda por WhatsApp.",
     "Atención odontológica para niños y adultos en el norte de Guayaquil. En la primera consulta se revisa tu boca y se te explica qué tratamiento necesitas y en qué orden.",
     ["Valoración y diagnóstico dental", "Limpieza dental", "Restauraciones (resinas)", "Extracciones, incluidos los terceros molares",
      "Ortodoncia", "Endodoncia", "Periodoncia", "Implantes dentales", "Diseño de sonrisa", "Odontopediatría"],
     "https://schema.org/Dentistry"),
    ("pediatria", "Pediatría", "Pediatra en Mucho Lote, Guayaquil",
     "Pediatría en Mucho Lote, norte de Guayaquil: control de niño sano, crecimiento y desarrollo, y atención de enfermedades comunes de la infancia.",
     "Consulta pediátrica para el cuidado de tus hijos, desde recién nacidos hasta la adolescencia.",
     ["Control de niño sano", "Seguimiento del crecimiento y el desarrollo", "Atención de enfermedades comunes de la infancia", "Orientación a los padres"],
     "https://schema.org/Pediatric"),
    ("ginecologia", "Ginecología", "Ginecólogo en Mucho Lote, Guayaquil",
     "Ginecología y obstetricia en Mucho Lote, norte de Guayaquil: consulta ginecológica y control del embarazo. Agenda por WhatsApp.",
     "Consulta ginecológica y control del embarazo, con un trato cuidadoso y en un ambiente privado.",
     ["Consulta ginecológica", "Control prenatal", "Papanicolaou", "Ecografía (ver la sección de Ecografía)"],
     "https://schema.org/Gynecologic"),
    ("medicina-general", "Medicina general", "Medicina general en Mucho Lote, Guayaquil",
     "Medicina general y medicina interna en Mucho Lote, norte de Guayaquil: consulta, control de enfermedades crónicas, certificados médicos y recetas.",
     "Consulta médica para adultos: valoración de síntomas, seguimiento de enfermedades crónicas y orientación para derivarte con el especialista cuando lo necesites.",
     ["Consulta de medicina general", "Medicina interna", "Control de presión arterial y de otras enfermedades crónicas", "Certificados médicos", "Recetas"],
     "https://schema.org/PrimaryCare"),
    ("ecografia", "Ecografía", "Ecografía en Mucho Lote, Guayaquil",
     "Ecografía en Mucho Lote, norte de Guayaquil, con informe del estudio. Agenda tu cita por WhatsApp.",
     "Estudios de ecografía realizados en el mismo centro, con informe del estudio. Escríbenos y te decimos cómo prepararte según el estudio que te pidió tu médico.",
     ["Ecografía con informe del estudio", "Estudios solicitados por tu médico tratante"],
     None),
    ("nutricion", "Nutrición", "Nutricionista en Mucho Lote, Guayaquil",
     "Nutrición en Mucho Lote, norte de Guayaquil: valoración nutricional y plan de alimentación según tus necesidades.",
     "Valoración nutricional y plan de alimentación pensado para tus necesidades y tu rutina.",
     ["Valoración nutricional", "Plan de alimentación individual", "Seguimiento de tus controles"],
     "https://schema.org/DietNutrition"),
    ("psicologia", "Psicología", "Psicólogo en Mucho Lote, Guayaquil",
     "Psicología en Mucho Lote, norte de Guayaquil: consulta psicológica y acompañamiento. Agenda por WhatsApp.",
     "Consulta psicológica en un espacio privado y respetuoso.",
     ["Consulta psicológica", "Orientación y acompañamiento"],
     None),
    ("laboratorio", "Laboratorio clínico", "Laboratorio clínico en Mucho Lote, Guayaquil",
     "Laboratorio clínico en Mucho Lote, norte de Guayaquil. Consulta por WhatsApp qué exámenes necesitas.",
     "Exámenes de laboratorio clínico. Escríbenos con la orden de tu médico y te indicamos cómo prepararte.",
     ["Exámenes de laboratorio clínico", "Orientación sobre la preparación para cada examen"],
     None),
]

FAQ = [
    ("¿Necesito cita previa?", f"Atendemos con cita previa. Escríbenos por WhatsApp al {TEL_VISIBLE} y te indicamos los horarios disponibles."),
    ("¿Dónde están ubicados?", f"{DIRECCION}, en el norte de la ciudad."),
    ("¿Cuál es el horario de atención?", "De lunes a viernes de 8:30 a. m. a 7:00 p. m. y los sábados de 8:30 a. m. a 4:00 p. m. Los domingos estamos cerrados."),
    ("¿Atienden a toda la familia?", "Sí. En el mismo centro hay atención para adultos, niños y embarazadas, con varias especialidades."),
    ("¿Cómo agendo mi cita?", f"Por WhatsApp al {TEL_VISIBLE}. Dinos la especialidad que necesitas y qué día te conviene."),
]

CLINICA = {
    "@context": "https://schema.org",
    "@type": "MedicalClinic",
    "@id": f"{BASE}/#clinic",
    "name": NOMBRE,
    "alternateName": ["Family Health Guayaquil"],
    "url": f"{BASE}/",
    "logo": f"{BASE}/logo.png",
    "image": f"{BASE}/logo.png",
    "telephone": TEL,
    "knowsLanguage": "es",
    "address": {"@type": "PostalAddress", "streetAddress": "Mucho Lote 2, Villa España 2, Mz. 2833, Villa 15",
                "addressLocality": "Guayaquil", "addressRegion": "Guayas", "postalCode": "090703", "addressCountry": "EC"},
    "areaServed": {"@type": "City", "name": "Guayaquil"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:30", "closes": "19:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:30", "closes": "16:00"},
    ],
    "medicalSpecialty": [e[6] for e in ESPECIALIDADES if e[6]],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Especialidades", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": e[1], "url": f"{BASE}/{e[0]}/"}} for e in ESPECIALIDADES]},
    "sameAs": [u for _, u in REDES],
}


EMOJI = {"odontologia": "🦷", "pediatria": "👶", "ginecologia": "🤰", "medicina-general": "🩺",
         "ecografia": "🔊", "nutricion": "🥗", "psicologia": "🧠", "laboratorio": "🧪"}
MAPA_EMBED = "https://www.google.com/maps?q=Centro+de+especialidades+Family+Health+Guayaquil&output=embed"
RESENAS = "4,9 en Google · 81 opiniones"  # actualizar a mano cuando cambie (visible en la portada, no va en los datos estructurados)
PASOS = [("Escríbenos por WhatsApp", f"Al {TEL_VISIBLE}, cuéntanos qué especialidad necesitas."),
         ("Elige tu horario", "Te proponemos los horarios disponibles y confirmamos tu cita."),
         ("Ven a tu cita", "Te esperamos en Mucho Lote 2, con tu orden médica si tienes una.")]


def horario_tabla():
    return "<table>" + "".join(f"<tr><td>{d}</td><td>{h}</td></tr>" for d, h in HORARIO) + "</table>"


def pagina(titulo, desc, ruta, cuerpo, ld):
    url = f"{BASE}/{ruta}"
    nav = "".join(f'<a href="/{e[0]}/">{e[1]}</a>' for e in ESPECIALIDADES)
    redes = " · ".join(f'<a href="{u}" rel="me">{n}</a>' for n, u in REDES)
    enlaces = "".join(f'<a href="/{e[0]}/">{e[1]}</a><br>' for e in ESPECIALIDADES[:4])
    enlaces2 = "".join(f'<a href="/{e[0]}/">{e[1]}</a><br>' for e in ESPECIALIDADES[4:])
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0a7a72">
<link rel="canonical" href="{url}">
<link rel="icon" href="/logo-192.webp">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/logo.png">
<meta property="og:locale" content="es_EC">
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top"><div class="wrap bar">
<a class="brand" href="/"><img src="/logo-192.webp" alt="" width="54" height="54"><span>Family Health<small>Centro de Especialidades · Guayaquil</small></span></a>
<nav class="nav" aria-label="Especialidades">{nav}</nav>
<a class="btn btn-sm" href="{WA}">WhatsApp</a>
</div></header>
<main>
{cuerpo}
</main>
<footer><div class="wrap">
<div class="cols">
<div><h3>{NOMBRE}</h3><p>{DIRECCION}</p><p>WhatsApp y teléfono: <a href="{WA}">{TEL_VISIBLE}</a></p><p>{redes}</p></div>
<div><h3>Horario</h3>{horario_tabla()}</div>
<div><h3>Especialidades</h3><p>{enlaces}</p></div>
<div><h3>&nbsp;</h3><p>{enlaces2}</p></div>
</div>
<p class="aviso">{AVISO}</p>
</div></footer>
<a class="flotante" href="{WA}" aria-label="Escríbenos por WhatsApp">💬 WhatsApp</a>
</body>
</html>
"""


def bloque_cita(titulo="¿Listo para agendar tu cita?"):
    return f"""<div class="cta"><h2>{titulo}</h2><p>Escríbenos por WhatsApp y te decimos los horarios disponibles.</p>
<a class="btn" href="{WA}">Agenda por WhatsApp</a></div>"""


def tarjetas_info():
    return f"""<div class="info">
<div class="tarjeta"><h3>Horario de atención</h3>{horario_tabla()}</div>
<div class="tarjeta"><h3>Dónde estamos</h3><p>{DIRECCION}.</p><p><a href="{MAPA}">Cómo llegar</a></p></div>
<div class="tarjeta"><h3>Agenda tu cita</h3><p>Con cita previa, por WhatsApp.</p><p><a href="{WA}"><strong>{TEL_VISIBLE}</strong></a></p></div>
</div>"""


def pagina_inicio():
    tarjetas = "".join(
        f'<li><a href="/{e[0]}/"><span class="ico" aria-hidden="true">{EMOJI[e[0]]}</span><strong>{e[1]}</strong>'
        f'<span class="d">{e[4].split(".")[0]}.</span><span class="mas">Ver más →</span></a></li>' for e in ESPECIALIDADES)
    pasos = "".join(f"<li><strong>{t}</strong>{d}</li>" for t, d in PASOS)
    faqs = "".join(f"<details><summary>{p}</summary><p>{r}</p></details>" for p, r in FAQ)
    cuerpo = f"""<section class="hero"><div class="wrap">
<p class="eyebrow">Mucho Lote 2 · Norte de Guayaquil</p>
<h1>{NOMBRE} en Guayaquil</h1>
<p class="lead">Odontología, pediatría, ginecología, medicina general, ecografía, nutrición, psicología y laboratorio clínico en un solo lugar. Atención para toda la familia con cita previa.</p>
<p class="acciones"><a class="btn btn-claro" href="{WA}">Agenda por WhatsApp</a><a class="btn btn-borde" href="#especialidades">Ver especialidades</a></p>
<ul class="chips"><li>★ {RESENAS}</li><li>Niños, adultos y embarazadas</li><li>Con cita previa</li></ul>
</div></section>
<div class="wrap">
{tarjetas_info()}
<section class="bloque" id="especialidades"><h2>Nuestras especialidades</h2><p class="sub">Elige una para ver qué ofrecemos.</p><ul class="cards">{tarjetas}</ul></section>
<section class="bloque"><h2>Cómo agendar tu cita</h2><p class="sub">Tres pasos, sin filas.</p><ol class="pasos">{pasos}</ol></section>
<section class="bloque"><h2>Dónde encontrarnos</h2><p class="sub">{DIRECCION}.</p>
<div class="dos"><div><iframe class="mapa" title="Mapa de {NOMBRE}" src="{MAPA_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<div><h3>Horario</h3>{horario_tabla()}<p class="acciones" style="margin-top:14px"><a class="btn" href="{MAPA}">Cómo llegar</a></p></div></div></section>
<section class="bloque"><h2>Preguntas frecuentes</h2>{faqs}</section>
{bloque_cita()}
</div>"""
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in FAQ]}
    desc = "Odontología, pediatría, ginecología, medicina general, ecografía, nutrición, psicología y laboratorio en Mucho Lote 2, norte de Guayaquil."
    return pagina(f"{NOMBRE} | Guayaquil", desc, "", cuerpo, [CLINICA, faq_ld])


def pagina_especialidad(e):
    slug, corto, h1, desc, intro, servicios, spec = e
    lista = "".join(f"<li>{s}</li>" for s in servicios)
    otras = "".join(f'<li><a href="/{o[0]}/">{EMOJI[o[0]]} {o[1]}</a></li>' for o in ESPECIALIDADES if o[0] != slug)
    cuerpo = f"""<section class="hero hero-sm"><div class="wrap">
<p class="migas"><a href="/">Inicio</a> › {corto}</p>
<div class="emoji-grande" aria-hidden="true">{EMOJI[slug]}</div>
<h1>{h1}</h1>
<p class="lead">{intro}</p>
<p class="acciones"><a class="btn btn-claro" href="{WA}">Agenda por WhatsApp</a></p>
</div></section>
<div class="wrap">
{tarjetas_info()}
<section class="bloque"><h2>Qué ofrecemos</h2><ul class="checks">{lista}</ul></section>
<section class="bloque"><h2>Dónde y cuándo</h2>
<p>{NOMBRE}, {DIRECCION}. Atendemos con cita previa de lunes a viernes de 8:30 a. m. a 7:00 p. m. y los sábados de 8:30 a. m. a 4:00 p. m.</p></section>
<section class="bloque"><h2>Otras especialidades</h2><ul class="otras">{otras}</ul></section>
{bloque_cita()}
</div>"""
    ld = {"@context": "https://schema.org", "@type": "MedicalWebPage", "name": h1, "description": desc, "url": f"{BASE}/{slug}/",
          "inLanguage": "es", "provider": {"@id": f"{BASE}/#clinic"}}
    if spec:
        ld["specialty"] = spec
    return pagina(f"{h1} | Family Health", desc, f"{slug}/", cuerpo, ld)


def escribir(ruta, texto):
    destino = OUT / ruta
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")


def main():
    escribir("index.html", pagina_inicio())
    for e in ESPECIALIDADES:
        escribir(f"{e[0]}/index.html", pagina_especialidad(e))

    hoy = datetime.date.today().isoformat()
    urls = [f"{BASE}/"] + [f"{BASE}/{e[0]}/" for e in ESPECIALIDADES]
    items = "".join(f"<url><loc>{u}</loc><lastmod>{hoy}</lastmod></url>" for u in urls)
    escribir("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>')
    escribir("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

    lineas = "\n".join(f"- [{e[1]}]({BASE}/{e[0]}/): {e[3]}" for e in ESPECIALIDADES)
    horario = "; ".join(f"{d} {h}" for d, h in HORARIO)
    escribir("llms.txt", f"""# {NOMBRE}

> Centro de especialidades médicas y odontológicas en Mucho Lote 2, norte de Guayaquil, Ecuador. Atención para toda la familia con cita previa.

- Dirección: {DIRECCION}
- WhatsApp y teléfono: {TEL_VISIBLE}
- Horario: {horario}
- Instagram: {REDES[0][1]}
- Facebook: {REDES[1][1]}
- TikTok: {REDES[2][1]}

## Especialidades

{lineas}

## Preguntas frecuentes

{chr(10).join(f"- {p} {r}" for p, r in FAQ)}

{AVISO}
""")
    print(f"{len(ESPECIALIDADES) + 1} páginas generadas")


if __name__ == "__main__":
    main()
