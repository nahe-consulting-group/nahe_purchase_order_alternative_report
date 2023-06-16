{
    'name': 'NAHE Purchase Order Alternative Report',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Alternative Purchase Order Report',
    'sequence': 10,
    'license': 'LGPL-3',
    'author': 'Matias. B. Nahe Consulting Group',
    'maintainer': 'Matias B',
    'website': 'www.nahe.com.ar',
    'depends': ['purchase'],
    'data': [
        'report/purchase_order_alternative_report.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': """
    Este módulo proporciona un informe alternativo para las órdenes de compra.
    """,
}
