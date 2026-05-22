from setuptools import setup, find_packages

setup(
    name='ayudante',   
    version='0.1.0',
    description='Un paquete de ayuda para análisis de datos y visualizaciones',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'scipy',
        'scikit-learn'
    ],
    python_requires='>=3.13',
)