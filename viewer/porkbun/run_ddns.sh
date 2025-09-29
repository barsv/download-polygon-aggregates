#!/usr/bin/env bash
set -e # exit on error
source ~/src/download-polygon-aggregates/viewer/porkbun/porkbun.env
exec /usr/bin/python3 ~/src/download-polygon-aggregates/viewer/porkbun/porkbun_dns.py