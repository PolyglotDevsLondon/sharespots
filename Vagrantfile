Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.box_version = "1.0.0"
  config.vm.box_download_insecure = true
  config.vm.network "forwarded_port", guest: 22, host: 2222, host_ip: "127.0.0.1", id: 'ssh'
end