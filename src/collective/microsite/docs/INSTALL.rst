Installation
------------

You may list ``collective.microsite`` to ``buildout.cfg`` or ``setup.py`` of your own package.

zc.buildout and the plone.recipe.zope2instance
==============================================

Use ``zc.buildout`` and the ``plone.recipe.zope2instance``
recipe by adding ``hexagonit.foldercontents`` to the list of egg::

    [buildout]
    ...
    eggs =
        ...
        collective.microsite

Dependency to your own package
==============================

You may also list to ``install_requires`` to ``setup.py`` within your package::

    setup(
        ...
        install_requires=[
            ...
            'collective.microsite',
            ...
        ],
        ...
    )