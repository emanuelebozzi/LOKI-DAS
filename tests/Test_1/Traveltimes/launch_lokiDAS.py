#!/usr/bin/env python

"""
To call LOKI you need this file and make it executable (or call python)

"""

from loki.loki import Loki

db_path = './Test_1/Traveltimes'
data_path = './Test_1/Data'
output_path = './Test_1/output'
hdr_filename = 'header_long.hdr'
geometry_filename = 'station_das_ign.tmp'
inputs = {}
inputs['tshortp_min'] = 0.1
inputs['tshortp_max'] = 0.1
inputs['tshorts_min'] = 0.15
inputs['tshorts_max'] = 0.15
inputs['slrat'] = 2
inputs['npr'] = 2
inputs['ntrial'] = 1
inputs['derivative'] = True
inputs['vfunc'] = 'erg'
inputs['hfunc'] = 'pca'
inputs['model'] = 'das'
inputs['epsilon'] = 0.001
precision = 'single'
comp = ['E', 'N', 'Z']
inputs['extension_sta'] = '*'
inputs['extension_das'] = '.h5'
inputs['delta_das'] = 200

# =========  Call


l1 = Loki(data_path, output_path, db_path, hdr_filename, geometry_filename, mode='locator')
l1.location( comp, precision, **inputs)
