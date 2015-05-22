#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

from os.path import join


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs
    from numpy.distutils.system_info import get_info
    from distutils.sysconfig import get_python_inc

    config = Configuration('spatial_016', parent_package, top_path)
    
    inc_dirs = [get_python_inc()]
    if inc_dirs[0] != get_python_inc(plat_specific=1):
        inc_dirs.append(get_python_inc(plat_specific=1))
    inc_dirs.append(get_numpy_include_dirs())

    ckdtree_src = ['ckdtree_query.cxx',
                   'ckdtree_globals.cxx',
                   'ckdtree_cpp_exc.cxx']
    ckdtree_src = [join('ckdtree', 'src', x) for x in ckdtree_src]
    
    ckdtree_headers = ['ckdtree_decl.h', 
                       'ckdtree_exc.h', 
                       'ckdtree_methods.h',
                       'ckdtree_utils.h']
    ckdtree_headers = [join('ckdtree', 'src', x) for x in ckdtree_headers]
    
    ckdtree_dep = ['ckdtree.cxx'] + ckdtree_headers + ckdtree_src
    config.add_extension('ckdtree',
                         sources=[join('ckdtree', 'ckdtree.cxx')] + ckdtree_src,
                         depends=ckdtree_dep,
                         include_dirs=inc_dirs + [join('ckdtree','src')])
    return config

if __name__ == '__main__':

    from numpy.distutils.core import setup
    setup(maintainer="SciPy Developers",
          author="Anne Archibald",
          maintainer_email="scipy-dev@scipy.org",
          description="Spatial algorithms and data structures",
          url="http://www.scipy.org",
          license="SciPy License (BSD Style)",
          **configuration(top_path='').todict()
          )
