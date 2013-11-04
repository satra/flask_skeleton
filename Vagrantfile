VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :web do |web_config|
    # web_config.vm.box = "precise64_base"
    # web_config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    web_config.vm.box = "gridneuro"
    web_config.vm.box_url = "https://dl.dropboxusercontent.com/u/363467/precise64_neuro.box"
    web_config.vm.network :forwarded_port, guest: 80, host: 8080
    web_config.vm.network :public_network, :bridge => 'en0: Wi-Fi (AirPort)'
    web_config.vm.network :private_network, ip: "192.168.100.10"

    web_config.vm.hostname = 'neuro'
    web_config.vm.synced_folder "../software", "/software"
    web_config.vm.synced_folder "../data", "/data"

    web_config.vm.provider :virtualbox do |vb|
    #   # Don't boot with headless mode
    #   vb.gui = true
    #
    #   # Use VBoxManage to customize the VM. For example to change memory:
     vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
     vb.customize ["modifyvm", :id, "--ioapic", "on"]
     vb.customize ["modifyvm", :id, "--memory", "4096"]
     vb.customize ["modifyvm", :id, "--cpus", "4"]
    end

    web_config.vm.provision :ansible do |ansible|
      ansible.playbook = "ops/vagrant-webserver.yml"
	  ansible.inventory_path = "ops/vagrant-hosts"
    end
  end

  config.vm.define :db do |db_config|
    db_config.vm.box = "precise64_base"
    db_config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    db_config.vm.network :forwarded_port, guest: 5432, host: 54322
    db_config.vm.network :public_network, :bridge => 'en0: Wi-Fi (AirPort)'
    db_config.vm.network :private_network, ip: "192.168.100.20"

    db_config.vm.provision :ansible do |ansible|
      ansible.playbook = "ops/vagrant-dbserver.yml"
	  ansible.inventory_path = "ops/vagrant-hosts"
    end
  end
end
