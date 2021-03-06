"""Tests for the file module, minus the IlambConfigFile class."""

import os
from nose.tools import raises, assert_true, assert_equal
from pbs_server.file import (get_region_labels_txt,
                             get_region_labels_ncdf)
from pbs_server import data_directory


regions_file_txt = 'tropics.txt'
regions_file_txt_path = os.path.join(data_directory, regions_file_txt)
labels_txt = ['tropics', 'afritrop']
regions_file_nc = 'basins_0.5x0.5.nc'
regions_file_nc_path = os.path.join(data_directory, regions_file_nc)
labels_nc = ['amazon', 'ob', 'lena']


@raises(IOError)
def test_get_region_labels_txt_path():
    get_region_labels_txt(regions_file_txt)


def test_get_region_labels_txt_type():
    x = get_region_labels_txt(regions_file_txt_path)
    assert_true(type(x), list)


def test_get_region_labels_txt_value():
    x = get_region_labels_txt(regions_file_txt_path)
    assert_equal(x, labels_txt)


@raises(IOError)
def test_get_region_labels_ncdf_path():
    get_region_labels_ncdf(regions_file_nc)


def test_get_region_labels_ncdf_type():
    x = get_region_labels_ncdf(regions_file_nc_path)
    assert_true(type(x), list)


def test_get_region_labels_ncdf_value():
    x = get_region_labels_ncdf(regions_file_nc_path)
    assert_equal(x[0:3], labels_nc)
