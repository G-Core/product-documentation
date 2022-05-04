#!/bin/sh

conf=$(envsubst '$SERVICE_PORT' < /etc/nginx/conf.d/default.conf)
echo "$conf" > /etc/nginx/conf.d/default.conf

nginx -g "daemon off;"
