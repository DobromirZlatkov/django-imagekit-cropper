from setuptools import setup, find_packages
#this is a test
setup(name = 'django-imagekit-cropper-py3.4.3',
      description = 'Allow users to manually specify image variant crops',
      version = '1.3.1',
      url = 'https://github.com/DobromirZlatkov/django-imagekit-cropper-py3.4.3',
      author = 'Dobromir Zlatkov',
      author_email='dobromir.v.zlatkov@gmail.com',
      license = 'BSD',
      packages=find_packages(),
      package_data={'': ['*.py','*.css','*.js']},
      include_package_data=True,
      install_requires = ['setuptools', 'Django', 'django-grappelli', 'django-imagekit'],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved',
            'Operating System :: OS Independent',
            'Programming Language :: Python'
      ]
)
