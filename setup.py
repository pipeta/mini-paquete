from setuptools import setup

setup(
    name='mini-paquete',
    version='0.1',
    packages=['mini-package'],
    url='https://github.com/pipeta/mi_paquete',
    license='',
    author='Felipe',
    author_email='pipe.tapia.guerra1@gmail.com',
    description='Este paquete permite obtener información de la página t13',
    install_requires=["requests","pandas","beautifulsoup4"],
    include_package_data=True
)
