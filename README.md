# Guía de Práctica de Desarrollo Basado en Pruebas (TDD) con Python

## Configuración del Entorno

### Instalación de Chocolatey

Chocolatey es un gestor de paquetes para Windows que facilita la instalación de software.

1. **Abrir PowerShell como administrador**
    - Busca PowerShell en el menú de inicio, haz clic derecho sobre él y selecciona "Ejecutar como administrador".

2. **Verificar la Política de Ejecución**
    - Ejecuta el siguiente comando para verificar la política de ejecución:
    ```
    Get-ExecutionPolicy
    ```
    - Si está en `Restricted`, debes cambiarla para poder instalar Chocolatey.

3. **Instalar Chocolatey**
    - Ejecuta el siguiente comando:
    ```
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

4. **Verificar la Instalación de Chocolatey**
    - Escribe `choco` en la terminal para comprobar si está correctamente instalado.

### Instalación de Python

1. **Abrir PowerShell como administrador** (si ya lo cerraste después de instalar Chocolatey).

2. **Instalar Python**
    - Ejecuta el comando:
    ```
    choco install python
    ```
    - Añade el parámetro `--pre` si deseas instalar la pre-release.

3. **Verificar la Instalación de Python**
    - Abre una nueva terminal (`cmd`) y escribe `python3 --version`. Si eso no funciona, intenta con `python --version`.
    - **Importante:** Es posible que necesites reiniciar tu terminal o incluso tu computadora para que los cambios tengan efecto.

## Introducción al Desarrollo Basado en Pruebas (TDD)

El Desarrollo Basado en Pruebas (TDD) es una técnica de desarrollo de software que implica escribir pruebas antes de escribir el código que debe pasar estas pruebas.

### Ejemplo de TDD

A continuación, te mostramos cómo comenzar con TDD escribiendo una prueba simple para una función hipotética `suma`.

**Prueba para la función suma:**

```
import unittest

class TestSuma(unittest.TestCase):
    def test_suma(self):
        resultado = suma(5, 7)
        self.assertEqual(resultado, 12)

if __name__ == '__main__':
    unittest.main()
```
