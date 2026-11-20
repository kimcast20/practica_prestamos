{
    'name': 'Gestión de Préstamo de Equipo',
    'version': '1.0',
    'summary': 'Administración de préstamos de equipo',
    'description': """
        Módulo para gestionar equipos y sus préstamos.
    """,
    'category': 'Operations',
    'author': 'UNICAH',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/prestamo_equipo_views.xml',
        'views/prestamo_prestamo_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}