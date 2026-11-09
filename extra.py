"""Páginas adicionales: Sobre mí (trayectoria y certificados), Notas (artículos) y la hoja de vida en PDF."""
from pathlib import Path

ROOT = Path(__file__).parent

TIMELINE = [
    ("2024", "Empiezo Estadística en la Universidad de Antioquia",
     "Pregrado en Estadística, con grado esperado en 2029. Allí está la base de todo lo demás: probabilidad, inferencia, "
     "modelos y la costumbre de preguntar cuánta incertidumbre hay detrás de un número.", "cientifico"),
    ("Nov. 2024", "Diseñador de formación en IA para empresas",
     "Diseño contenidos para que equipos de empresa, técnicos y no técnicos, usen IA generativa en su trabajo diario. "
     "Construí un curso completo sobre el uso de Claude en procesos de negocio (casos de uso, buenas prácticas de prompts "
     "y flujos de trabajo), con materiales de presentación revisados con un sistema de diseño. También traduje al español "
     "guías técnicas de certificación en IA.", "ia"),
    ("Nov. 2025", "Consultor independiente en análisis de datos y documentación",
     "Apoyo a clientes de distintos sectores con análisis de datos e informes: limpieza y análisis en Python (pandas, SciPy) "
     "y Excel con pruebas estadísticas y gráficos, documentos corporativos en Word y Excel, traducción y digitalización con OCR, "
     "y uso de IA para acelerar la producción con control de calidad.", "analista"),
    ("Ago.–oct. 2026", "90 días, 82 publicaciones, seis proyectos",
     "Seguí un canal educativo de IA y anoté cada publicación. De esas notas salieron los seis proyectos de este portafolio, "
     "todos con código, datos y tests públicos.", "amber"),
    ("2029", "Grado en Estadística (esperado)", "", "muted"),
]

SKILLS = [
    ("Estadística", "cientifico", ["Inferencia y pruebas de hipótesis", "Regresión y modelos lineales", "Calibración de probabilidades",
                                   "PSI, KS y chi-cuadrado", "Variables de confusión", "Diseño de métricas de negocio"]),
    ("Programación", "amber", ["Python", "pandas", "scikit-learn", "SciPy", "matplotlib y Plotly", "pytest"]),
    ("Bases de datos", "analista", ["SQL", "DuckDB", "CTE y funciones de ventana", "Modelado en capas", "Reglas de calidad de datos", "Excel"]),
    ("IA generativa", "ia", ["Claude API y tool use", "RAG y búsqueda híbrida", "Evaluación de LLMs", "Diseño de prompts",
                             "Costo y latencia", "Formación de equipos"]),
]

SOFTWARE = [
    ("Estadística", "cientifico", ["R y RStudio"]),
    ("Datos y BI", "analista", ["Excel avanzado", "Power BI", "Tableau", "Google Sheets y Looker Studio"]),
    ("Desarrollo", "amber", ["VS Code", "Cursor", "PyCharm", "Jupyter y Google Colab", "Anaconda", "Git y GitHub", "PostgreSQL y MySQL"]),
    ("IA", "ia", ["Claude y Claude Code", "ChatGPT y Copilot", "Gemini y NotebookLM", "Perplexity", "OpenAI API y Gemini API",
                  "LangChain y LlamaIndex", "Ollama y LM Studio", "Midjourney"]),
    ("Productividad", "muted", ["Word y PowerPoint", "Notion y Google Workspace", "n8n, Zapier y Make", "Microsoft Teams y Slack"]),
]

LANGS = [("Español", "Nativo"), ("Inglés", "Profesional (B1–B2)"), ("Portugués", "Intermedio"),
         ("Alemán", "Básico"), ("Italiano", "Básico")]

# Para agregar un certificado: ("Nombre", "Entidad", "Año", "enlace de verificación o None")
CERTS = []

NOTES = [
    {
        "slug": "nota-90-dias-canal-ia",
        "title": "Seguí un canal de IA durante 90 días y medí qué me estaba enseñando",
        "date": "Noviembre de 2026", "role": "analista", "project": "my-data-diary-analytics",
        "summary": "Pasé de leer publicaciones a contarlas. El canal empezó enseñando a construir y terminó preparando para buscar empleo.",
        "body": [
            ("p", "Entre agosto y octubre de 2026 seguí un canal educativo de IA y, cada mes, escribí un informe en Word con lo que se había publicado. "
                  "Al final tenía tres documentos y una sensación: el contenido había cambiado. Quise saber si era cierto o solo una impresión."),
            ("h", "Convertir informes en datos"),
            ("p", "Lo primero fue sacar las tablas de los tres informes a un solo dataset. Quedaron 82 publicaciones en 72 días activos. "
                  "Limpié fechas, detecté reenvíos y separé las series que se repiten a propósito de los duplicados reales, que no son lo mismo."),
            ("p", "Para clasificar cada publicación por formato y tema usé reglas escritas a mano, no un modelo. La razón es práctica: con 82 filas, "
                  "una regla se puede leer, discutir y probar con tests. Si una publicación cae en el tema equivocado, sé exactamente por qué."),
            ("h", "Lo que mostraron los números"),
            ("p", "Las publicaciones sobre carrera profesional pasaron del 9 % en agosto al 48 % en octubre. Los proyectos guiados bajaron del 41 % al 16 %, "
                  "y los temas de modelos de lenguaje, del 31 % al 8 %. La impresión era cierta y además tenía una dirección clara: el canal pasó de enseñar a construir a preparar para el empleo."),
            ("h", "Qué me llevo"),
            ("p", "Primero, que vale la pena medir lo que uno consume. Agosto sirve para aprender a construir; septiembre y octubre, para buscar trabajo, y saberlo cambia cómo uso el canal. "
                  "Segundo, que no todo problema de clasificación necesita IA: con pocos datos, una regla auditable es más honesta que un modelo. "
                  "Y tercero, que mis propias notas eran un dataset. De ellas salieron los otros cinco proyectos del portafolio."),
        ],
    },
    {
        "slug": "nota-umbral-churn",
        "title": "Por qué mi modelo de churn decide con 0,25 y no con 0,5",
        "date": "Noviembre de 2026", "role": "cientifico", "project": "churn-prediction-pipeline",
        "summary": "El umbral por defecto no sabe cuánto cuesta una oferta de retención. Elegirlo por beneficio subió la ganancia en 19 %.",
        "body": [
            ("p", "Casi todos los tutoriales de clasificación terminan igual: el modelo da una probabilidad y, si pasa de 0,5, el cliente se clasifica como “se va”. "
                  "Ese número parece neutral, pero esconde una decisión de negocio que nadie tomó."),
            ("h", "El problema real"),
            ("p", "Una empresa de telecomunicaciones quiere ofrecer retención a los clientes con riesgo de irse. Cada oferta cuesta dinero, y cada cliente retenido vale más que esa oferta. "
                  "Equivocarse por no contactar a alguien que se iba no cuesta lo mismo que contactar a alguien que se iba a quedar. Con costos distintos, 0,5 casi nunca es el mejor punto de corte."),
            ("h", "Cómo lo resolví"),
            ("p", "Comparé regresión logística, Random Forest y Gradient Boosting con validación cruzada de 5 folds. El más simple empató con los complejos: PR-AUC de 0,659 frente a 0,657. "
                  "Me quedé con la regresión logística porque se puede explicar variable por variable."),
            ("p", "Después elegí el umbral que maximiza el beneficio, usando predicciones out-of-fold y no el conjunto de prueba. Esto importa: si elijo el umbral mirando el test, el resultado final deja de ser una medición honesta."),
            ("h", "El resultado"),
            ("p", "El umbral óptimo quedó en 0,25. En el conjunto de prueba, el beneficio fue de 51.819 dólares frente a 43.440 con el umbral de 0,5: un 19 % más. "
                  "Con ese umbral se encuentra al 80 % de los clientes que se iban. El ROC-AUC en prueba fue de 0,842."),
            ("h", "Qué me llevo"),
            ("p", "Un modelo no termina en la métrica. La pregunta útil no es “¿qué tan bien clasifica?”, sino “¿qué decisión tomo con esto y cuánto vale?”. "
                  "Elegir el umbral es parte del modelo, y debería hacerse con los números del negocio sobre la mesa."),
        ],
    },
    {
        "slug": "nota-drift-monitoreo",
        "title": "Monitorear los datos no basta: lo que aprendí simulando drift",
        "date": "Noviembre de 2026", "role": "cientifico", "project": "model-drift-monitoring",
        "summary": "Simulé 16 semanas de producción. El cambio que más daño hizo no se veía en los datos, solo en el rendimiento.",
        "body": [
            ("p", "Un modelo entrenado hoy empieza a envejecer mañana. Los clientes cambian, los precios cambian y la relación entre las variables y el resultado también. "
                  "Quería ver ese envejecimiento de cerca, así que lo simulé."),
            ("h", "El montaje"),
            ("p", "Tomé el modelo de churn y simulé 16 semanas de producción con dos tipos de cambio controlados: data drift, cuando cambia la distribución de las variables, "
                  "y concept drift, cuando cambia la relación entre las variables y el churn. Para vigilarlo implementé PSI por variable, pruebas KS y chi-cuadrado, y monitoreo de calibración."),
            ("h", "Lo que pasó"),
            ("p", "La primera alerta de drift llegó en la semana 6. Desde la semana 7, el PSI de MonthlyCharges y Contract entró en zona crítica. La caída fuerte del rendimiento llegó en la semana 8."),
            ("p", "El hallazgo más importante fue incómodo: el concept drift no aparece en el PSI. Las variables pueden verse estables mientras el modelo se equivoca cada vez más. "
                  "Solo se detecta mirando el rendimiento, y para eso hacen falta etiquetas reales."),
            ("h", "Reentrenar también puede salir mal"),
            ("p", "Diseñé una política de reentrenamiento con disparadores por datos y por rendimiento, y un periodo de enfriamiento. Documenté un error propio: un reentrenamiento temprano, con pocos datos nuevos, empeoró el modelo. "
                  "Con la política final, el modelo vivo llegó a un AUC de 0,789 en las semanas 13 a 16, frente a 0,763 del modelo que nunca se actualizó."),
            ("h", "Qué me llevo"),
            ("p", "Vigilar solo los datos da una falsa tranquilidad. Un monitoreo útil combina las dos miradas, datos y rendimiento, y una regla clara de cuándo actuar y cuándo esperar."),
        ],
    },
]

COLOR = {"cientifico": "var(--cientifico)", "ia": "var(--ia)", "analista": "var(--analista)", "amber": "var(--amber)", "muted": "var(--faint)"}


def build(g):
    e, head, nav, FOOT, NAME = g["e"], g["head"], g["nav"], g["FOOT"], g["NAME"]
    BACK, GH, EMAIL, LINKEDIN, CV, PROJECTS = g["BACKDROP_ROLE"], g["GH"], g["EMAIL"], g["LINKEDIN"], g["CV"], g["PROJECTS"]

    # ---------- Sobre mí ----------
    tl = "".join(
        f'<li style="--role:{COLOR[c]}"><p class="when">{e(d)}</p><div><h3>{e(t)}</h3>{f"<p>{e(x)}</p>" if x else ""}</div></li>'
        for d, t, x, c in TIMELINE)
    sk = "".join(
        f'<div class="skill-group" style="--role:{COLOR[c]}"><h3>{e(n)}</h3><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul></div>'
        for n, c, items in SKILLS)
    if CERTS:
        certs = '<ul class="certs">' + "".join(
            f'<li><h3>{e(n)}</h3><p>{e(org)}, {e(y)}</p>{f"<a href={chr(34)}{u}{chr(34)}>Verificar</a>" if u else ""}</li>'
            for n, org, y, u in CERTS) + "</ul>"
    else:
        certs = ('<div class="certs-empty"><p>Estoy reuniendo mis certificados de formación. Este espacio se llenará pronto; '
                 'mientras tanto, cada proyecto del portafolio tiene su código y sus tests públicos como evidencia.</p>'
                 '<div class="slots" aria-hidden="true"><span></span><span></span><span></span></div></div>')
    body = f"""{head(f'Sobre mí · {NAME}', 'Trayectoria, habilidades y certificados de Juan Manuel Herrera Mejia.')}{nav('sobre')}
<main id="contenido" style="--role:var(--amber)">
<section class="role-hero">{BACK}<p class="tabname">sobre_mi.md</p><h1>Sobre mí</h1>
<p class="pitch">Estudio Estadística, enseño IA a equipos de empresa y construyo proyectos de datos que se pueden revisar.</p>
<p>Soy Juan Manuel Herrera Mejia y vivo en Medellín. Me interesa el punto donde la estadística se encuentra con decisiones reales: cuánto vale un modelo en dinero,
cuándo deja de servir y cómo explicárselo a alguien que no programa. Hablo español, inglés y portugués, y estoy aprendiendo alemán e italiano.</p>
<p class="actions"><a class="btn" href="{CV}" download>Descargar hoja de vida (PDF)</a><a class="btn ghost" href="mailto:{EMAIL}">Escribirme</a></p>
</section>
<section class="block"><h2>Trayectoria</h2><ol class="timeline">{tl}</ol></section>
<section class="block"><h2>Habilidades</h2><div class="skill-grid">{sk}</div></section>
<section class="block"><h2>Software que uso</h2><div class="sw-grid">{"".join(f'<div class="sw" style="--role:{COLOR[c]}"><h3>{e(n)}</h3><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul></div>' for n, c, items in SOFTWARE)}</div></section>
<section class="block"><h2>Idiomas</h2><ul class="langs">{"".join(f'<li><span>{e(l)}</span>{e(v)}</li>' for l, v in LANGS)}</ul></section>
<section class="block" id="certificados"><h2>Certificados de formación</h2>{certs}</section>
<section class="block contact-block"><h2>Hablemos</h2>
<p>Estoy abierto a prácticas, empleos y proyectos de análisis de datos, ciencia de datos e IA, en Medellín, híbridos o remotos.</p>
<ul class="contact-list">
<li><span>Correo</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><span>LinkedIn</span><a href="{LINKEDIN}">linkedin.com/in/juanmhmejia</a></li>
<li><span>GitHub</span><a href="{GH}">github.com/jmanuelhe</a></li>
<li><span>Hoja de vida</span><a href="{CV}" download>Descargar PDF</a></li>
</ul></section>
</main>
{FOOT}"""
    (ROOT / "sobre-mi.html").write_text(body, encoding="utf-8")

    # ---------- Notas ----------
    items = "".join(
        f'<li style="--role:{COLOR[n["role"]]}"><p class="when">{e(n["date"])}</p><h2><a href="{n["slug"]}.html">{e(n["title"])}</a></h2><p>{e(n["summary"])}</p></li>'
        for n in NOTES)
    body = f"""{head(f'Notas · {NAME}', 'Artículos cortos sobre lo que aprendí construyendo proyectos de datos e IA.')}{nav('notas')}
<main id="contenido" style="--role:var(--amber)">
<section class="role-hero">{BACK}<p class="tabname">notas/</p><h1>Notas</h1>
<p class="pitch">Lo que aprendí construyendo cada proyecto, contado sin código.</p>
<p>Cada nota sale de un proyecto real del portafolio. Si quieres ver los detalles técnicos, al final de cada una está el enlace al repositorio.</p></section>
<ul class="notes">{items}</ul>
</main>
{FOOT}"""
    (ROOT / "notas.html").write_text(body, encoding="utf-8")

    for n in NOTES:
        prose = "".join(f"<h2>{e(x)}</h2>" if k == "h" else f"<p>{e(x)}</p>" for k, x in n["body"])
        proj = next(p for p in PROJECTS.values() if p["repo"] == n["project"])
        others = "".join(f'<li><a href="{o["slug"]}.html">{e(o["title"])}</a></li>' for o in NOTES if o is not n)
        body = f"""{head(f'{n["title"]} · {NAME}', n['summary'])}{nav('notas')}
<main id="contenido" style="--role:{COLOR[n['role']]}">
<article class="note">
<p class="crumbs"><a href="notas.html">Notas</a></p>
<h1>{e(n['title'])}</h1>
<p class="note-meta">{e(n['date'])}. Juan Manuel Herrera Mejia</p>
<p class="note-lede">{e(n['summary'])}</p>
{prose}
<aside class="note-proj"><p>Proyecto relacionado</p><h3>{e(proj['title'])}</h3>
<p class="links"><a href="{GH}/{proj['repo']}">Ver código en GitHub</a></p></aside>
<nav class="more" aria-label="Otras notas"><h2>Otras notas</h2><ul>{others}</ul></nav>
</article>
</main>
{FOOT}"""
        (ROOT / f"{n['slug']}.html").write_text(body, encoding="utf-8")

    build_cv(g)


CV_PROJECTS = [
    ("My Data Diary Analytics", "Python, pandas, Plotly",
     "Convertí tres informes en Word en un dataset de 82 publicaciones y medí cómo cambió el contenido: el tema carrera pasó de 9 % a 48 %."),
    ("Telco Churn: análisis SQL", "SQL, DuckDB",
     "Nueve consultas con CTE y funciones de ventana. Un segmento con el 13 % de los clientes concentra el 38 % del ingreso perdido."),
    ("Churn Prediction Pipeline", "scikit-learn, SQL",
     "Umbral de decisión elegido por beneficio de negocio: +19 % frente al umbral de 0,5, con ROC-AUC de 0,842 en prueba."),
    ("Model Drift Monitoring", "SciPy, Plotly",
     "16 semanas de producción simuladas con PSI, KS y una política de reentrenamiento. Primera alerta en la semana 6."),
    ("RAG Document Q&A", "Claude API, BM25",
     "Búsqueda híbrida con filtros por fecha: 0,933 de acierto en la primera posición sobre 45 preguntas propias."),
    ("AI CSV Analyst Agent", "Claude tool use",
     "Agente con seis herramientas validadas, límites de pasos y de costo, y tests que corren sin conexión."),
]
CV_SKILLS = [
    ("Estadística", "Inferencia, regresión, calibración, PSI, KS y chi-cuadrado, variables de confusión"),
    ("Machine learning", "scikit-learn, validación cruzada, métricas para clases desbalanceadas, monitoreo de drift"),
    ("Datos", "SQL (CTE, ventanas), DuckDB, PostgreSQL, MySQL, pandas, reglas de calidad de datos"),
    ("IA generativa", "Claude API y tool use, RAG con búsqueda híbrida, evaluación de LLMs, LangChain, Ollama"),
]
CV_SOFTWARE = [
    ("Análisis y BI", "R y RStudio, Excel avanzado, Power BI, Tableau, Google Sheets, Looker Studio"),
    ("Desarrollo", "Python, VS Code, Cursor, PyCharm, Jupyter, Colab, Anaconda, Git y GitHub"),
    ("IA y automatización", "Claude, ChatGPT, Gemini, NotebookLM, Perplexity, n8n, Zapier, Make"),
    ("Oficina", "Word, PowerPoint, Notion, Google Workspace, Teams, Slack"),
]
LEVEL = {"Nativo": 5, "Profesional (B1–B2)": 4, "Intermedio": 3, "Básico": 2}


def build_cv(g):
    e, EMAIL, LINKEDIN, GH = g["e"], g["EMAIL"], g["LINKEDIN"], g["GH"]
    fonts = ROOT / "assets" / "cv-fonts"
    ff = "".join(
        f'@font-face{{font-family:"{fam}";font-weight:{w};src:url("{(fonts / f).resolve().as_uri()}") format("woff2")}}'
        for fam, w, f in [("Public Sans", 400, "public-sans-latin-400-normal.woff2"), ("Public Sans", 500, "public-sans-latin-500-normal.woff2"),
                          ("Public Sans", 600, "public-sans-latin-600-normal.woff2"), ("Public Sans", 700, "public-sans-latin-700-normal.woff2"),
                          ("Bricolage", 600, "bricolage-grotesque-latin-600-normal.woff2"), ("Bricolage", 700, "bricolage-grotesque-latin-700-normal.woff2"),
                          ("Bricolage", 800, "bricolage-grotesque-latin-800-normal.woff2"),
                          ("JBMono", 400, "jetbrains-mono-latin-400-normal.woff2"), ("JBMono", 500, "jetbrains-mono-latin-500-normal.woff2")])
    proj = "".join(f'<div class="proj"><div class="ph"><h4>{e(t)}</h4><span>{e(st)}</span></div><p>{e(d)}</p></div>'
                   for t, st, d in CV_PROJECTS)
    skills = "".join(f'<div class="sg"><h4>{e(n)}</h4><p>{e(t)}</p></div>' for n, t in CV_SKILLS)
    soft = "".join(f'<div class="sg"><h4>{e(n)}</h4><p>{e(t)}</p></div>' for n, t in CV_SOFTWARE)
    langs = "".join(
        f'<li><span class="ln">{e(l)}</span><span class="dots" aria-label="{e(v)}">{"".join("<i class=on></i>" if k < LEVEL.get(v, 3) else "<i></i>" for k in range(5))}</span><span class="lv">{e(v)}</span></li>'
        for l, v in LANGS)
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Hoja de vida, Juan Manuel Herrera Mejia</title>
<style>
{ff}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--ink:#0E1420;--text:#262E3D;--muted:#5D6779;--line:#DCE1E9;--tint:#F3F5F9;--teal:#0F8A73;--blue:#2D6FD2;--violet:#6A4FD0}}
html,body{{width:210mm;height:297mm}}
body{{font:400 8.9pt/1.48 "Public Sans",sans-serif;color:var(--text);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{display:grid;grid-template-columns:1fr 68mm;height:297mm}}
.main{{padding:15mm 9mm 12mm 15mm}}
.side{{background:var(--tint);padding:15mm 10mm 12mm 8.5mm;border-left:1px solid var(--line)}}
h1{{font:800 25pt/1 "Bricolage",sans-serif;color:var(--ink);letter-spacing:-.025em}}
.role{{font:500 10.4pt/1.35 "Public Sans";color:var(--muted);margin-top:7px}}
.rule{{height:3px;width:46mm;margin:11px 0 0;background:linear-gradient(90deg,var(--blue) 0 33.3%,var(--teal) 33.3% 66.6%,var(--violet) 66.6%)}}
h2{{font:700 10.5pt/1 "Bricolage",sans-serif;color:var(--ink);letter-spacing:.01em;margin:17px 0 8px;padding-bottom:5px;border-bottom:1px solid var(--line)}}
.side h2{{margin-top:0}} .side section+section h2{{margin-top:15px}}
p{{margin:0}}
.lead{{font-size:9.3pt;line-height:1.55}}
.job{{margin-bottom:10px}}
.jh{{display:flex;justify-content:space-between;align-items:baseline;gap:8px}}
h3{{font:600 9.7pt/1.3 "Public Sans";color:var(--ink)}}
.date{{font:400 7.6pt "JBMono",monospace;color:var(--muted);white-space:nowrap}}
.org{{color:var(--muted);font-size:8.5pt;margin:1px 0 4px}}
ul{{padding-left:11px}} li{{margin:2px 0}} li::marker{{color:var(--teal)}}
.proj{{padding:6px 0;border-top:1px dashed var(--line)}} .proj:first-of-type{{border-top:0;padding-top:0}}
.ph{{display:flex;justify-content:space-between;align-items:baseline;gap:8px}}
h4{{font:600 9pt/1.3 "Public Sans";color:var(--ink)}}
.ph span{{font:400 7.4pt "JBMono",monospace;color:var(--teal);white-space:nowrap}}
.proj p{{color:var(--text);margin-top:1px}}
.more{{margin-top:7px;font-size:8.3pt;color:var(--muted)}}
.ct{{list-style:none;padding:0}} .ct li{{margin:0 0 6px;font-size:8.3pt;line-height:1.35}}
.ct b{{display:block;font:500 7pt "JBMono",monospace;color:var(--muted);letter-spacing:.02em}}
.ct a{{color:var(--ink);text-decoration:none}}
.edu h3{{font-size:9.2pt}} .edu p{{font-size:8.4pt;color:var(--muted)}}
.sg{{margin-bottom:6px}} .sg h4{{font-size:8.3pt}} .sg p{{font-size:7.9pt;color:var(--text);line-height:1.4}}
.langs{{list-style:none;padding:0}}
.langs li{{display:grid;grid-template-columns:15mm auto 1fr;align-items:center;gap:5px;margin:0 0 5px;font-size:8.3pt}}
.ln{{font-weight:600;color:var(--ink)}}
.dots{{display:flex;gap:2.5px}} .dots i{{width:5.5px;height:5.5px;border-radius:50%;background:#C9D0DC}} .dots i.on{{background:var(--teal)}}
.lv{{font-size:7.2pt;color:var(--muted);text-align:right;white-space:nowrap}}
</style></head><body><div class="page">
<div class="main">
<h1>Juan Manuel Herrera Mejia</h1>
<p class="role">Análisis de datos, machine learning e IA generativa</p>
<div class="rule"></div>
<h2>Perfil</h2>
<p class="lead">Estudiante de Estadística en la Universidad de Antioquia con dos años diseñando formación en IA generativa para empresas y un año como consultor independiente en análisis de datos. Construyo proyectos que se evalúan en términos de negocio, con código, datos y tests públicos.</p>
<h2>Experiencia</h2>
<div class="job"><div class="jh"><h3>Consultor independiente en análisis de datos y documentación</h3><span class="date">nov. 2025 – hoy</span></div>
<p class="org">Independiente, Medellín</p>
<ul><li>Limpieza y análisis de datos en Python (pandas, SciPy) y Excel, con pruebas estadísticas y gráficos.</li>
<li>Informes y documentos corporativos en Word y Excel: estructura, diseño y consolidación de versiones.</li>
<li>Traducción y digitalización de documentos con OCR, y uso de IA con control de calidad.</li></ul></div>
<div class="job"><div class="jh"><h3>Diseñador de formación en IA para empresas</h3><span class="date">nov. 2024 – hoy</span></div>
<p class="org">Independiente, Medellín</p>
<ul><li>Curso completo sobre el uso de Claude en procesos de negocio: casos de uso, prompts y flujos de trabajo.</li>
<li>Materiales de presentación con un sistema de diseño profesional y revisión visual de calidad.</li>
<li>Traducción al español de guías técnicas de certificación en IA.</li></ul></div>
<h2>Proyectos</h2>
{proj}
<p class="more">Código, datos y tests de cada proyecto: github.com/jmanuelhe</p>
</div>
<aside class="side">
<section><h2>Contacto</h2><ul class="ct">
<li><b>Correo</b><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><b>Portafolio</b><a href="https://jmanuelhe.github.io">jmanuelhe.github.io</a></li>
<li><b>LinkedIn</b><a href="{LINKEDIN}">linkedin.com/in/juanmhmejia</a></li>
<li><b>GitHub</b><a href="{GH}">github.com/jmanuelhe</a></li>
<li><b>Ubicación</b>Medellín, Colombia</li></ul></section>
<section class="edu"><h2>Educación</h2><h3>Pregrado en Estadística</h3><p>Universidad de Antioquia</p><p class="date">2024 – 2029 (esperado)</p></section>
<section><h2>Habilidades</h2>{skills}</section>
<section><h2>Software</h2>{soft}</section>
<section><h2>Idiomas</h2><ul class="langs">{langs}</ul></section>
</aside></div></body></html>"""
    src = ROOT / "assets" / "cv.html"
    src.write_text(html, encoding="utf-8")
    import asyncio
    from playwright.async_api import async_playwright

    async def run():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page()
            await pg.goto(src.resolve().as_uri())
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(800)
            h = await pg.evaluate("[...document.querySelectorAll('.main,.side')].map(x=>{const r=[...x.children].pop().getBoundingClientRect();return Math.round(r.bottom)})")
            print("alto de contenido (px):", h, "de", round(297 * 96 / 25.4))
            await pg.pdf(path=str(ROOT / g["CV"]), format="A4", print_background=True, prefer_css_page_size=True)
            await b.close()
    asyncio.run(run())
    src.unlink()
