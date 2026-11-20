from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PrestamoPrestamo(models.Model):
    _name = 'prestamo.prestamo'
    _description = 'Solicitud de préstamo de equipo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'create_date desc'

    name = fields.Char(
        string='Número de préstamo',
        required=True,
        copy=False,
        default='Nuevo',
        tracking=True
    )

    solicitante_id = fields.Many2one(
        'res.partner',
        string='Solicitante',
        required=True,
        tracking=True
    )

    fecha_solicitud = fields.Date(
        string='Fecha de solicitud',
        default=fields.Date.context_today,
        required=True
    )

    fecha_inicio = fields.Date(
        string='Fecha de inicio',
        required=True,
        tracking=True
    )

    fecha_fin = fields.Date(
        string='Fecha de devolución prevista',
        required=True,
        tracking=True
    )

    fecha_devolucion_real = fields.Date(
        string='Fecha de devolución real',
        tracking=True
    )

    duracion = fields.Integer(
        string='Duración (días)',
        compute='_compute_duracion',
        store=True
    )

    linea_ids = fields.One2many(
        'prestamo.linea',
        'prestamo_id',
        string='Equipos solicitados'
    )

    estado = fields.Selection(
        [
            ('borrador', 'Borrador'),
            ('solicitado', 'Solicitado'),
            ('prestado', 'Prestado'),
            ('devuelto', 'Devuelto'),
            ('cancelado', 'Cancelado'),
        ],
        string='Estado',
        default='borrador',
        tracking=True,
        required=True
    )

    observaciones = fields.Text(
        string='Observaciones'
    )

    @api.depends('fecha_inicio', 'fecha_fin')
    def _compute_duracion(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                record.duracion = (
                    record.fecha_fin - record.fecha_inicio
                ).days
            else:
                record.duracion = 0

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if (
                record.fecha_inicio
                and record.fecha_fin
                and record.fecha_fin < record.fecha_inicio
            ):
                raise ValidationError(
                    'La fecha de devolución prevista no puede '
                    'ser anterior a la fecha de inicio.'
                )
