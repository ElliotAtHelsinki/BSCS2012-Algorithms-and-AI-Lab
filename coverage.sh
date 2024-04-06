#!/bin/bash

if pip list | grep -q 'coverage'; then
  python -m coverage run -m unittest
  python -m coverage report
else
  pip install coverage
  python -m coverage run -m unittest
  python -m coverage report
fi
