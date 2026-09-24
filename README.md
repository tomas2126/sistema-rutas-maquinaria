# Sistema inteligente de atención de maquinaria

## Descripción

Este proyecto presenta un sistema inteligente basado en reglas desarrollado en Python. El sistema utiliza una base de conocimiento para identificar diferentes tipos de fallas en maquinaria y determinar una ruta de atención según la información almacenada.

El programa recibe como entrada el tipo de falla y, mediante reglas lógicas, identifica:

* Área responsable de la atención.
* Técnico encargado.
* Nivel de prioridad.
* Ruta recomendada para solucionar la falla.

El proyecto permite demostrar de manera práctica el funcionamiento de un sistema basado en conocimiento y reglas.

## Objetivo

Desarrollar un programa en Python que utilice una base de conocimiento y reglas lógicas para determinar una ruta de atención frente a diferentes tipos de fallas en maquinaria.

## Tecnologías utilizadas

* Python 3
* Git
* GitHub
* Visual Studio Code
* PowerShell

## Estructura del sistema

El programa está compuesto por los siguientes elementos:

### 1. Base de conocimiento

Contiene la información relacionada con cada tipo de falla:

* Eléctrica
* Mecánica
* Hidráulica
* Neumática
* Software

Para cada falla se almacena el área responsable, el técnico encargado y la prioridad de atención.

### 2. Reglas

Las reglas relacionan el tipo de falla con el área encargada.

Por ejemplo:

**SI** la falla es eléctrica
**ENTONCES** debe ser atendida por el área eléctrica.

### 3. Búsqueda

El sistema recibe la falla ingresada por el usuario y consulta la base de conocimiento para encontrar la información correspondiente.

### 4. Ruta de atención

Cuando se encuentra una regla válida, el sistema genera una ruta:

1. Máquina con falla
2. Diagnóstico
3. Área responsable
4. Técnico encargado
5. Reparación

### 5. Validación

Si el usuario introduce una falla que no está registrada en la base de conocimiento, el sistema informa que no existe una regla para atenderla y muestra las opciones disponibles.

## Ejecución del programa

### Requisitos

Tener instalado Python 3 y Git.

Para comprobar que Python está instalado, ejecutar:

```bash
py --version
```

### Ejecutar el programa

Ubicarse en la carpeta del proyecto:

```powershell
cd "C:\Users\TDPU\Desktop\Actividad 2"
```

Después ejecutar:

```powershell
py sistema-rutas-maquinaria.py
```

El programa mostrará las fallas disponibles y solicitará al usuario seleccionar una.

## Ejemplo de ejecución

Entrada:

```text
Ingrese el tipo de falla: Electrica
```

Resultado:

```text
Falla identificada: Electrica

Regla aplicada:
Si la falla es eléctrica, debe ser atendida por el área eléctrica.

Prioridad de atención: Alta

Ruta recomendada:
1. Máquina con falla
2. Diagnóstico
3. Área eléctrica
4. Técnico electricista
5. Reparación
```

## Conceptos de Inteligencia Artificial utilizados

El proyecto aplica conceptos relacionados con los sistemas inteligentes basados en conocimiento:

* Base de conocimiento.
* Representación del conocimiento.
* Reglas lógicas.
* Condiciones.
* Búsqueda de información.
* Inferencia mediante reglas.
* Toma de decisiones basada en conocimiento.

La lógica principal del sistema puede representarse de la siguiente manera:

```text
Tipo de falla
      ↓
Consulta de la base de conocimiento
      ↓
Aplicación de una regla
      ↓
Identificación del área
      ↓
Identificación del técnico
      ↓
Prioridad
      ↓
Ruta de atención
```

## Autores

Proyecto académico desarrollado para la asignatura:

**Inteligencia Artificial**
Corporación Universitaria Iberoamericana
Actividad 2 - Búsqueda y sistemas basados en reglas

## Repositorio

El código fuente de este proyecto se encuentra disponible en GitHub.

**Repositorio:**
https://github.com/tomas2126/sistema-rutas-maquinaria
