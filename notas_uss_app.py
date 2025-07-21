import streamlit as st
from datetime import datetime
from PIL import Image

# Mostrar fecha y hora actual
fecha_hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
st.markdown(f"#### 🕒 Fecha y hora actual: {fecha_hora_actual}")

# Logo USS
logo = Image.open("logo_uss.jpg")
st.image(logo, width=150)

# Título y bienvenida
st.title("Notas Universitarias - USS")
st.subheader("Creado por: ARIANA JARLEY CAMACHO GONZALES")
st.markdown("##### Puesto: 16 de 254 estudiantes")

# Ingreso de datos
dni = st.text_input("Ingrese su DNI")
nombre = st.text_input("Ingrese sus nombres y apellidos")

if dni and nombre:
    st.success(f"Bienvenida, {nombre}")

    st.markdown("---")
    st.header("📚 Notas por curso")

    # Patología
    st.subheader("Patología")
    st.write("Nota final: **15**")

    # Fisiopatología
    st.subheader("Fisiopatología")
    te1 = 15
    tef = 17
    expo = 16
    monografia = 16
    fisioprom = round((te1 * 0.35) + (tef * 0.35) + (expo * 0.15) + (monografia * 0.15), 2)
    st.write("Examen Teórico I: 15")
    st.write("Exposición: 16")
    st.write("Monografía: 16")
    st.write("Teórico Final: 17")
    st.write(f"**Promedio final: {fisioprom}**")

    # Farmacología
    st.subheader("Farmacología")
    st.write("Nota final: **16**")

    # Semiología
    st.subheader("Semiología")
    sem_te1 = 19
    sem_te2 = 16
    sem_prac1 = 18
    sem_prac2 = 16
    sem_expo = 19
    semioprom = round((sem_te1 * 0.35) + (sem_te2 * 0.35) + (sem_prac1 * 0.075) + (sem_prac2 * 0.075) + (sem_expo * 0.15), 2)
    st.write("Examen Teórico I: 19")
    st.write("Examen Práctico I: 18")
    st.write("Exposición: 19")
    st.write("Examen Teórico II: 16")
    st.write("Examen Práctico II: 16")
    st.write(f"**Promedio final: {semioprom}**")

    # Electivo I
    st.subheader("Electivo I")
    st.write("Nota final: **18**")

    # Promedio general
    notas = [15, fisioprom, 16, semioprom, 18]
    promedio_general = round(sum(notas) / len(notas), 2)
    st.markdown("---")
    st.header(f"📊 Promedio General: **{promedio_general}**")

    if promedio_general >= 14:
        st.success("✅ APROBADO")
    else:
        st.error("❌ DESAPROBADO")
