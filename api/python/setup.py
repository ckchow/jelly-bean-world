from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext

extra_compile_args = {
    'msvc' : ['/W3', '/GT', '/Ox', '/Ot', '/Oy', '/DNDEBUG', '/DUNICODE'],
    'unix' : ['-std=c++11', '-O3', '-DNDEBUG', '-fno-stack-protector', '-march=native']}
extra_link_args = {
    'msvc' : ['ws2_32.lib']}

class build_ext_subclass(build_ext):
  def build_extensions(self):
    c = self.compiler.compiler_type
    if c in extra_compile_args:
      for e in self.extensions:
        e.extra_compile_args = extra_compile_args[c]
    if c in extra_link_args:
      for e in self.extensions:
        e.extra_link_args = extra_link_args[c]
    build_ext.build_extensions(self)

simulator_c = Extension(
  'nel.simulator_c',
  define_macros = [('MAJOR_VERSION', '1'),
                   ('MINOR_VERSION', '0')],
  include_dirs = ['../..', '../../deps'],
  # libraries = ['...'],
  # library_dirs = ['/usr/local/lib'],
  sources = ['nel/simulator.cpp'])

setup(
  name = 'nel',
  version = '1.0',
  description = 'Never-ending learning framework',
  ext_modules = [simulator_c],
  packages = ['nel'], 
  install_requires = ['enum34'],
  cmdclass = {'build_ext' : build_ext_subclass} )
