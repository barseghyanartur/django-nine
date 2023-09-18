#!/usr/bin/env bash
cd examples/requirements/

#echo "\n\npip-compile base.in"
#pip-compile base.in "$@"

#echo "\n\npip-compile common.in"
#pip-compile common.in "$@"

echo "\n\npip-compile debug.in"
pip-compile debug.in "$@"

echo "\n\npip-compile django_1_4.in"
pip-compile django_1_4.in "$@"

echo "\n\npip-compile django_1_5.in"
pip-compile django_1_5.in "$@"

echo "\n\npip-compile django_1_6.in"
pip-compile django_1_6.in "$@"

echo "\n\npip-compile django_1_7.in"
pip-compile django_1_7.in "$@"

echo "\n\npip-compile django_1_8.in"
pip-compile django_1_8.in "$@"

echo "\n\npip-compile django_1_9.in"
pip-compile django_1_9.in "$@"

echo "\n\npip-compile django_1_10.in"
pip-compile django_1_10.in "$@"

echo "\n\npip-compile django_1_11.in"
pip-compile django_1_11.in "$@"

echo "\n\npip-compile django_2_0.in"
pip-compile django_2_0.in "$@"

echo "\n\npip-compile django_2_1.in"
pip-compile django_2_1.in "$@"

echo "\n\npip-compile django_2_2.in"
pip-compile django_2_2.in "$@"

echo "\n\npip-compile django_3_0.in"
pip-compile django_3_0.in "$@"

echo "\n\npip-compile django_3_1.in"
pip-compile django_3_1.in "$@"

echo "\n\npip-compile django_3_2.in"
pip-compile django_3_2.in "$@"

echo "\n\npip-compile django_4_0.in"
pip-compile django_4_0.in "$@"

echo "\n\npip-compile django_4_1.in"
pip-compile django_4_1.in "$@"

echo "\n\npip-compile django_4_2.in"
pip-compile django_4_2.in "$@"

echo "\n\npip-compile django_master.in"
pip-compile django_master.in "$@"

echo "\n\npip-compile docs.in"
pip-compile docs.in "$@"

echo "\n\npip-compile style_checkers.in"
pip-compile style_checkers.in "$@"

echo "\n\npip-compile testing.in"
pip-compile testing.in "$@"
