from setuptools import setup, find_packages

config = {
    'description': 'FIWARE Context Broker instance integration with the EDP',
    'author': 'CEF Digital',
    'url': 'https://github.com/ConnectingEurope/ContextBroker-EDP',
    'version': '1.0',
    'install_requires': ['Click', 'configobj', 'Flask', 'gunicorn', 'requests', 'time_uuid'],
    'packages': find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    'package_data': {'': ['logger.yml', 'integrated.ini', 'template.ini', 'template.xml', 'api/templates/error.html']},
    'include_package_data': True,
    'py_modules': ['cb_edp'],
    'name': 'cb-edp',
    'entry_points': '''
    	[console_scripts]
    	cb-edp=cb_edp.commands:cli
    	'''
}

# Add in any extra build steps for cython, etc.
setup(**config)
