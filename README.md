# 🎬 Fake Cinema Automation

Automatización de pruebas para una app de cine, usando arquitectura POM, Selenium, Pytest y BDD con Gherkin. Proyecto desarrollado durante un bootcamp técnico.

---

## 📖 Descripción del proyecto

Este repositorio contiene un framework de automatización para validar el flujo completo de selección de alimentos en una aplicación de cine. El enfoque se basa en buenas prácticas de QA como:

- Uso de Page Object Model (POM) para mantener una arquitectura modular y escalable.
- Integración de `pytest` con fixtures para controlar el ciclo de vida de los tests.
- Validaciones robustas con `asserts` y `waits` explícitos para entornos dinámicos.
- Parametrización de pruebas para evitar duplicidad y mejorar la cobertura.
- Reportes visuales y trazabilidad para asegurar transparencia en los resultados.

El objetivo es simular la experiencia de usuario en la selección de alimentos, validando cada paso del flujo con precisión técnica y enfoque DRY.

---

## 📦 Requisitos

Antes de ejecutar los tests, asegúrate de tener instalado:

- Python 3.13
- Google Chrome (última versión)
- ChromeDriver compatible con tu versión de Chrome
- pip (gestor de paquetes de Python)

---

## ⚙️ Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/valenzzaira/Fake-cinema-automation.git

   Fake-cinema-automation/
├── pages/               # Clases POM con métodos reutilizables por página
│   ├── base_page.py     # Métodos comunes (click, input, waits, asserts)
│   └── food_page.py     # Acciones específicas de la selección de alimentos
│
├── tests/               # Casos de prueba automatizados
│   ├── test_food_flow.py  # Validación completa del flujo de alimentos
│   └── conftest.py        # Fixtures globales para setup/teardown
│
├── features/            # Archivos .feature para pruebas BDD (si aplica)
│   └── food_selection.feature
│
├── requirements.txt     # Lista de dependencias
└── README.md            # Documentación del proyecto
   
