"""
cmdv-rrm-anl.code.filemanagement.ingest
=======================================

code for ingesting CPOL and Berrimah files
to CF-Radial

.. autosummary::
    :toctree: generated/

    get_file_tree
"""

import os
from glob import glob


def get_file_tree(start_dir, pattern):
    """
    Make a list of all files matching pattern
    above start_dir

    Parameters
    ----------
    start_dir : string
        base_directory

    pattern : string
        pattern to match. Use * for wildcard

    Returns
    -------
    files : list
        list of strings
    """

    files = []

    for dir, _, _ in os.walk(start_dir):
        files.extend(glob(os.path.join(dir, pattern)))
    return files


def create_monthly_filelist_cpol(epoch, year,
                                 month, scantype,
                                 start_dir=None):
    """
    Get all radar files, will not work for vol files
    old lassen files.. this will be dealt later

    Parameters
    ----------
    epoch : string
         new, old

    year : string
        year in format YYYY

    month : string
        month in format MM

    scantype : string
        only useful for cpol, point, rhi, PPI

    start_dir : string, optional
        directory where radar files are located

    Returns
    -------
    radar_file_names : list
        list of strings with location of radra files
    """

    if start_dir is None:
        start_dir = '/lcrc/group/earthscience/radar/stage/'

    if radar == 'new':
        pattern = year + month + '*Gunn_Pt.rapic'

    if radar == 'old':
        pattern = '#Gunn_pt_' + year + month + '*_'\
                              + scantype.ucase() + '.lassen'

    radar_file_names = get_file_tree(start_dir, pattern)
    return radar_file_names
