#!/bin/bash

if which pylint >/dev/null; then
  pylint main.py
else
  pip install pylint
  pylint main.py
fi
