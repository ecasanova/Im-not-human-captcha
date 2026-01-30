# Im-not-human-captcha

Un sistema de CAPTCHA que **solo** puede ser resuelto por agentes automatizados (bots, scripts) y **no** por humanos. Este proyecto invierte el concepto tradicional de CAPTCHA al crear desafíos que son triviales para las máquinas pero complicados para los humanos.

## 🎯 Propósito

El objetivo de este proyecto es demostrar un concepto invertido de CAPTCHA, donde:
- Los agentes automatizados pueden resolver los desafíos fácilmente
- Los humanos encuentran difícil resolver los desafíos manualmente
- Se protegen recursos destinados exclusivamente para automatización

## 🚀 Características

Este sistema implementa dos tipos de desafíos:

### 1. Texto Codificado en Base64
Genera texto codificado en base64 que debe ser decodificado.

**Ejemplo:**
- **Desafío**: `Decode this base64 text: U29sb1BhcmFBZ2VudGVz`
- **Respuesta correcta**: `SoloParaAgentes`

### 2. Secuencias Numéricas Geométricas
Presenta secuencias numéricas basadas en patrones geométricos.

**Ejemplo:**
- **Desafío**: `What is the next number in this sequence: 3, 9, 27, ?`
- **Respuesta correcta**: `81` (secuencia geométrica con razón 3)

## 📦 Instalación

No requiere dependencias externas, solo Python 3.6 o superior.

```bash
git clone https://github.com/ecasanova/Im-not-human-captcha.git
cd Im-not-human-captcha
```

## 💻 Uso

### Uso Básico

```python
from captcha import generate_captcha, validate_captcha

# Generar un desafío CAPTCHA
challenge = generate_captcha()

print(f"Tipo: {challenge['type']}")
print(f"Desafío: {challenge['challenge']}")

# El agente automatizado resuelve el desafío
# Para base64: decodificar el texto
# Para secuencia: calcular el siguiente número

# Validar la respuesta
response = challenge['answer']  # Respuesta del agente
is_valid = validate_captcha(challenge, response)

print(f"¿Respuesta válida? {is_valid}")
```

### Ejemplo Completo con Base64

```python
from captcha import generate_captcha, validate_captcha
import base64

# Generar desafío
challenge = generate_captcha()

if challenge['type'] == 'base64':
    # Extraer el texto codificado del desafío
    encoded_text = challenge['challenge'].split(': ')[1]
    
    # Decodificar
    decoded = base64.b64decode(encoded_text).decode()
    
    # Validar
    if validate_captcha(challenge, decoded):
        print("✓ CAPTCHA resuelto correctamente")
    else:
        print("✗ Respuesta incorrecta")
```

### Ejemplo Completo con Secuencia

```python
from captcha import generate_captcha, validate_captcha

challenge = generate_captcha()

if challenge['type'] == 'sequence':
    # Extraer los números de la secuencia
    sequence_part = challenge['challenge'].split(': ')[1]
    numbers = [int(x.strip()) for x in sequence_part.split(',') if x.strip() != '?']
    
    # Detectar el patrón (razón geométrica)
    ratio = numbers[1] // numbers[0]
    next_number = numbers[-1] * ratio
    
    # Validar
    if validate_captcha(challenge, str(next_number)):
        print("✓ CAPTCHA resuelto correctamente")
    else:
        print("✗ Respuesta incorrecta")
```

## 🧪 Pruebas

El proyecto incluye pruebas unitarias completas:

```bash
python -m unittest test_captcha -v
```

Las pruebas cubren:
- Generación correcta de desafíos
- Validación de respuestas correctas e incorrectas
- Manejo de espacios en blanco
- Casos específicos documentados
- Validación de formato de datos

## 📁 Estructura del Proyecto

```
Im-not-human-captcha/
├── captcha.py          # Lógica principal del sistema CAPTCHA
├── test_captcha.py     # Pruebas unitarias
└── README.md           # Este archivo
```

## 🔧 API

### `generate_captcha()`

Genera un desafío CAPTCHA aleatorio.

**Retorna:**
- `dict` con las siguientes claves:
  - `type` (str): Tipo de desafío ('base64' o 'sequence')
  - `challenge` (str): El texto del desafío
  - `answer` (str): La respuesta correcta

### `validate_captcha(challenge, response)`

Valida la respuesta de un desafío.

**Parámetros:**
- `challenge` (dict): El diccionario retornado por `generate_captcha()`
- `response` (str): La respuesta del usuario/agente

**Retorna:**
- `bool`: `True` si la respuesta es correcta, `False` en caso contrario

## 🔮 Extensiones Futuras

Este diseño puede extenderse para incorporar:
- Operaciones matemáticas complejas (factoriales, fibonacci, etc.)
- Conversión entre sistemas numéricos (binario, hexadecimal)
- Expresiones regulares complejas
- Cálculos hash (MD5, SHA)
- Operaciones con fechas y timestamps
- Parsing de JSON/XML

## 📝 Licencia

Este proyecto está disponible como código abierto para fines educativos y de demostración.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## ⚠️ Nota

Este proyecto es un concepto educativo y de demostración. No se recomienda usar en producción sin las debidas consideraciones de seguridad y casos de uso apropiados.
