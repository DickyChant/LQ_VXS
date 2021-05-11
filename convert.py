#! /usr/env/python3

import os
filenames = os.listdir("LHEs")

for name in filenames:
	os.system(f"python3 LHEConverter.py -i LHEs/{name}")

