from setuptools import setup

setup(
    name = 'wsgitalkback',
    version = '1.0',
    license = 'Apache Software License',
    url = 'http://www.github.com/pytalkweb',
    description = "A package to respond to http requests via mod_wsgi, implements RFC 2616,RFC 2965",
    long_description = __doc__,
    author = 'Madhukumar Seshadri',
    author_email = 'madhuseshadri@@gmail.com',
    zip_safe = False,
    platforms = 'any',
    packages = [
	    'wsgitalkback',
    ],
    include_package_data=True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
