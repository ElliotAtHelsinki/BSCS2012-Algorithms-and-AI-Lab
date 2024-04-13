#!/bin/bash

if pip list | grep -q 'coverage'; then
  python -m coverage run --omit=*/dist-packages/*,functions.py,generate.py,encrypt.py,decrypt.py -m unittest
  python -m coverage report
else
  pip install coverage
  python -m coverage run --omit=*/dist-packages/*,functions.py,generate.py,encrypt.py,decrypt.py -m unittest
  python -m coverage report
fi
