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