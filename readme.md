# Analizador de Rendimiento Web y SEO

## 🚀 Descripción

Este proyecto es una herramienta automatizada que utiliza la API de Google PageSpeed Insights y técnicas de SEO para analizar y generar reportes detallados sobre el rendimiento de sitios web. Está diseñado específicamente para analizar múltiples sitios web relacionados con palabras clave específicas en el mercado panameño.

## 🛠️ Características Principales

- Análisis automatizado de rendimiento web usando Google PageSpeed Insights
- Búsqueda y análisis de los top 10 resultados por palabra clave
- Generación automática de reportes en formato Markdown
- Exclusión inteligente de dominios de redes sociales
- Análisis de rendimiento móvil
- Sistema de agentes inteligentes para automatizar el proceso

## 📋 Requisitos Previos

- Python 3.10 o superior
- API Key de Google PageSpeed Insights
- API Key de Serper.dev
- API Key de OpenAI

## 🔧 Configuración

1. Clonar el repositorio
2. Instalar las dependencias:

```bash
pip install crewai crewai-tools requests
```

3. Configurar las variables de entorno en `crew.py`:

```python
os.environ["OPENAI_API_KEY"] = "tu-api-key"
os.environ["SERPER_API_KEY"] = "tu-api-key-serper"
```

## 🤖 Agentes del Sistema

El proyecto utiliza tres agentes principales:

1. **Investigador (Researcher)**

   - Identifica y limpia las URLs de los top 10 enlaces por palabra clave
   - Excluye dominios de redes sociales

2. **Analizador (Analyzer)**

   - Analiza el rendimiento de los sitios web encontrados
   - Utiliza Google API SpeedTest para evaluación

3. **Reportero (Reporter)**
   - Compila reportes de rendimiento detallados
   - Genera archivos Markdown con los resultados

## 📊 Estructura de los Reportes

Los reportes generados incluyen:

- URL del sitio web
- Puntuación de rendimiento (0-100%)
- Formato ordenado y legible
- Guardado automático en archivos Markdown

## 🚀 Uso

Para ejecutar un análisis:

```python
from crew import crew

keywords = ["tu palabra clave"]
result = crew.kickoff(inputs={'keywords': keywords})
print(result)
```

## 📁 Estructura del Proyecto

```
├── crew.py                 # Configuración principal y lógica de agentes
├── GoogleApiSpeedTest.py   # Herramienta de análisis de velocidad
├── SaveMD.py              # Herramienta para guardar reportes
└── performance reports/    # Directorio de reportes generados
```

## 📈 Ejemplo de Reporte

```markdown
1 - ejemplo.com : Performance Score - 85%
2 - ejemplo2.com : Performance Score - 92%
...
```

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, asegúrate de:

1. Hacer fork del proyecto
2. Crear una rama para tu feature
3. Hacer commit de tus cambios
4. Crear un Pull Request

## 📝 Notas

- Las puntuaciones de rendimiento son basadas en la versión móvil de los sitios
- Los reportes se generan automáticamente en la carpeta 'performance reports'
- Se recomienda no ejecutar demasiadas consultas simultáneas para evitar límites de API
