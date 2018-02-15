#!/usr/bin/env python

import docker


def main():
    client = docker.from_env()
    print('REMOVING STOPPED CONTAINERS.')
    client.containers.prune()
    print('REMOVING RUNNING CONTAINERS...')
    for c in client.containers.list():
        c.remove(v=True,force=True)
    print('DONE! ALL CONTAINERS REMOVED.')


if __name__ == '__main__':
    main()

