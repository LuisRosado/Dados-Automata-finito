# Juego de Dados con Autómata Finito

Este es un pequeño proyecto de Python que implementa un juego de dados junto con un autómata finito que valida una cadena generada durante el juego.

## Descripción

El programa consta de dos partes principales:

1. **Juego de Dados**:
   - El usuario debe adivinar la suma de dos dados lanzados.
   - Se proporciona retroalimentación sobre la corrección de la respuesta del usuario.
   - El usuario tiene un número limitado de intentos para adivinar correctamente.

2. **Autómata Finito**:
   - El programa genera una cadena basada en las respuestas del usuario durante el juego de dados.
   - Esta cadena es validada por un autómata finito.
   - El autómata verifica si la cadena sigue un patrón específico y devuelve si es válida o no.

## Funcionamiento

- Ejecutar el programa `juego_de_dados.py`.
- Introducir el nombre de usuario y adivinar la suma de los dados según se solicite.
- Después de un número limitado de intentos, se valida la cadena generada durante el juego utilizando el autómata finito.
- Se informa al usuario si la cadena es válida o no.

## Requisitos

- Python 3.x
