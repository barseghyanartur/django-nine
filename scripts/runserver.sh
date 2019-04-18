#!/usr/bin/env bash

cd example/simple/

server="0.0.0.0"
port="8000"
if [[ $1 == "--port" ]]
then
    port="$2"
    shift
    shift
    args="$@"
else
    port="8000"
    args="$@"
fi

if [[ $args ]]
then
    ./manage.py runserver "$server:$port" --traceback -v 3 "$args"
else
    ./manage.py runserver "$server:$port" --traceback -v 3 "$@"
fi
