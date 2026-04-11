# Microservicio DevOps - EP1

## Descripcion
Microservicio REST desarrollado con Flask como base para el pipeline DevOps.

## Estrategia de Ramificacion: GitFlow
Elegimos GitFlow porque permite separar el codigo estable (main) del trabajo en progreso (develop), facilitando el trabajo en equipo y la trazabilidad.

## Estructura de ramas
- main: Codigo en produccion
- develop: Integracion de features
- feature/nombre: Nuevas funcionalidades
- hotfix/nombre: Correcciones urgentes

## Convenciones de Commits
- feat: Nueva funcionalidad
- fix: Correccion de bug
- docs: Documentacion
- ci: Cambios en pipeline
- refactor: Refactorizacion

## Flujo de Merge
1. Crear rama desde develop
2. Desarrollar y hacer commits
3. Abrir Pull Request con descripcion
4. Revision del codigo
5. Merge tras aprobacion

## GitHub Actions
El pipeline CI se ejecuta automaticamente con cada push a develop y pull request a main.

## Herramientas de IA
Se utilizo Claude (Anthropic) como apoyo para redaccion y estructura.
