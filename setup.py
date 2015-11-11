from setuptools import setup, find_packages

setup(
    name="kraki",
    version="0.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="",
    description="Commandline interface for Rolf",
    long_description="Simple commandline tool for interfacing with the Rolf deployment manager",
    install_requires = ['requests', 'blessings', 'pyopenssl', 'ndg-httpsclient', 'pyasn1', 'cryptography', 'certifi', 'urllib3'],
    scripts = ['scripts/kraki'],
    license = "BSD",
    platforms = ["any"],
    zip_safe=False,
    package_data = {'' : ['*.*']},
    packages=['kraki'],
    test_suite='nose.collector',
    )
