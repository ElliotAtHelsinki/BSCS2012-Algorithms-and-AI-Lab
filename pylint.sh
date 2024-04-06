#!/bin/bash

if which pylint >/dev/null; then
  pylint functions
else
  pip install pylint
  pylint functions
fi
