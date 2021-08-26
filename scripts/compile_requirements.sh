#!/usr/bin/env bash
cd examples/requirements/

echo "pip-compile base.in"
pip-compile base.in "$@"

echo "pip-compile common.in"
pip-compile common.in "$@"

echo "pip-compile django_1_4.in"
pip-compile django_1_4.in "$@"

echo "pip-compile django_1_5.in"
pip-compile django_1_5.in "$@"

echo "pip-compile django_1_6.in"
pip-compile django_1_6.in "$@"

echo "pip-compile django_1_7.in"
pip-compile django_1_7.in "$@"

echo "pip-compile django_1_8.in"
pip-compile django_1_8.in "$@"

echo "pip-compile django_1_9.in"
pip-compile django_1_9.in "$@"

echo "pip-compile django_1_10.in"
pip-compile django_1_10.in "$@"

echo "pip-compile django_1_11.in"
pip-compile django_1_11.in "$@"

echo "pip-compile django_2_0.in"
pip-compile django_2_0.in "$@"

echo "pip-compile django_2_1.in"
pip-compile django_2_1.in "$@"

echo "pip-compile django_2_2.in"
pip-compile django_2_2.in "$@"

echo "pip-compile django_3_0.in"
pip-compile django_3_0.in "$@"

echo "pip-compile django_3_1.in"
pip-compile django_3_1.in "$@"

echo "pip-compile django_3_2.in"
pip-compile django_3_2.in "$@"

echo "pip-compile django_master.in"
pip-compile django_master.in "$@"

echo "pip-compile testing.in"
pip-compile testing.in "$@"
