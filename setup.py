from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open(os.path.join("src", "collective", "microsite", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "microsite", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "microsite", "docs", "INSTALL.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "microsite", "docs", "CONTRIBUTORS.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "microsite", "docs", "CREDITS.rst")).read())


setup(
    name='collective.microsite',
    version='0.0.0.1',
    description="Adds action to make folderish content micro site.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/collective/collective.microsite',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone>=4.2',
        'five.grok',
        'five.pt',
        'plone.app.dexterity',
        'hexagonit.testing',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
