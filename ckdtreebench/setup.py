#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import sys
import os

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('ckdtreebench',parent_package,top_path)
    config.add_subpackage('spatial_015')
    config.add_subpackage('spatial_016')
    config.add_subpackage('spatial_PR4890')
    config.make_config_py()
    return config

if __name__ == '__main__':

    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())

