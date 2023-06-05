# -*- coding: utf-8 -*-
{
    "name": "sw_addon",
    "summary": """
        Module for test task.
        """,
    "description": """
        Adds planet to address, also adds model and menu item for planets.
        Menu item is located at "Contacts" -> "Settings" -> "Planets".
    """,
    "author": "RYDLAB",
    "website": "http://www.rydlab.ru",
    "category": "Customizations",
    "version": "16.0.1.0.0",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/planet.xml",
        "views/planet.xml",
    ],
}
