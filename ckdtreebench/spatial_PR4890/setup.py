#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

from os.path import join


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs
    from numpy.distutils.system_info import get_info
    from distutils.sysconfig import get_python_inc

    config = Configuration('spatial_PR4890', parent_package, top_path)
    
    inc_dirs = [get_python_inc()]
    if inc_dirs[0] != get_python_inc(plat_specific=1):
        inc_dirs.append(get_python_inc(plat_specific=1))
    inc_dirs.append(get_numpy_include_dirs())

    # cKDTree    
    ckdtree_src = ['query.cxx', 
                   'globals.cxx',
                   'cpp_exc.cxx',
                   'query_pairs.cxx',
                   'count_neighbors.cxx',
                   'query_ball_point.cxx',
                   'query_ball_tree.cxx',
                   'sparse_distances.cxx']
                   
    ckdtree_src = [join('ckdtree', 'src', x) for x in ckdtree_src]
    
    ckdtree_headers = ['ckdtree_decl.h', 
                       'cpp_exc.h', 
                       'query_methods.h',
                       'cpp_utils.h',
                       'rectangle.h',
                       'ordered_pair.h']
                       
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
