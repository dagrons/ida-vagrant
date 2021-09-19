# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "gusztavvargadr/windows-10"
  config.vm.box_check_update = false

  # config.vm.provision "file", source: "./templates/ida_7.0/ida_7.0.zip", destination: "ida_7.0.zip"  # copy file to Documents  
  # config.vm.provision "shell", inline: "Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"  
  # config.vm.provision "shell", inline: "choco install -y 7zip.install git visualstudiocode microsoft-windows-terminal -y"  
  # config.vm.provision "shell", path: "./scripts/add_idapython_to_path.ps1"   
  config.vm.provision "shell", inline: "pip install flask"

  config.vm.network "forwarded_port", guest: 5000, host: 5001, host_ip: "127.0.0.1"

  config.vm.synced_folder "./app", "/app"
  config.vm.synced_folder "./data", "/data"
  config.vm.synced_folder "./ida-scripts", "/ida-scripts"
end
