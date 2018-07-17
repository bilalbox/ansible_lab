#!/usr/bin/env python

import docker
import json
import argparse
import sys

CLIST = docker.from_env().containers.list()

def parse_args():
    parser = argparse.ArgumentParser(description='Docker Inventory Script')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--host')
    return parser.parse_args()


def list_running_hosts():
    hosts = {
        c.name: { 'ansible_host': c.attrs['NetworkSettings']['IPAddress'] }
        for c in CLIST
        }
    md = { 'hostvars' : hosts }
    groups = dict()
    for c in CLIST:
        g = c.labels['group']
        if g in groups.keys():
            groups[g].append(c.name)
        else:
            groups[g] = [c.name]
    groups['_meta'] = md
    return groups


def get_host_details(host):
    groups = list_running_hosts()
    return groups['_meta']['hostvars'][host]


def main():
    args = parse_args()
    if args.list:
        groups = list_running_hosts()
        json.dump(groups, sys.stdout)
    else:
        details = get_host_details(args.host)
        json.dump(details, sys.stdout)


if __name__ == '__main__':
    main()

