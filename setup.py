import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='dokr',

     version='0.1',

     scripts=['dokr'] ,

     author="Carlos Ferreira",

     author_email="carlos.ferreira@us.ibm.com",

     description="An unnoffical package to install Watosn IOO Functions",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/javatechy/dokr",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )