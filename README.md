# ProyectoCoder

- Todas las vistas son hechas con plantilla padre. 
- La vista de inicio dejamos la de Bootstrap.
- Las otras 4 vistas apuntan a la misma plantilla (formulario_generico.html), donde por contexto le pasamos los formularios a mostrar.
Hay un formulario para agregar registro al modelo y un formulario para buscar en el modelo:
      - Profesores: Se busca por Apellido
      - Cursos: Se busca por Camada
      - Estudiantes: Se busca por Apellido
      - Entregables: Se busca por Nombre
- Los formularios de búsqueda direccionan a plantillas separadas (ejemplo: resultados_cursos.html). Podría mejorarse para que los resultados usen todos la misma plantilla.
- Todos los formularios de ingreso direccionan a la misma plantilla (gracias_ingreso.html), donde por contexto pasamos desde dónde se actualizó la BBDD.
- En el formulario para ingresar Entregables, debemos usar 'entregado = forms.BooleanField(required=False)' para poder ingresar entregables con 'entregado=False'.

Para probar las búsquedas de cada modelo una opción es:
- Proesores, apellido: Mezio
- Cursos, camada: 12345
- Estudiantes, apellido: Marmol
- Entregables, nombre: Alejandro

