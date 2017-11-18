import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ecom_merci',
    version='0.1.0',
    include_package_data=True,
    license='MIT License',  # example license
    description='Projeto de e-commerce desenvolvido em Python/Django.',
    long_description=README,
    url='https://github.com/Desenho-2-2017/Ecom_merci',
    author='Desenho-2-2017',
    author_email='jefersonalvesf2009@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],

    package_dir={'': 'src'},
    packages=find_packages('src'),
    
    install_requires=[
        #"django"
    ],
    
    extras_require={
        'dev': [
            #'pytest==3.2.3'
        ],
    },
    
    entry_points = {
       "console_scripts": ["ecom_merci = ecom_merci.__main__:main"]
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
)