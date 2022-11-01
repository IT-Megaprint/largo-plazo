# -*- coding: utf-8 -*-
{
    'name': "Point of Sale Extended",

    'summary': """
        Customized Receipt""",

    'description': """
        Point of sale receipt customized
    """,

    'author': "aleemcaan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'fel_megaprint'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_assets.xml',
    ],
    'qweb':[
        'static/src/xml/Screens/ReceiptScreen/CustomOrderReceipt.xml'
    ]

}
