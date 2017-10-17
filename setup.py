from distutils.core import setup

setup(
    name='deeproxy',
    version='0.10.17',
    packages=['deeproxy'],
    url='http://open.deepera.com',
    license='CPL-3.0',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Deepera Django Proxy System',
    install_requires=[
        'django',
        'djangorestframework',
    ],
)
