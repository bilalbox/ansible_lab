#!/usr/bin/env python

import docker
import json
import argparse
import sys


IMAGE_NAME = 'ansible:01'
GROUPS = {
    'lb': 1,
    'web': 3,
    'db': 2,
    }
BUILD_PARAMS = { 
    'path': './', 
    'tag': IMAGE_NAME,
    'rm': True,
    'forcerm': True,
    }


def main():
    client = docker.from_env()
    print('BUILDING DOCKER IMAGE...')
    client.images.build(**BUILD_PARAMS)
    print('DONE BUILDING!')
    print('RUNNING CONTAINERS...')
    for g,n in GROUPS.items():
        for i in range(n):
            cid = client.containers.run(
                name='{}{:03d}'.format(g,i+1),
                labels={'group': g},
                image=IMAGE_NAME,
                detach=True,
                init=True,
                tty=True,
            )
            print('RUNNING {}...'.format(cid))
    print('DONE! ALL CONTAINERS NOW RUNNING')


if __name__ == '__main__':
    main()

