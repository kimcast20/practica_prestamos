# Kimberly Yamileth Castro Moreno - 1502200700137
## Respuestas
### Paso 1. Catálogo de equipos

**1. ¿Qué pasa con un equipo cuando se desmarca el campo Activo? ¿Por qué es mejor que borrarlo?**

Cuando se desmarca el campo Activo, el equipo queda archivado y deja de aparecer en las búsquedas y listas habituales. Es mejor que eliminarlo porque se conserva su información y su historial, lo que permite consultarlo nuevamente si es necesario.

**2. ¿Para qué sirve copy=False en el campo codigo?**

Sirve para evitar que el código de inventario se copie automáticamente cuando se duplica un equipo. Así se evita que dos equipos tengan el mismo código de inventario.

### Paso 2. Registro de préstamos

**1. Este modelo usa `_name` y `_inherit` al mismo tiempo. ¿Qué hace cada uno aquí?**

`_name` permite crear un modelo nuevo llamado `prestamo.prestamo`, mientras que `_inherit` incorpora las funcionalidades del modelo `mail.thread`, como el chatter para registrar mensajes y cambios.

**2. ¿Qué hace `tracking=True` en el campo `state`?**

Permite llevar un seguimiento de los cambios realizados en el estado del préstamo, registrándolos en el chatter para poder consultar su historial.