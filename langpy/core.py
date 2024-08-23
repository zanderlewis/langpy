from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import numpy
from Cython.Build import cythonize
from setuptools_rust import RustExtension

class langpy:
    def __init__(self):
        self.ext_modules = []

    def add_extension(self, name, sources, language, fortran_type='f90'):
        if language == 'fortran':
            self.ext_modules.append(Extension(
                name, 
                sources, 
                language=fortran_type,
                include_dirs=[numpy.get_include()]
            ))
        elif language == 'cython':
            self.ext_modules.extend(cythonize(sources))
        elif language == 'rust':
            self.ext_modules.append(RustExtension(name, sources))
        else:
            self.ext_modules.append(Extension(name, sources, language=language))

    def build(self, **kwargs):
        setup(
            **kwargs,
            ext_modules=self.ext_modules,
            cmdclass={'build_ext': build_ext},
        )

"""
# Example usage
builder = langpy()

builder.add_extension("example_c", ["src/example.c"], "c")
builder.add_extension("example_cpp", ["src/example.cpp"], "c++")
builder.add_extension("example_fortran", ["src/example.f90"], "fortran")
builder.add_extension("example_python", ["src/example.py"], "python")
builder.add_extension("example_cython", ["src/example.pyx"], "cython")
builder.add_extension("example_rust", ["src/lib.rs"], "rust")

builder.build(
    name="example",
    version="0.0.1",
    description="Example package",
    author="Author",
    author_email="author@example.com",
    url="https://example.com"
)
"""