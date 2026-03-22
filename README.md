# Wallet Backend API

Backend de una billetera virtual desarrollado con FastAPI, orientado a simular el funcionamiento de una aplicación financiera. Permite gestionar depósitos, gastos e inversiones mediante una API REST estructurada, aplicando buenas prácticas de desarrollo backend como separación de modelos, validación de datos y arquitectura modular.

---

## Descripción

Este proyecto implementa una API backend para una billetera digital donde los usuarios pueden administrar su dinero de forma simple:

* Depositar fondos
* Registrar gastos
* Crear inversiones
* Consultar el estado actual de la billetera

El sistema está diseñado siguiendo principios comunes en el desarrollo de APIs modernas, separando los datos de entrada de aquellos generados por el sistema, como identificadores y marcas de tiempo.

---

## Objetivo

El objetivo del proyecto es aplicar conceptos fundamentales de desarrollo backend:

* Diseño de APIs REST
* Modelado de datos
* Separación de responsabilidades
* Validación automática de datos
* Simulación de lógica de negocio financiera

---

## Tecnologías utilizadas

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## Estructura del proyecto

```id="x0t6dc"
app/
│
├── main.py
├── models.py
├── data.py
│
└── routers/
    ├── wallet.py
    ├── expenses.py
    └── investments.py
```

La aplicación está organizada de forma modular, separando rutas, modelos y lógica de datos para facilitar el mantenimiento y la escalabilidad.

---

## Instalación y ejecución

1. Clonar el repositorio:

```id="q76vsl"
git clone https://github.com/rodrings/Wallet-Backend.git
cd Wallet-Backend
```

2. Crear entorno virtual:

```id="r9ccfo"
python -m venv venv
.\venv\Scripts\activate
```

3. Instalar dependencias:

```id="k1b8bg"
pip install fastapi uvicorn
```

4. Ejecutar el servidor:

```id="n7o9fx"
uvicorn main:app --reload
```

---

## Endpoints principales

### Wallet

* `GET /wallet`
  Obtiene el estado actual de la billetera.

---

### Depósitos

* `POST /deposit`

```json id="qrcw6o"
{
  "amount": 100,
  "origin": "salary"
}
```

---

### Gastos

* `POST /expense`

```json id="t0ue19"
{
  "amount": 50,
  "description": "food"
}
```

---

### Inversiones

* `POST /invest`

```json id="8dqsyg"
{
  "amount": 200,
  "rate": 0.05
}
```

---

## Ejemplo de respuesta

```json id="y6zh3f"
{
  "balance": 850,
  "investments": [
    {
      "id": 1,
      "amount": 200,
      "rate": 0.05,
      "start": "2026-03-17T18:22:10"
    }
  ]
}
```

---

## Testing

La API puede probarse mediante:

* Documentación interactiva (Swagger):
  http://127.0.0.1:8000/docs

* Thunder Client dentro de Visual Studio Code

---

## Conclusión

Este proyecto constituye una base sólida para el desarrollo de un backend de tipo financiero, incorporando prácticas utilizadas en entornos profesionales y permitiendo su extensión hacia sistemas más complejos.

---

## Autor

Rodrigo García Solá
