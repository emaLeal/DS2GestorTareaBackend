Contenido de TaskFlow_AllDeliverables.zip

•	README_BACKEND.md

Guía de instalación paso a paso (clonar repo, crear entorno virtual, instalar dependencias, correr migraciones, crear superusuario, arrancar servidor).

Ejemplos con cURL y Postman para probar el CRUD.

Sección de problemas comunes y soluciones.
¿Por qué?: Sirve como manual de usuario técnico y asegura que cualquiera pueda levantar el proyecto sin dudas.
ARQUITECTURA.md
Explicación de la arquitectura Frontend–Backend–DB.
Diagrama del flujo de autenticación con JWT.
Módulos del sistema y cómo interactúan (users, tasks, department, role).
¿Por qué?: Justifica el diseño del sistema y demuestra que la solución responde a los requisitos funcionales y no funcionales.


TECNOLOGIAS.md
Comparativa entre tecnologías posibles (Django vs Flask, Angular vs React, SQLite vs PostgreSQL).
Justificación de por qué se eligió cada una.

¿Por qué?: Responde a la rúbrica de “decisiones de arquitectura” y demuestra criterio técnico.
BRANCHING.md

Convención clara de ramas (feature/, fix/, docs/) con ejemplos vinculados a Jira.

Ejemplo de commit y Pull Request.
¿Por qué?: Facilita la trazabilidad (Jira ↔ Git) y garantiza orden en el trabajo en equipo.

DEPLOY_BACKEND.md
Variables de entorno explicadas línea por línea.
Pasos para despliegue en local, Render y Railway.
Ejemplo de pipeline CI/CD con GitHub Actions.
¿Por qué?: Permite poner la app en producción en un servicio gratuito y asegura la reproducibilidad del despliegue.

CRUD_TASKS.md
Explicación del CRUD de tareas en Django REST.
Código comentado, ejemplo de request y response.
Tablas con campos obligatorios y de solo lectura.
¿Por qué?: Demuestra que el núcleo funcional del sistema (gestión de tareas) está implementado y documentado.
•	TASK_SERVICE.ts
Servicio Angular documentado (list, create, patch, remove).
Ejemplo de integración en un componente.
¿Por qué?: Asegura la comunicación correcta entre el frontend y el backend.


Archivos Python de la app tasks/

models.py → Define el modelo Task con auditoría mínima y soft delete.
serializers.py → Serializadores para creación/edición y lectura.
views.py → Vistas basadas en clases con permisos, filtros y auditoría.
urls.py → Define endpoints CRUD (/api/task/ y /api/task/<id>/).
¿Por qué?: Son la implementación concreta del CRUD, validan que los requisitos funcionales estén cubiertos (crear, leer, actualizar, eliminar).

Pruebas funcionales automatizadas

tests.py
Usa APITestCase de DRF.
Cubre flujo completo: login, crear tarea, listar, actualizar, eliminar (soft delete).
Verifica respuestas HTTP y consistencia de datos.
¿Por qué?: Garantiza que el CRUD funciona realmente end-to-end y que el sistema cumple con los criterios de aceptación definidos.

Paquetes intermedios

•	TaskFlow_Deliverables_Extended.zip (documentación extendida en Markdown).
•	TaskFlow_TasksApp_Python.zip (código CRUD Python).
¿Por qué?: Incluidos como respaldo en caso de que quieras usarlos por separado