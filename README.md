# Auditoría de Recorridos Terrestres - SQL & Analítica 🚚💨

Este repositorio contiene un proyecto end-to-end de ingeniería de datos y analítica predictiva enfocado en la limpieza, auditoría y optimización de bitácoras de viajes logísticos terrestres. El objetivo principal es identificar inconsistencias en los registros de rutas mediante simulación de datos en Python, almacenamiento estructurado en PostgreSQL y modelado predictivo.

---

## 📈 Metodología de Desarrollo y Estado del Proyecto

Para garantizar un desarrollo limpio, estructurado y alineado con las prácticas de la industria, el proyecto se encuentra organizado en **Sprints** incrementales. A continuación se detalla el alcance y el avance actual:

### 🔄 Sprint 1: Configuración del Entorno y Simulación Base (En Proceso)
- [x] Inicialización del repositorio local y enlace con GitHub.
- [x] Configuración del entorno virtual aislado (`.venv`) en Python 3.9.
- [x] Implementación del escudo de seguridad `.gitignore` y plantilla `.env.example`.
- [x] Creación del script en Python para simular los datos base de las bitácoras terrestres (coordenadas, tiempos, operarios).
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

---

## 📐 Diseño Preliminar de la Base de Datos (Esquema Relacional)

Para garantizar la integridad de los datos, eliminar la redundancia (3FN) y optimizar los costos de almacenamiento, el dataset plano se normaliza en un modelo relacional de cuatro tablas con tipado estricto.

### 📊 Diagrama Entidad-Relación (ERD)
```mermaid
erDiagram
    CONDUCTORES ||--o{ VIAJES : "opera"
    VEHICULOS ||--o{ VIAJES : "es_asignado_a"
    RUTAS ||--o{ VIAJES : "define"

    CONDUCTORES {
        VARCHAR(13) id_conductor PK "TIPO-NUMERO (Ej: CC-1090111000)"
        VARCHAR(100) nombre
        SMALLINT experiencia_anos "Restricción: Máximo 2 dígitos"
    }

    VEHICULOS {
        VARCHAR(6) placa PK "Estándar colombiano de 6 caracteres"
        VARCHAR(50) tipo "Van, Bus, Tractomula, etc."
        VARCHAR(20) categoria "[Carga / Pasajeros]"
        NUMERIC capacidad "Cantidad neta"
        VARCHAR(10) unidad_medida "[TON / PASAJEROS]"
    }

    RUTAS {
        VARCHAR(10) id_ruta PK "Código de ruta (Ej: R01, OP_MNT)"
        VARCHAR(100) origen
        VARCHAR(100) destino
        NUMERIC distancia_km
        NUMERIC tiempo_estimado_hrs
        VARCHAR(20) tipo_operacion "[Nacional / Local]"
    }

    VIAJES {
        VARCHAR(12) id_viaje PK "Formato V-0000000001"
        DATE fecha
        TIMESTAMP hora_salida
        TIMESTAMP hora_llegada
        VARCHAR(13) id_conductor FK
        VARCHAR(6) placa FK
        VARCHAR(10) id_ruta FK
        VARCHAR(50) clima_reportado
        NUMERIC km_real
        NUMERIC horas_viaje
        VARCHAR(50) tipo_registro "[Normal / Desvío / Anomalía]"
        TEXT observaciones_bitacora
    }