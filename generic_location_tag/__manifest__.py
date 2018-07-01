{
    'name': "Generic Location Tag",

    'summary': """
    """,

    'author': "Center of Research & Development",
    'website': "https://crnd.pro",

    'category': 'Generic Location',
    'version': '11.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['generic_location', 'generic_tag'],

    # always loaded
    'data': [
        'data/generic_tag_model.xml',
        'views/generic_location_tag_menu.xml',
        'views/generic_location_tag.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo_location_tag.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'Other proprietary',
}