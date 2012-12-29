from setuptools import setup, find_packages
setup(
    name="django-br-documents",
    version="0.0.1",
    packages=find_packages(),
    author="Felipe 'chronos' Prenholato",
    author_email="philipe.rp@gmail.com",
    maintainer="Felipe 'chronos' Prenholato",
    maintainer_email="philipe.rp@gmail.com",
    url="http://github.com/chronossc/django-br-documents",
    license='NEW BSD LICENSE: http://www.opensource.org/licenses/bsd-license.php',
    description="Provide fields for br_documents objects (CPF, CNPJ and other"
        "brazillian documents).",
    long_description="django-br-documents give you model fields, form fields"
        "and widgets to use with br_documents package objects.",
    classifiers=[
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=["Django>=1.4.3","br_documents"],
)
