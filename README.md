# 🎬 Fake Cinema Automation

![Tests](https://github.com/valenzzaira/Fake-cinema-automation/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.15-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-7.4-orange.svg)

Proyecto de automatización de pruebas End-to-End para el sistema de compra de boletos y alimentos de [Fake Cinema](https://fake-cinema.vercel.app/).

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Test Cases](#-test-cases)
- [CI/CD](#-cicd)
- [Contribuir](#-contribuir)
- [Autor](#-autor)

---

## 📖 Descripción

Este proyecto automatiza las pruebas de funcionalidad del sitio web **Fake Cinema**, cubriendo flujos completos de:

- 🎟️ Compra de boletos de cine
- 🍿 Compra de alimentos (palomitas, sandwich, bebidas)
- 💳 Proceso de checkout y pago
- ✅ Validaciones de formularios

Utiliza **Selenium WebDriver** con **Python** y el patrón de diseño **Page Object Model (POM)** para mantener un código limpio, mantenible y escalable.

---

## ✨ Características

- ✅ Tests End-to-End automatizados
- ✅ Patrón Page Object Model (POM)
- ✅ Ejecución en modo headless para CI/CD
- ✅ Reportes HTML con pytest-html
- ✅ Integración con GitHub Actions
- ✅ Screenshots automáticos en caso de fallo
- ✅ Fixtures parametrizados con pytest
- ✅ Data-driven testing

---

## 🛠️ Tecnologías

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.13 | Lenguaje principal |
| Selenium | 4.15.2 | Automatización del navegador |
| Pytest | 7.4.3 | Framework de testing |
| WebDriver Manager | 4.0.1 | Gestión de drivers |
| pytest-html | 4.1.1 | Generación de reportes |

---

## 📦 Instalación

### Prerrequisitos

- Python 3.13+
- Google Chrome (última versión)
- Git

### Pasos

**1. Clona el repositorio**

```bash
git clone https://github.com/valenzzaira/Fake-cinema-automation.git
cd Fake-cinema-automation
```

**2. Crea un entorno virtual** (opcional pero recomendado)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instala las dependencias**

```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

### Ejecutar todos los tests

```bash
pytest
```

### Ejecutar tests con reporte HTML

```bash
pytest --html=reports/report.html --self-contained-html
```

### Ejecutar tests específicos

```bash
# Un archivo específico
pytest tests/test_food_purchase.py

# Un test específico
pytest tests/test_food_purchase.py::test_flujo_completo

# Por marca (si las tienes)
pytest -m smoke
```

### Ejecutar en modo headless

```bash
# Linux/Mac
HEADLESS=true pytest

# Windows
set HEADLESS=true && pytest
```

### Ver reporte

Después de ejecutar los tests, abre el archivo:
```
reports/report.html
```

---

## 📁 Estructura del Proyecto

```
Fake-cinema-automation/
├── .github/
│   └── workflows/
│       └── tests.yml          # Configuración de GitHub Actions
├── pages/                      # Page Objects
│   ├── base_page.py           # Clase base con métodos comunes
│   ├── home_page.py           # Página principal
│   ├── food_pages.py          # Página de alimentos
│   ├── food_details.py        # Detalles del producto
│   ├── cart_pages.py          # Carrito de compras
│   └── checkout_page.py       # Página de checkout
├── tests/                      # Tests automatizados
│   ├── test_food_purchase.py  # Tests de compra de alimentos
│   └── test_customer_data.py  # Tests de formulario
├── reports/                    # Reportes generados (git ignored)
├── conftest.py                # Configuración de fixtures
├── requirements.txt           # Dependencias del proyecto
├── .gitignore
└── README.md
```

---

## 🧪 Test Cases

El proyecto incluye los siguientes tipos de tests:

### Tests Funcionales
- ✅ Agregar productos al carrito
- ✅ Eliminar productos del carrito
- ✅ Actualizar cantidades
- ✅ Proceso de checkout completo
- ✅ Validación de formularios

### Tests Negativos
- ❌ Email inválido
- ❌ Campos obligatorios vacíos
- ❌ Tarjeta inválida
- ❌ CVV inválido

### Tests E2E
- 🎯 Flujo completo de compra de alimentos
- 🎯 Flujo completo de compra de boletos

📊 **Documentación completa de Test Cases:** [Ver en Google Sheets](https://docs.google.com/spreadsheets/d/11_UKXfdTq8x_Z2P--q5lnym-Kn-XmGmykmqQL19PKiM/edit?usp=sharing)

---

## 🔄 CI/CD

Este proyecto utiliza **GitHub Actions** para ejecutar los tests automáticamente en cada push y pull request.

### Workflow

```
✓ Checkout del código
✓ Instalación de Python 3.13
✓ Instalación de Chrome
✓ Instalación de dependencias
✓ Ejecución de tests
✓ Generación de reportes
✓ Upload de artifacts
```

### Ver resultados

Los resultados de los tests están disponibles en la pestaña **Actions** del repositorio:

🔗 [Ver GitHub Actions](https://github.com/valenzzaira/Fake-cinema-automation/actions)

### Descargar reportes

Después de cada ejecución, puedes descargar:
- 📄 Reporte HTML de tests

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: nueva característica'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Convenciones

- Seguir el patrón Page Object Model
- Escribir tests descriptivos
- Incluir docstrings en funciones
- Mantener el código limpio y documentado

---

## 📝 Notas

- Los tests se ejecutan en modo **headless** en CI/CD
- Localmente se ejecutan con interfaz gráfica por defecto
- Los reportes HTML se generan automáticamente
- Screenshots se capturan solo cuando hay fallos

---

## 👨‍💻 Autor

**Zaira Valenzuela**

- GitHub: [@valenzzaira](https://github.com/valenzzaira)
- Proyecto: [Fake Cinema Automation](https://github.com/valenzzaira/Fake-cinema-automation)

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la [MIT License](LICENSE).

---

<div align="center">

⭐ **Si este proyecto te fue útil, considera darle una estrella en GitHub!** ⭐

🎬 **URL del sitio bajo prueba:** [https://fake-cinema.vercel.app/](https://fake-cinema.vercel.app/)

</div>


   
