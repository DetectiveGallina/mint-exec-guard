from distutils.core import setup
from DistUtilsExtra.command import *

class mint_exec_guard_build_i18n(build_i18n.build_i18n):
    def run(self):
         build_i18n.build_i18n.run(self)

setup(
    name='mint-exec-guard',
    version='1.0.0',
    url='https://github.com/DetectiveGallina/mint-exec-guard',
    author='Facundo Godoy',
    author_email='facundogodoyrentero@gmail.com',
    description='Mint Exec Guard',
    long_description=("Mint Exec Guard shows a warning when attempting to run unknown Linux or Windows executables and offers more trusted alternatives. Ported from the original Zorin Exec Guard."),
    license='GPL-3.0',

    packages=['mint_exec_guard'],
    package_dir={'mint_exec_guard': 'mint_exec_guard'},
    scripts=['bin/mint-exec-guard-linux','bin/mint-exec-guard-windows'],
    cmdclass = { "build" : build_extra.build_extra,
        "build_i18n" :  mint_exec_guard_build_i18n,
        "clean": clean_i18n.clean_i18n,
    }
)
