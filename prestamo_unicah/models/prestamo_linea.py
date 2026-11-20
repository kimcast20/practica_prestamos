from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PrestamoLinea(models.Model):
    _name = 'prestamo.linea'
    _description = 'Detalle de equipos prestados'

    prestamo_id = fields.Many2one(
        'prestamo.prestamo',
        string='Préstamo',
        required=True,
        ondelete='cascade'
    )

    equipo_id = fields.Many2one(
        'prestamo.equipo',
        string='Equipo',
        required=True
    )

    cantidad = fields.Integer(
        string='Cantidad',
        default=1,
        required=True
    )

    observaciones = fields.Char(
        string='Observaciones'
    )

    @api.constrains('cantidad')
    def _check_cantidad(self):
        for record in self:
            if record.cantidad <= 0:
                raise ValidationError(
                    'La cantidad debe ser mayor que cero.'
                )

    _sql_constraints = [
        (
            'equipo_prestamo_unique',
            'UNIQUE(prestamo_id, equipo_id)',
            'No se puede agregar el mismo equipo dos veces '
            'en un préstamo.'
        ),
    ]
