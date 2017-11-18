# -*- mode: ruby -*-
# vi: set ft=ruby :

ENV["LC_ALL"] = "en_US.UTF-8"

Vagrant.configure("2") do |config|
  config.vm.define "web" do |web|
    web.vm.box = "ubuntu/xenial64"

    web.vm.network "forwarded_port", guest: 3000, host: 3000
    web.vm.network "private_network", ip: "192.168.1.10"

    web.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "512"
    end

    web.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y build-essential python

      curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
      apt-get install -y nodejs

      mkdir /home/ubuntu/.npm-packages
      echo "prefix=/home/ubuntu/.npm-packages" >> /home/ubuntu/.npmrc

      echo "NPM_PACKAGES=\"/home/ubuntu/.npm-packages\"" >> /home/ubuntu/.bashrc
      echo "PATH=\"$NPM_PACKAGES/bin:$PATH\"" >> /home/ubuntu/.bashrc

      cd /vagrant/project && npm install
    SHELL
  end
end
