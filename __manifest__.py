# -*- coding: utf-8 -*-
{
    'name': "Product Meilisearch Connector",

    'summary': """
        A simple addon to connect odoo product searching in the website with meilisearch
        """,

    'description': """ ... """,

    'author': "Jorge Luis Alfonso Chavez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
