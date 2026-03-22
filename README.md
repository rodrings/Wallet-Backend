Descripción General
Este proyecto consiste en una interfaz de programación de aplicaciones (API) robusta diseñada para la gestión de finanzas personales. Implementa un motor de cálculo de rendimientos variables en tiempo real, permitiendo la administración de activos líquidos e inversiones de renta fija a través de una arquitectura orientada a servicios.

Arquitectura y Principios de Diseño
El sistema ha sido desarrollado bajo principios de modularidad y escalabilidad, utilizando las siguientes estrategias de ingeniería:

Arquitectura de Capas (Routers): Segregación de responsabilidades mediante el uso de APIRouter, dividiendo la lógica de negocio en módulos de Inversiones, Transacciones y Estado de Cuenta (Wallet).

Modelado de Datos con Pydantic: Implementación de esquemas de validación estrictos para garantizar la integridad de los datos de entrada y salida, asegurando que cada transacción cumpla con los tipos de datos requeridos.

Normalización de Transacciones: Aplicación de un modelo unificado de Transaccion que consolida diversos orígenes de datos (Depósitos, Gastos, Liquidaciones) en un registro histórico coherente.

Gestión de Estado en Memoria: Uso de un repositorio de datos centralizado para la persistencia volátil durante el ciclo de vida de la aplicación.

Especificaciones Técnicas
1. Motor de Rendimientos (Real-Time Accrual)
A diferencia de sistemas estáticos, esta API calcula los intereses acumulados de forma dinámica. Utiliza la diferencia de marcas temporales (timestamps) para determinar el rendimiento exacto al segundo, aplicando la fórmula de interés simple sobre el capital expuesto.

2. Control de Flujo de Fondos
El sistema implementa validaciones de lógica financiera:

Verificación de Solvencia: Los gastos e inversiones están sujetos a la disponibilidad de saldo en el balance.

Ciclo de Inversión: Proceso completo desde la detracción del balance principal, la generación de intereses, hasta la liquidación y retorno del capital con su respectiva utilidad.

Documentación de Endpoints
Gestión de Estado
GET /wallet: Retorna un objeto complejo que consolida el balance disponible, capital invertido, intereses devengados acumulados y el historial de transacciones reciente.

GET /history: Punto de acceso al registro histórico con soporte para parámetros de consulta (query parameters) que permiten filtrar por tipo de operación (deposit, expense, investment).

Operaciones Financieras
POST /deposit: Registra el ingreso de capital al sistema desde un origen externo.

POST /expense: Ejecuta la salida de fondos, requiriendo una descripción de la transacción.

POST /investment/invest: Inicia un nuevo activo de inversión, asignando un identificador único y una tasa de rendimiento específica.

POST /investment/close/{id}: Realiza el cierre técnico de una inversión. Calcula el monto final (capital + intereses) y reintegra los fondos al balance de libre disponibilidad.

Requisitos e Instalación
Requisitos del Sistema
Python 3.10 o superior.

Entorno de ejecución para FastAPI (Uvicorn).

Instalación
Clonar el repositorio.

Instalar las dependencias core:

Bash
pip install fastapi uvicorn pydantic
Iniciar el servicio:

Bash
uvicorn main:app --host 0.0.0.0 --port 8000
