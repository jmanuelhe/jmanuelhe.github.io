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
    ("analista", "My Data Diary Analytics", "9 % → 48 %", "de publicaciones sobre carrera profesional",
     "Convertí tres informes en Word en un dataset de 82 publicaciones y medí cómo cambió un canal educativo de IA en tres meses.",
     ["Python", "pandas", "Plotly"]),
    ("analista", "Telco Churn: análisis SQL", "38 %", "del ingreso perdido está en el 13 % de los clientes",
     "Nueve consultas con CTE y funciones de ventana, reglas de calidad de datos y control de una variable de confusión.",
     ["SQL", "DuckDB", "pandas"]),
    ("cientifico", "Churn Prediction Pipeline", "+19 %", "de beneficio frente al umbral de 0,5",
     "Comparé tres modelos con validación cruzada y elegí el umbral de decisión por beneficio de negocio. ROC-AUC de 0,842.",
     ["scikit-learn", "SQL", "joblib"]),
    ("cientifico", "Model Drift Monitoring", "Semana 6", "primera alerta, dos semanas antes de la caída",
     "Simulé 16 semanas de producción con PSI, KS y chi-cuadrado, y diseñé una política de reentrenamiento.",
     ["SciPy", "scikit-learn", "Plotly"]),
    ("ia", "RAG Document Q&A", "0,933", "de acierto en la primera posición",
     "Búsqueda híbrida (BM25 y TF-IDF) con filtros por fecha y respuestas de Claude con citas verificables.",
     ["Claude API", "BM25", "Streamlit"]),
    ("ia", "AI CSV Analyst Agent", "6", "herramientas validadas, sin código arbitrario",
     "Agente con tool use, límites de pasos y de costo en USD, registro de latencia y tests que corren sin conexión.",
     ["Claude tool use", "pandas", "pytest"]),
]
CV_SKILLS = [
    ("Estadística", "cientifico", ["Inferencia y pruebas de hipótesis", "Regresión", "Calibración de probabilidades", "PSI, KS y chi-cuadrado", "Variables de confusión"]),
    ("Machine learning", "cientifico", ["scikit-learn", "Validación cruzada", "Clases desbalanceadas", "Monitoreo de drift"]),
    ("Datos", "analista", ["SQL (CTE, ventanas)", "DuckDB", "PostgreSQL y MySQL", "pandas", "Calidad de datos"]),
    ("IA generativa", "ia", ["Claude API y tool use", "RAG híbrido", "Evaluación de LLMs", "LangChain", "Ollama"]),
]
CV_SOFTWARE = [
    ("Análisis y BI", "analista", ["R y RStudio", "Excel avanzado", "Power BI", "Tableau", "Google Sheets", "Looker Studio"]),
    ("Desarrollo", "amber", ["Python", "VS Code", "Cursor", "PyCharm", "Jupyter y Colab", "Anaconda", "Git y GitHub"]),
    ("IA y automatización", "ia", ["Claude", "ChatGPT", "Gemini", "NotebookLM", "Perplexity", "n8n", "Zapier", "Make"]),
    ("Oficina", "muted", ["Word", "PowerPoint", "Notion", "Google Workspace", "Teams", "Slack"]),
]
LEVEL = {"Nativo": 5, "Profesional (B1–B2)": 4, "Intermedio": 3, "Básico": 2}
PAPER = {"analista": "#2563C9", "cientifico": "#0B8A72", "ia": "#6A4CD1", "amber": "#C98A0B", "muted": "#5B6578"}
ROLE_NAME = {"analista": "Análisis de datos", "cientifico": "Ciencia de datos", "ia": "Ingeniería de IA"}


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
    cards = "".join(
        f'<article class="card" style="--c:{PAPER[r]}"><p class="tag">{e(ROLE_NAME[r])}</p><h3>{e(t)}</h3>'
        f'<p class="kpi"><b>{e(n)}</b><span>{e(nl)}</span></p><p class="desc">{e(d)}</p>'
        f'<p class="tools">{"".join(f"<span>{e(x)}</span>" for x in tools)}</p></article>'
        for r, t, n, nl, d, tools in CV_PROJECTS)
    def groups(rows):
        return "".join(f'<div class="grp" style="--c:{PAPER[c]}"><h4>{e(n)}</h4><p class="chips">{"".join(f"<span>{e(x)}</span>" for x in items)}</p></div>'
                       for n, c, items in rows)
    langs = "".join(
        f'<li><span class="ln">{e(l)}</span><span class="bar"><i style="width:{LEVEL.get(v, 3) * 20}%"></i></span><span class="lv">{e(v)}</span></li>'
        for l, v in LANGS)
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Hoja de vida, Juan Manuel Herrera Mejia</title>
<style>
{ff}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--ink:#101828;--text:#2B3445;--muted:#667085;--line:#E4E7EC;--soft:#F5F7FA;--navy:#0E1420;
  --blue:#2563C9;--teal:#0B8A72;--violet:#6A4CD1;--amber:#E2A72E}}
body{{font:400 9.6pt/1.6 "Public Sans",sans-serif;color:var(--text);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto;break-after:auto}}
.wrap{{padding:0 18mm}}

/* banda superior, en diálogo con la portada de LinkedIn */
.band{{background:var(--navy);color:#E8EDF5;padding:14mm 18mm 11mm;position:relative;overflow:hidden}}
.band .motif{{position:absolute;right:14mm;top:9mm;width:78mm;height:46mm;opacity:.9}}
.band .motif text{{font-family:"JBMono";font-size:7.6px}}
.band h1{{font:800 30pt/1 "Bricolage",sans-serif;letter-spacing:-.03em;color:#fff;position:relative}}
.band .role{{font:500 11.5pt/1.4 "Public Sans";color:#AEB9CC;margin-top:9px;position:relative}}
.contact{{display:flex;flex-wrap:wrap;gap:6px 22px;margin-top:15px;position:relative}}
.contact a,.contact span{{font:400 8.3pt "JBMono",monospace;color:var(--amber);text-decoration:none}}
.tri{{height:4px;background:linear-gradient(90deg,var(--blue) 0 33.33%,var(--teal) 33.33% 66.66%,var(--violet) 66.66%)}}

/* secciones con riel de títulos */
.sec{{display:grid;grid-template-columns:36mm 1fr;gap:0 8mm;padding:7.5mm 0 0}}
.sec > h2{{font:700 11pt/1.25 "Bricolage",sans-serif;color:var(--ink);padding-top:2px;border-top:2px solid var(--ink);padding-top:7px;align-self:start}}
.sec > div{{border-top:1px solid var(--line);padding-top:7px}}
.lead{{font-size:10.6pt;line-height:1.65;color:var(--ink)}}
.job + .job{{margin-top:10px;padding-top:10px;border-top:1px dashed var(--line)}}
.jh{{display:flex;justify-content:space-between;align-items:baseline;gap:10px}}
h3{{font:700 11pt/1.3 "Bricolage",sans-serif;color:var(--ink);letter-spacing:-.005em}}
.date{{font:500 8pt "JBMono",monospace;color:var(--teal);white-space:nowrap;background:#E7F4F1;padding:2px 7px;border-radius:4px}}
.org{{color:var(--muted);font-size:9pt;margin:2px 0 7px}}
ul{{padding-left:14px}} li{{margin:4px 0}} li::marker{{color:var(--teal)}}
.edu .date{{color:var(--blue);background:#E9F0FB}}
.langs{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:10px}}
.langs li{{display:flex;flex-direction:column;gap:4px;margin:0}}
.ln{{font-weight:600;color:var(--ink)}}
.bar{{height:6px;border-radius:3px;background:var(--line);overflow:hidden}}
.bar i{{display:block;height:100%;border-radius:3px;background:linear-gradient(90deg,var(--teal),var(--blue))}}
.lv{{font-size:7.5pt;color:var(--muted);line-height:1.25;white-space:nowrap}}
.foot{{position:absolute;left:18mm;right:18mm;bottom:8mm;display:flex;justify-content:space-between;font:400 7.6pt "JBMono",monospace;color:#98A2B3;border-top:1px solid var(--line);padding-top:6px}}

/* página 2 */
.mini{{display:flex;justify-content:space-between;align-items:center;padding:12mm 18mm 0}}
.mini b{{font:800 12pt "Bricolage",sans-serif;color:var(--ink)}}
.mini .tri{{width:30mm;border-radius:2px}}
.p2 h2.big{{font:800 17pt/1.1 "Bricolage",sans-serif;color:var(--ink);letter-spacing:-.02em;margin:8mm 0 2mm}}
.p2 .sub{{color:var(--muted);font-size:9.4pt;margin-bottom:4.5mm}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:4.5mm}}
.card{{background:var(--soft);border-radius:8px;padding:10px 15px 11px;border-top:3px solid var(--c);break-inside:avoid}}
.tag{{font:500 7.4pt "JBMono",monospace;color:var(--c);letter-spacing:.02em}}
.card h3{{font-size:10.6pt;margin-top:3px}}
.kpi{{display:flex;align-items:baseline;gap:7px;margin:6px 0 5px}}
.kpi b{{font:800 16pt/1 "Bricolage",sans-serif;color:var(--c);letter-spacing:-.02em;white-space:nowrap}}
.kpi span{{font-size:8.3pt;color:var(--muted);line-height:1.3}}
.desc{{font-size:8.9pt;line-height:1.55}}
.tools{{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px}}
.tools span,.chips span{{font:400 7.6pt "JBMono",monospace;background:#fff;border:1px solid var(--line);border-radius:4px;padding:1px 6px;color:var(--text)}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:6mm}}
.two h2{{font:700 11pt "Bricolage",sans-serif;color:var(--ink);border-top:2px solid var(--ink);padding-top:7px;margin-bottom:8px}}
.grp{{margin-bottom:6px}}
.grp h4{{font:600 9pt "Public Sans";color:var(--c);margin-bottom:4px}}
.chips{{display:flex;flex-wrap:wrap;gap:4px}}
.chips span{{background:var(--soft);border-color:transparent}}
</style></head><body>

<section class="page">
<header class="band">
<svg class="motif" viewBox="0 0 300 175" aria-hidden="true">
<path d="M10 150 C80 150 95 25 150 25 S220 150 290 150" fill="none" stroke="#3FBFA3" stroke-opacity=".45" stroke-width="1.6"/>
<g fill="#3FBFA3" fill-opacity=".22">{''.join(f'<rect x="{10 + i * 10}" y="{150 - h}" width="6" height="{h}"/>' for i, h in enumerate([4,7,12,20,31,46,64,82,98,110,118,118,110,98,82,64,46,31,20,12,7,4,2,1,1,1,1,1]))}</g>
<text x="170" y="40" fill="#8FA9E6" fill-opacity=".55">SELECT * FROM clientes</text>
<text x="196" y="72" fill="#E2A72E" fill-opacity=".5">&gt;&gt;&gt; import pandas</text>
<text x="10" y="18" fill="#B49CFF" fill-opacity=".5">P(A|B) = P(B|A)P(A)/P(B)</text>
</svg>
<h1>Juan Manuel<br>Herrera Mejia</h1>
<p class="role">Análisis de datos, machine learning e IA generativa</p>
<p class="contact"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="https://jmanuelhe.github.io">jmanuelhe.github.io</a><a href="{LINKEDIN}">linkedin.com/in/juanmhmejia</a><a href="{GH}">github.com/jmanuelhe</a><span>Medellín, Colombia</span></p>
</header>
<div class="tri"></div>
<div class="wrap">
<section class="sec"><h2>Perfil</h2><div><p class="lead">Estudiante de Estadística en la Universidad de Antioquia. Llevo dos años diseñando formación en IA generativa para empresas y uno como consultor independiente en análisis de datos. Me interesa que los modelos se midan en decisiones y en dinero, y construyo proyectos con código, datos y tests públicos.</p></div></section>
<section class="sec"><h2>Experiencia</h2><div>
<div class="job"><div class="jh"><h3>Consultor independiente en análisis de datos y documentación</h3><span class="date">nov. 2025 – hoy</span></div>
<p class="org">Independiente · Medellín</p>
<ul><li>Limpieza y análisis de datos en Python (pandas, SciPy) y Excel, con pruebas estadísticas y gráficos.</li>
<li>Informes y documentos corporativos en Word y Excel: estructura, diseño y consolidación de versiones.</li>
<li>Traducción y digitalización con OCR, y uso de IA para acelerar la producción con control de calidad.</li></ul></div>
<div class="job"><div class="jh"><h3>Diseñador de formación en IA para empresas</h3><span class="date">nov. 2024 – hoy</span></div>
<p class="org">Independiente · Medellín</p>
<ul><li>Diseño contenidos para que equipos técnicos y no técnicos usen IA generativa en su trabajo diario.</li>
<li>Curso completo sobre el uso de Claude en procesos de negocio: casos de uso, prompts y flujos de trabajo.</li>
<li>Materiales de presentación con un sistema de diseño profesional y revisión visual de calidad.</li>
<li>Traducción al español de guías técnicas de certificación en IA.</li></ul></div>
</div></section>
<section class="sec edu"><h2>Educación</h2><div><div class="jh"><h3>Pregrado en Estadística</h3><span class="date">2024 – 2029 (esperado)</span></div><p class="org">Universidad de Antioquia · Medellín</p></div></section>
<section class="sec"><h2>Idiomas</h2><div><ul class="langs">{langs}</ul></div></section>
</div>
<p class="foot"><span>Juan Manuel Herrera Mejia</span><span>1 / 2</span></p>
</section>

<section class="page p2">
<div class="mini"><b>Juan Manuel Herrera Mejia</b><div class="tri"></div></div>
<div class="wrap">
<h2 class="big">Proyectos</h2>
<p class="sub">Seis proyectos organizados por rol, con código, datos y tests en github.com/jmanuelhe.</p>
<div class="grid">{cards}</div>
<div class="two">
<div><h2>Habilidades</h2>{groups(CV_SKILLS)}</div>
<div><h2>Software</h2>{groups(CV_SOFTWARE)}</div>
</div>
</div>
<p class="foot"><span>jmanuelhe.github.io</span><span>2 / 2</span></p>
</section>
</body></html>"""
    src = ROOT / "assets" / "cv.html"
    src.write_text(html, encoding="utf-8")
    import asyncio
    from playwright.async_api import async_playwright

    async def run():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": 794, "height": 1123})
            await pg.goto(src.resolve().as_uri())
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(800)
            over = await pg.evaluate("""[...document.querySelectorAll('.page')].map(pg=>{const top=pg.getBoundingClientRect().top;
              const foot=pg.querySelector('.foot').getBoundingClientRect().top-top;
              const last=[...pg.querySelectorAll('.wrap > *')].pop().getBoundingClientRect().bottom-top;return [Math.round(last),Math.round(foot)]})""")
            print("contenido vs pie por página (px):", over)
            await pg.pdf(path=str(ROOT / g["CV"]), format="A4", print_background=True, prefer_css_page_size=True)
            await b.close()
    asyncio.run(run())
    src.unlink()
