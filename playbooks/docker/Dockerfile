FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python-minimal sudo openssh-server
RUN mkdir /var/run/sshd
RUN useradd --create-home --shell /bin/bash ansible &&\
    echo "ansible:ansible" | chpasswd &&\
    adduser ansible sudo &&\
    echo "ansible ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
ADD id_rsa.pub /tmp/id_sa.pub  
RUN mkdir /home/ansible/.ssh && cat /tmp/id_sa.pub >> /home/ansible/.ssh/authorized_keys && rm -f /tmp/id_sa.pub  
  

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
