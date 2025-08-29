---
applyTo: '**/*.py'
---
- Contexto/versión:
    - Usa la versión de Python definida en pyproject.toml. Si no existe, asume Python 3.11.
    - Mantén compatibilidad con la matriz de CI si está definida.

- Estilo y formato:
    - Sigue PEP 8. Formatea con Black (line-length 88) y ordena imports con isort/ruff.
    - Usa f-strings; evita concatenaciones con +.
    - Nombres claros y descriptivos; evita abreviaturas crípticas.

- Tipado:
    - Habilita from __future__ import annotations en nuevos módulos.
    - Anota tipos en funciones públicas y en cualquier API. Evita Any salvo necesidad justificada.
    - Prefiere dataclasses/enums/TypedDict/Protocol cuando aporte claridad.

- Docstrings:
    - Estilo Google o NumPy en funciones no triviales y públicas. Explica efectos laterales, errores y ejemplos.
    - No repitas tipos ya expresados por hints; documenta el “por qué”, no el obvio “qué”.

- Manejo de errores:
    - Lanza excepciones específicas. Evita bare except y except Exception sin re-lanzar o registrar.
    - Valida entradas al inicio; mensajes de error útiles y accionables.

- Logging:
    - Usa logging (no print) con niveles adecuados. No registres secretos ni datos sensibles.

- Estructura y diseño:
    - Funciones pequeñas y puras cuando sea posible. Separa I/O de lógica.
    - No rompas API pública; usa deprecaciones cuando sea necesario.

- Concurrencia/I/O:
    - En async, evita bloqueos; usa bibliotecas compatibles (e.g., httpx/aiofiles).
    - Para operaciones costosas, considera concurrent.futures.

- Dependencias:
    - Prefiere stdlib. Justifica dependencias nuevas y fija versiones en pyproject/requirements.
    - Evita dependencias abandonadas; revisa licencias.

- Seguridad:
    - No uses eval/exec en entradas no confiables.
    - Valida/escapa datos externos. No expongas rutas ni detalles internos en errores.

- Rendimiento:
    - Evita complejidad innecesaria (cuida O(n^2)). Mide antes de micro-optimizar.
    - No copies colecciones grandes sin necesidad.

- Pruebas:
    - Usa pytest. Añade tests para nuevas funciones y errores corregidos.
    - Aísla I/O y red con fixtures/mocks. Cobertura mínima 90% en módulos nuevos.
    - Incluye casos límite y entradas inválidas.

- Documentación:
    - Actualiza README/CHANGELOG y docstrings cuando cambies comportamiento.
    - Incluye ejemplos de uso mínimos y reproducibles.

- Guías para IA (generar código/responder/revisar):
    - Haz preguntas aclaratorias si hay ambigüedad; enuncia supuestos explícitamente.
    - Mantén el estilo existente (formato, tipos, nombres). No introduzcas dependencias sin justificar.
    - Entrega snippets completos y ejecutables con imports necesarios.
    - No cambies APIs públicas ni contratos sin explicarlo y proponer migración.
    - Propón tests junto con el código. Señala implicaciones de seguridad y rendimiento.
    - Referencia rutas relativas del repo al sugerir cambios.
    - No uses emojis ni adornos; sé conciso y técnico.

- Convenciones adicionales:
    - Código, identificadores y comentarios en inglés. Mensajes de commit claros y en imperativo.
    - No uses iconos/emojis en bloques de código.