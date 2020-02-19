from setuptools import setup, find_packages

setup(
    # Application name:
    name="Ponto Digital",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Renato Valim",
    author_email="andradevalim.renato@gmail.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",

    #
    # license="LICENSE.txt",
    description="Aplicativo para deficientes visuais",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "flask-Login",
        "flask-MySQLdb",
        "flask-SQLAlchemy",
        "firebase-admin",
        "jwt",
        "pyjwt",
        "pymysql",
        "requests",
        "mysqlclient",
        "peewee",
        "SQLAlchemy",
        "mysql.connector"
    ],
)
