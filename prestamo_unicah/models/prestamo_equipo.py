from odoo import models, fields, api


class PrestamoEquipo(models.Model):
    _name = 'prestamo.equipo'
    _description = 'Equipo disponible para préstamo'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string='Nombre del equipo',
        required=True
    )

    codigo = fields.Char(
        string='Código',
        required=True,
        copy=False
    )

    tipo = fields.Selection(
        [
            ('laptop', 'Laptop'),
            ('desktop', 'Computadora de escritorio'),
            ('proyector', 'Proyector'),
            ('tablet', 'Tablet'),
            ('otro', 'Otro'),
        ],
        string='Tipo de equipo',
        required=True
    )

    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    numero_serie = fields.Char(string='Número de serie')

    estado = fields.Selection(
        [
            ('disponible', 'Disponible'),
            ('prestado', 'Prestado'),
            ('mantenimiento', 'En mantenimiento'),
            ('baja', 'Dado de baja'),
        ],
        string='Estado',
        default='disponible',
        required=True
    )

    fecha_adquisicion = fields.Date(
        string='Fecha de adquisición'
    )

    observaciones = fields.Text(
        string='Observaciones'
    )

    active = fields.Boolean(
        string='Activo',
        default=True
    )

    _sql_constraints = [
        (
            'codigo_equipo_unique',
            'UNIQUE(codigo)',
            'El código del equipo debe ser único.'
        ),
    ]
