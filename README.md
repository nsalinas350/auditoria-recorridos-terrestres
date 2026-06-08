# Auditoría de Recorridos Terrestres - SQL & Analítica 🚚💨

Este repositorio contiene un proyecto end-to-end de ingeniería de datos y analítica predictiva enfocado en la limpieza, auditoría y optimización de bitácoras de viajes logísticos terrestres. El objetivo principal es identificar inconsistencias en los registros de rutas mediante simulación de datos en Python, almacenamiento estructurado en PostgreSQL y modelado predictivo.

---

## 📈 Metodología de Desarrollo y Estado del Proyecto

Para garantizar un desarrollo limpio, estructurado y alineado con las prácticas de la industria, el proyecto se encuentra organizado en **Sprints** incrementales. A continuación se detalla el alcance y el avance actual:

### 🔄 Sprint 1: Configuración del Entorno y Simulación Base (En Proceso)
- [x] Inicialización del repositorio local y enlace con GitHub.
- [x] Configuración del entorno virtual aislado (`.venv`) en Python 3.9.
- [x] Implementación del escudo de seguridad `.gitignore` y plantilla `.env.example`.
- [ ] Creación del script en Python para simular los datos base de las bitácoras terrestres (coordenadas, tiempos, operarios).
- [ ] Diseño preliminar del esquema de base de datos en PostgreSQL.

### ⏳ Sprint 2: Ingesta, Conexión y Modelado SQL (Próximamente)
- [ ] Configuración del contenedor o base de datos local en PostgreSQL.
- [ ] Creación de scripts de migración (`DDL`) utilizando Python (con `psycopg2` o `SQLAlchemy`).
- [ ] Diseño de consultas avanzadas y auditorías de integridad mediante SQL.

### ⏳ Sprint 3: Análisis Exploratorio de Datos (EDA) y Limpieza (Próximamente)
- [ ] Conexión del entorno con Jupyter Notebooks en la carpeta `notebooks/`.
- [ ] Análisis exploratorio con `Pandas`, `Matplotlib` y `Seaborn`.
- [ ] Detección automatizada de anomalías en tiempos de recorrido y paradas no autorizadas.

### ⏳ Sprint 4: Modelado Predictivo / Optimización (Próximamente)
- [ ] Implementación de algoritmos de clustering o regresión para predecir tiempos estimados de arribo (ETA).
- [ ] Evaluación técnica de métricas del modelo.

---

## 🛠️ Tecnologías y Herramientas Utilizadas
- **Lenguaje Principal:** Python 3.9
- **Base de Datos:** PostgreSQL
- **Control de Versiones:** Git & GitHub
- **Librerías Clave:** Pandas, NumPy, (Próximamente: Scikit-learn, Psycopg2)