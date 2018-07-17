# ansible_lab
Run a python script which uses the Docker API to build and deploy a small collection of containers. Deploy simple tiered web-service using Ansible playbooks.


# Clone this repo
```bash
git clone https://github.com/bilalbox/terraform_ansible_labs.git
```

# Generate your SSH key and copy to build and playbook folders
```bash
ssh-keygen
cd terraform_ansible_labs/ansible/lab_01
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

