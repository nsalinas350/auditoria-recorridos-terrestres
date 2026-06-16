import random
from datetime import datetime, timedelta

###############################
########## SECCIÓN 1 ##########
###############################
# 1. DATOS MAESTROS PARA LA SIMULACIÓN
CONDUCTORES = [
    {"id_conductor": "CC-1017234001", "nombre": "Carlos Mario Jaramillo", "experiencia_anos": 8},
    {"id_conductor": "CC-1037654002", "nombre": "Juan Fernando Hoyos", "experiencia_anos": 12},
    {"id_conductor": "CC-1152431003", "nombre": "Andrés Felipe Restrepo", "experiencia_anos": 4},
    {"id_conductor": "CC-1017987004", "nombre": "Santiago Alarcón", "experiencia_anos": 15},
    {"id_conductor": "CC-1033456005", "nombre": "Mateo Bermúdez", "experiencia_anos": 2},
    {"id_conductor": "CC-1128475006", "nombre": "Luis Alberto Posada", "experiencia_anos": 10},
    {"id_conductor": "CC-1045321007", "nombre": "Diana Carolina Vélez", "experiencia_anos": 6}
]

VEHICULOS = [
    # Carga (Segmentado por Toneladas)
    {"placa": "TRB789", "tipo": "Camioneta", "categoria": "Carga", "capacidad": "1.5 Ton"},
    {"placa": "SNC456", "tipo": "Camión Sencillo", "categoria": "Carga", "capacidad": "8 Ton"},
    {"placa": "KML654", "tipo": "Camión Doble Troque", "categoria": "Carga", "capacidad": "16 Ton"},
    {"placa": "TRK123", "tipo": "Tractomula", "categoria": "Carga", "capacidad": "35 Ton"},
    
    # Pasajeros (Segmentado por capacidad)
    {"placa": "VAN015", "tipo": "Van", "categoria": "Pasajeros", "capacidad": "15 Pasajeros"},
    {"placa": "VAN018", "tipo": "Van", "categoria": "Pasajeros", "capacidad": "18 Pasajeros"},
    {"placa": "BUS040", "tipo": "Bus Intermunicipal", "categoria": "Pasajeros", "capacidad": "40 Pasajeros"},
    {"placa": "BUS054", "tipo": "Bus Imperial", "categoria": "Pasajeros", "capacidad": "54 Pasajeros"}
]

# Rutas reales saliendo desde Medellín
RUTAS = [
    # --- VIAJES COMERCIALES NACIONALES ---
    {"id_ruta": "R01", "origen": "Medellín", "destino": "Bogotá", "distancia_km": 415, "tiempo_estimado_hrs": 9, "tipo_operacion": "Nacional"},
    {"id_ruta": "R02", "origen": "Medellín", "destino": "Cali", "distancia_km": 420, "tiempo_estimado_hrs": 9.5, "tipo_operacion": "Nacional"},
    {"id_ruta": "R03", "origen": "Medellín", "destino": "Barranquilla", "distancia_km": 710, "tiempo_estimado_hrs": 15, "tipo_operacion": "Nacional"},
    {"id_ruta": "R04", "origen": "Medellín", "destino": "Apartadó", "distancia_km": 310, "tiempo_estimado_hrs": 7.5, "tipo_operacion": "Nacional"},
    {"id_ruta": "R05", "origen": "Medellín", "destino": "Pereira", "distancia_km": 220, "tiempo_estimado_hrs": 5, "tipo_operacion": "Nacional"},
    
    # --- MOVIMIENTOS OPERATIVOS LOCALES ---
    {"id_ruta": "OP_MNT", "origen": "Base Medellín", "destino": "Taller", "distancia_km": 12, "tiempo_estimado_hrs": 1.5, "tipo_operacion": "Local"},
    {"id_ruta": "OP_LVD", "origen": "Base Medellín", "destino": "Lavadero", "distancia_km": 5, "tiempo_estimado_hrs": 1.0, "tipo_operacion": "Local"},
    {"id_ruta": "OP_TNQ", "origen": "Base Medellín", "destino": "Tanqueo", "distancia_km": 3, "tiempo_estimado_hrs": 0.5, "tipo_operacion": "Local"},
    {"id_ruta": "OP_LLN", "origen": "Base Medellín", "destino": "Montallantas", "distancia_km": 8, "tiempo_estimado_hrs": 1.2, "tipo_operacion": "Local"}
]

CLIMAS = ["Despejado", "Lluvia Ligera", "Tormenta", "Niebla"]

###############################
########## SECCIÓN 2 ##########
###############################
# 2. FUNCIÓN GENERADORA DE RECORRIDOS

def simular_viaje(id_viaje, fecha_base):
    conductor = random.choice(CONDUCTORES)
    vehiculo = random.choice(VEHICULOS)
    ruta = random.choice(RUTAS)
    clima = random.choice(CLIMAS)
    
    origen = ruta["origen"]
    destino = ruta["destino"]
    distancia_teorica = ruta["distancia_km"]
    tiempo_teorico = ruta["tiempo_estimado_hrs"]
    tipo_operacion = ruta["tipo_operacion"]
    
    # 1. Comportamiento base según el tipo de operación
    if tipo_operacion == "Local":
        # Movimientos locales tienen variaciones por tráfico urbano pesado de Medellín
        variacion_km = random.uniform(0.90, 1.10) # Variación normal urbana (cambio de ruta en ciudad)
        distancia_real = distancia_teorica * variacion_km
        
        variacion_tiempo = random.uniform(0.85, 1.50) # El tráfico de ciudad es muy variable
        tiempo_real = tiempo_teorico * variacion_tiempo
        tipo_registro = "Operación Local"
        observaciones = f"Movimiento operativo registrado: {destino}."
    else:
        # Comportamiento Nacional Base (Afectado por clima)
        factor_clima = 1.0
        if clima == "Lluvia Ligera": factor_clima = 1.15
        elif clima == "Tormenta": factor_clima = 1.35
        elif clima == "Niebla": factor_clima = 1.25
        
        variacion_normal = random.uniform(0.9, 1.15)
        tiempo_real = tiempo_teorico * factor_clima * variacion_normal
        distancia_real = distancia_teorica * random.uniform(0.98, 1.02)
        tipo_registro = "Normal"
        observaciones = "Viaje comercial completado sin novedades."

    # -------------------------------------------------------------------------
    # 🚨 INYECCIÓN DE ANOMALÍAS (Probabilidad del 15%)
    # -------------------------------------------------------------------------
    disparador_anomalia = random.random()
    
    if disparador_anomalia < 0.15:
        # Si es una operación LOCAL, sus anomalías son distintas a las nacionales
        if tipo_operacion == "Local":
            tipo_anomalia_local = random.choice(["Km Atípico Urbano", "Tiempo Excesivo"])
            
            if tipo_anomalia_local == "Km Atípico Urbano":
                tipo_registro = "Anomalía Local - Kilometraje"
                # Multiplicamos el km por 3 o 4 (Se fue a otra sede lejana por falta de cupo/repuestos)
                distancia_real = distancia_teorica * random.uniform(3.0, 5.0)
                tiempo_real = tiempo_real * random.uniform(2.0, 3.0)
                observaciones = f"Kilometraje atípico en {ruta['id_ruta']}: Desvío a sede alterna por alta congestión o falta de insumos."
                
            elif tipo_anomalia_local == "Tiempo Excesivo":
                tipo_registro = "Anomalía Local - Tiempo"
                # El kilometraje es normal, pero se quedó varado o esperando horas extras
                tiempo_real = tiempo_real * random.uniform(4.0, 8.0)
                observaciones = f"Tiempos muertos detectados en {destino}. Retraso en fila de espera o entrega de repuestos."
        
        # Si es una operación NACIONAL, aplicamos tus otras anomalías de carretera
        else:
            tipo_anomalia_nac = random.choice([1, 2, 3])
            
            # Caso 1: Nombres de lugares mal estandarizados (Ej: "Medellin", "Bogota D.C.", "b/quilla")
            if tipo_anomalia_nac == 1:
                tipo_registro = "Error Estandarización"
                origen = random.choice(["Medellin", "MEDELLIN", "MDE", "MEDELIN"]) if origen == "Medellín" else origen
                destino = random.choice(["Bogota D.C.", "BOGOTA", "bogota", "BOG"]) if destino == "Bogotá" else destino
                destino = random.choice(["b/quilla", "bquilla", "baranquilla", "BAQ"]) if destino == "Barranquilla" else destino
                observaciones = "Registro ingresado por app móvil desactualizada."
                
            elif tipo_anomalia_nac == 2:
                tipo_registro = "Ruta Vacía"
                origen = None
                destino = None
                observaciones = "Error de sincronización GPS durante el despacho."
                
            elif tipo_anomalia_nac == 3: # Tu caso 4: Desvíos nacionales por derrumbes
                tipo_registro = "Desvío Operacional"
                factor_desvio = random.uniform(1.25, 1.60)
                distancia_real = distancia_teorica * factor_desvio
                tiempo_real = tiempo_real * factor_desvio * random.uniform(1.1, 1.3)
                observaciones = "Desvío en vía principal reportado por INVÍAS (Derrumbe/Arreglos de calzada)."

    # 2. Calcular marcas de tiempo (timestamps)
    hora_salida = fecha_base + timedelta(hours=random.uniform(4, 22), minutes=random.uniform(0, 59))
    hora_llegada = hora_salida + timedelta(hours=tiempo_real)
    
    return {
        "id_viaje": f"V-{id_viaje:010d}",
        "fecha": hora_salida.strftime("%Y-%m-%d"),
        "hora_salida": hora_salida.strftime("%Y-%m-%d %H:%M:%S"),
        "hora_llegada": hora_llegada.strftime("%Y-%m-%d %H:%M:%S"),
        "id_conductor": conductor["id_conductor"],
        "nombre_conductor": conductor["nombre"],
        "placa": vehiculo["placa"],
        "tipo_vehiculo": vehiculo["tipo"],
        "categoria_vehiculo": vehiculo["categoria"],
        "capacidad_vehiculo": vehiculo["capacidad"],
        "id_ruta": ruta["id_ruta"],
        "tipo_operacion": tipo_operacion,
        "origen_registrado": origen,
        "destino_registrado": destino,
        "clima_reportado": clima,
        "km_teorico": distancia_teorica,
        "km_real": round(distancia_real, 2),
        "horas_viaje": round(tiempo_real, 2),
        "tipo_registro": tipo_registro,
        "observaciones_bitacora": observaciones
    }


###############################
########## SECCIÓN 3 ##########
###############################
# 2. FUNCIÓN QUE SIMULA EL DATASET
import csv
import os

def generar_dataset(total_viajes=2500):
    print(f"🚀 Iniciando simulación de {total_viajes} registros de viajes...")
    
    # Asegurar que la carpeta 'data' exista
    os.makedirs("data", exist_ok=True)
    ruta_csv = "data/bitacora_viajes.csv"
    
    # Fecha de inicio para la simulación (hacia atrás desde hoy)
    fecha_inicio = datetime.now() - timedelta(days=180)
    
    viajes_simulados = []
    
    for i in range(1, total_viajes + 1):
        # Distribuir los viajes a lo largo de los últimos 6 meses
        fecha_viaje = fecha_inicio + timedelta(days=random.randint(0, 180))
        viaje = simular_viaje(i, fecha_viaje)
        viajes_simulados.append(viaje)
    
    # Obtener los nombres de las columnas (las llaves del diccionario)
    columnas = viajes_simulados[0].keys()
    
    # Escribir los datos en el archivo CSV
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(viajes_simulados)
        
    print(f"✨ ¡Dataset generado con éxito! Archivo guardado en: {ruta_csv}")

# Este bloque asegura que el script se ejecute si lo llamas desde la terminal
if __name__ == "__main__":
    # Generamos 2,500 viajes para tener un volumen robusto para SQL
    generar_dataset(total_viajes=2500)