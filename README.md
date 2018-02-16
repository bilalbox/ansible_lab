# ansible_lab
Lightweight docker-based lab for testing ansible concepts.


# Pre-requisites
* docker 17.12.0-ce or greater ([Installation instructions](https://docs.docker.com/install/))
* python 2.7.12 or greater ([Installation instructions](https://wiki.python.org/moin/BeginnersGuide/Download))
* ansible 2.4.3.0 or greater ([Installation instructions](http://docs.ansible.com/ansible/latest/intro_installation.html))


# Clone this repo
```bash
git clone https://github.com/bilalbox/ansible_lab.git
```

# Generate your SSH key and copy to build and playbook folders
```bash
ssh-keygen
cd ansible_lab/
cp ~/.ssh/id_rsa.pub docker/
cp ~/.ssh/id_rsa.pub playbooks/files/authorized_keys.ansible
```

# Run build script to build docker image and deploy lab
```bash
cd docker
chmod a+x build_docker_lab.py
./build_docker_lab.py
```

# Cleanup when you're done
```bash
chmod a+x cleanup.py
./cleanup.py
```

