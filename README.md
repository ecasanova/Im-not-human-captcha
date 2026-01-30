# I'm Not Human CAPTCHA

A reverse CAPTCHA system designed to be solved by automated agents but difficult for humans.

## Descripción del Proyecto

Este proyecto implementa un sistema de CAPTCHA innovador que invierte el concepto tradicional: en lugar de validar que el usuario es humano, valida que el usuario es una máquina o agente automatizado. El sistema presenta desafíos que son triviales para scripts pero complejos o tediosos para humanos.

## Tipos de Desafíos

### 1. Texto Codificado en Base64
El sistema genera un texto codificado en base64 que debe ser decodificado.

**Ejemplo:**
- **Texto original:** `SoloParaAgentes`
- **Desafío (codificado):** `U29sb1BhcmFBZ2VudGVz`
- **Respuesta esperada:** `SoloParaAgentes`

### 2. Secuencia Numérica Geométrica
El sistema presenta una secuencia numérica que sigue un patrón geométrico. El desafío es calcular el siguiente número en la secuencia.

**Ejemplo:**
- **Desafío:** `3, 9, 27, ?`
- **Patrón:** Cada número es el anterior multiplicado por 3
- **Respuesta esperada:** `81`

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/ecasanova/Im-not-human-captcha.git
cd Im-not-human-captcha

# No se requieren dependencias adicionales (solo Python 3.6+)
```

## Uso

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
    encoded_text = challenge['challenge']
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
    sequence_str = challenge['challenge'].replace(', ?', '')
    numbers = [int(n.strip()) for n in sequence_str.split(',')]
    
    # Calcular el patrón (razón geométrica)
    ratio = numbers[1] / numbers[0]
    next_number = int(numbers[-1] * ratio)
    
    # Validar
    is_valid = validate_captcha(challenge, str(next_number))
    print(f"Validación: {is_valid}")  # True
```

## API Reference

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

## Testing

El proyecto incluye pruebas unitarias completas:

```bash
# Ejecutar todas las pruebas
python -m unittest test_captcha -v

# Ejecutar pruebas específicas
python -m unittest test_captcha.TestCaptcha -v
python -m unittest test_captcha.TestBase64Challenge -v
python -m unittest test_captcha.TestSequenceChallenge -v
```

## Casos de Uso

Este sistema puede ser utilizado en:

1. **APIs para automatización**: Verificar que las solicitudes provienen de scripts autorizados
2. **Sistemas de integración**: Validar conexiones entre servicios automatizados
3. **Educación**: Enseñar conceptos de codificación y patrones matemáticos
4. **Juegos para desarrolladores**: Desafíos que requieren programación para resolver

## Extensibilidad

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

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto está disponible como código abierto bajo los términos de la licencia MIT.

## Autor

- ecasanova

## Notas de Seguridad

Este sistema está diseñado como una prueba de concepto y demostración educativa. Para uso en producción, considere:

- Implementar límites de tasa (rate limiting)
- Registrar y monitorear intentos de validación
- Rotar desafíos regularmente
- Implementar timeouts para respuestas
