# ansible_lab

Lightweight docker-based lab for testing out ansible concepts.


# Pre-requisites

* docker 17.12.0-ce or greater (Installation instructions)
* python 2.7.12 or greater (Installation instructions)
* ansible 2.4.3.0 or greater (Installation instructions)


# Clone this repo

`git clone https://github.com/bilalbox/ansible_lab.git`


# Generate your SSH key and copy to build and playbook folders

`ssh-keygen`

`cd ansible_lab/docker`

`cp ~/.ssh/id_rsa.pub ./`

`cp ~/.ssh/id_rsa.pub files/authorized_keys.ansible`



# Run build script to build docker image and deploy lab

`chmod a+x build_docker_lab.py`

`./build_docker_lab.py`



# Cleanup when you're done

`chmod a+x cleanup.py`

`./cleanup.py`

