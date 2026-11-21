# Kimberly Yamileth Castro Moreno - 1502200700137
## Respuestas
### Paso 1. Catálogo de equipos

**1. ¿Qué pasa con un equipo cuando se desmarca el campo Activo? ¿Por qué es mejor que borrarlo?**

Cuando se desmarca el campo Activo, el equipo queda archivado y deja de aparecer en las búsquedas y listas habituales. Es mejor que eliminarlo porque se conserva su información y su historial, lo que permite consultarlo nuevamente si es necesario.

**2. ¿Para qué sirve copy=False en el campo codigo?**

Sirve para evitar que el código de inventario se copie automáticamente cuando se duplica un equipo. Así se evita que dos equipos tengan el mismo código de inventario.

### Paso 2. Registro de préstamos

**1. Este modelo usa _name y _inherit al mismo tiempo. ¿Qué hace cada uno aquí?**

_name permite crear un modelo nuevo llamado prestamo.prestamo, mientras que _inherit incorpora las funcionalidades del modelo mail.thread, como el chatter para registrar mensajes y cambios.

**2. ¿Qué hace tracking=True en el campo state?**

Permite llevar un seguimiento de los cambios realizados en el estado del préstamo, registrándolos en el chatter para poder consultar su historial.

### Paso 3. Equipos del préstamo

**1. En fields.One2many("prestamo.linea", "prestamo_id")`, ¿qué indica cada parámetro?**

El primer parámetro, prestamo.linea, indica el modelo relacionado que contiene las líneas del préstamo. El segundo, prestamo_id, indica el campo Many2one de ese modelo que establece la relación con el préstamo.

**2. ¿Qué pasa con las líneas cuando se borra un préstamo? ¿Qué parte del código lo define?**

Las líneas del préstamo se eliminan automáticamente cuando se borra el préstamo al que pertenecen. Esto se define mediante ondelete="cascade" en el campo prestamo_id del modelo prestamo_linea.py.

### Paso 4. Flujo de estados

**1. Los botones ya se ocultan según el estado. ¿Por qué los métodos vuelven a validar el estado?**

Porque los botones solo controlan lo que se muestra en la interfaz, pero los métodos también deben validar que la operación sea correcta. Así se evita que un préstamo cambie de estado de manera incorrecta.

**2. ¿Qué hace prestamo.linea_ids.equipo_id.write(...)? ¿Por qué no hace falta un for para cada equipo?**

Permite modificar el estado de todos los equipos relacionados con las líneas del préstamo. No hace falta un ciclo for porque Odoo permite ejecutar write() directamente sobre varios registros al mismo tiempo.

### Paso 5. Reglas del préstamo

**1. El campo equipo_id ya filtra los equipos disponibles. ¿Por qué hace falta el TODO 5?**

Porque el filtro solamente muestra los equipos disponibles al momento de seleccionarlos. Sin embargo, su estado podría cambiar antes de confirmar el préstamo. Por eso es necesario volver a verificar que el equipo siga disponible cuando se pulsa el botón Prestar.

**2. ¿En qué momento se ejecuta un método con @api.constrains? ¿Y la validación de action_prestar?**

Un método con @api.constrains se ejecuta cuando se modifican o guardan los campos indicados en la restricción. En cambio, las validaciones de action_prestar se ejecutan cuando el usuario pulsa el botón Prestar.

### Paso 6. Contacto, kanban y búsqueda

**1. ¿Qué pasa si arrastra una tarjeta del kanban a otra columna? ¿Por qué?**

La tarjeta cambia de estado porque las columnas representan los diferentes valores del campo estado. Al moverla, Odoo puede actualizar el valor de ese campo según la columna de destino.

**2. El campo prestamo_ids se agregó a res.partner. ¿Se crea una columna nueva en la tabla de contactos? Explique.**

No, porque prestamo_ids es un campo One2many. Este tipo de relación no crea una columna nueva en la tabla de contactos, sino que utiliza el campo Many2one partner_id del modelo de préstamos para relacionar los registros.