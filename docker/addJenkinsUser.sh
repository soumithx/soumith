sudo usermod -aG docker jenkins
chmod 777 /var/run/docker.sock
systemctl restart jenkins
