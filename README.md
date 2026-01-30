# I'm Not Human CAPTCHA

A reverse CAPTCHA system designed to be solved by automated agents but difficult for humans. This project inverts the traditional CAPTCHA concept by creating challenges that are trivial for machines but complicated for humans.

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
- **Texto original:** `SoloParaAgentes`
- **Desafío (codificado):** `U29sb1BhcmFBZ2VudGVz`
- **Respuesta esperada:** `SoloParaAgentes`

### 2. Secuencias Numéricas Geométricas
Presenta secuencias numéricas basadas en patrones geométricos.

**Ejemplo:**
- **Desafío:** `3, 9, 27, ?`
- **Patrón:** Cada número es el anterior multiplicado por 3
- **Respuesta correcta**: `81`

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

print(f"Tipo de desafío: {challenge['type']}")
print(f"Desafío: {challenge['challenge']}")

# El agente automatizado resuelve el desafío
# Para base64: decodificar el texto
# Para secuencia: calcular el siguiente número

# Simular respuesta del agente
response = challenge['answer']  # En producción, el agente calcula esto

# Validar la respuesta
is_valid = validate_captcha(challenge, response)
print(f"¿Respuesta correcta? {is_valid}")
```

### Ejemplo Completo con Base64

```python
import base64
from captcha import generate_captcha, validate_captcha

# Generar desafío
challenge = generate_captcha()

if challenge['type'] == 'base64':
    # El agente decodifica el desafío
    encoded_text = challenge['challenge'].split(': ')[1]
    decoded_text = base64.b64decode(encoded_text).decode()
    
    # Validar
    is_valid = validate_captcha(challenge, decoded_text)
    print(f"Validación: {is_valid}")  # True
```

### Ejemplo Completo con Secuencia

```python
from captcha import generate_captcha, validate_captcha

# Generar desafío
challenge = generate_captcha()

if challenge['type'] == 'sequence':
    # El agente analiza la secuencia
    sequence_part = challenge['challenge'].split(': ')[1]
    sequence_str = sequence_part.replace(', ?', '')
    numbers = [int(n.strip()) for n in sequence_str.split(',')]
    
    # Calcular el patrón (razón geométrica)
    ratio = numbers[1] / numbers[0]
    next_number = int(numbers[-1] * ratio)
    
    # Validar
    is_valid = validate_captcha(challenge, str(next_number))
    print(f"Validación: {is_valid}")  # True
```

## 🧪 Testing

El proyecto incluye pruebas unitarias completas:

```bash
# Ejecutar todas las pruebas
python -m unittest test_captcha -v

# Ejecutar pruebas específicas
python -m unittest test_captcha.TestCaptcha -v
```

Las pruebas cubren:
- Generación correcta de desafíos
- Validación de respuestas correctas e incorrectas
- Manejo de espacios en blanco
- Casos específicos documentados
- Validación de formato de datos
- Patrones geométricos en secuencias

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
  - `challenge` (str): El desafío presentado
  - `answer` (str): La respuesta correcta

### `validate_captcha(challenge, response)`

Valida la respuesta de un usuario contra un desafío generado.

**Parámetros:**
- `challenge` (dict): El diccionario de desafío retornado por `generate_captcha()`
- `response` (str): La respuesta del usuario

**Retorna:**
- `bool`: `True` si la respuesta es correcta, `False` en caso contrario

## 🔮 Casos de Uso

Este sistema puede ser utilizado en:

1. **APIs para automatización**: Verificar que las solicitudes provienen de scripts autorizados
2. **Sistemas de integración**: Validar conexiones entre servicios automatizados
3. **Educación**: Enseñar conceptos de codificación y patrones matemáticos
4. **Juegos para desarrolladores**: Desafíos que requieren programación para resolver

## 🔧 Extensibilidad

El diseño modular permite agregar fácilmente nuevos tipos de desafíos:

```python
def _generate_custom_challenge():
    """Implementar nuevo tipo de desafío"""
    return {
        'type': 'custom',
        'challenge': 'tu_desafío_aquí',
        'answer': 'respuesta_correcta'
    }
```

Posibles extensiones futuras:
- Operaciones matemáticas complejas (factoriales, fibonacci, etc.)
- Conversión entre sistemas numéricos (binario, hexadecimal)
- Expresiones regulares complejas
- Cálculos hash (MD5, SHA)
- Operaciones con fechas y timestamps
- Parsing de JSON/XML

## 📝 Licencia

Este proyecto está disponible como código abierto bajo los términos de la licencia MIT.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## ⚠️ Notas de Seguridad

Este sistema está diseñado como una prueba de concepto y demostración educativa. Para uso en producción, considere:

- Implementar límites de tasa (rate limiting)
- Registrar y monitorear intentos de validación
- Rotar desafíos regularmente
- Implementar timeouts para respuestas
