#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

from os.path import join

import os
import sys
import subprocess

def generate_cython():
    cwd = os.path.abspath(os.path.dirname(__file__))
    print("Cythonizing sources")
    p = subprocess.call([sys.executable,
                         os.path.join(cwd, 'tools', 'cythonize.py'),
                         'ckdtreebench'],
                        cwd=cwd)
    if p != 0:
        raise RuntimeError("Running cythonize failed!")


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('ckdtreebench')
    
    return config


def setup_package():

    metadata = dict(
        name='ckdtreebench',
        maintainer="Sturla Molden"
    )

    from numpy.distutils.core import setup

    generate_cython()
    metadata['configuration'] = configuration
    setup(**metadata)

if __name__ == '__main__':
    setup_package()

