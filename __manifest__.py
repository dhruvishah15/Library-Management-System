# -*- coding: utf-8 -*-
{
    'name': "Library Management System",
    'summary': "Managing college library",
    ""
    'description': """
        Manage the college library
    """,
    'author': "Gopi",
    'category': 'extra tools',
    'version': '0.0.1',
    'sequence': 3,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/college_student_views.xml',
        'views/college_teacher_views.xml',
        'views/library_book_views.xml',
        'views/college_curriculum_views.xml'
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/icon.png'],
}