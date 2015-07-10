from setuptools import setup

setup(name='tciaexplorer',
        version='0.1',
        packages=['tciaexplorer'],
        author='Ganesh Iyer',
        install_requires=[
            'requests',
            'pyopenssl',
            'ndg-httpsclient',
            'pyasn1'
        ]
)
