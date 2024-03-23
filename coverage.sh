#!/bin/bash

if pip list | grep -q 'coverage'; then
  python -m coverage run -m unittest
else
  pip install coverage
  python -m coverage run -m unittest
fi
