import os
from setuptools import find_packages, setup

from pip.req import parse_requirements


def get_install_reqs():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    install_requires = parse_requirements(
        os.path.join(root_dir, 'requirements.txt'), session=False,
    )

    return [str(ir.req) for ir in install_requires]


setup(
    name="drfdocs",
    version=__import__('rest_framework_docs').__version__,
    author="Emmanouil Konstantinidis",
    author_email="manos@iamemmanouil.com",
    packages=find_packages(),
    include_package_data=True,
    url="http://www.drfdocs.com",
    license='BSD',
    description="Documentation for Web APIs made with Django Rest Framework.",
    long_description=open("README.md").read(),
    install_requires=get_install_reqs(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
