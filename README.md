准备用来搭建一个基于IDA Pro的恶意代码静态特征提取平台

## Tree 
```
📦app  
 ┣ 📜execute_for_no_suffix.ps1
 ┗ 📜main.py
📦data # samples to be processed , the analysis result also stored there
📦templates # templates files for app environment
📦scripts # scripts for provisioning 
```

## TODO
- 创建预装IDA的base box

## Usage
1. batch processing mode
   > copy all samples into a folder, and execute the following commands for the the folder
   ```
   C:\app\execute_for_no_suffix.ps1 <script_path> <data_folder>
   ```
2. service mode
   ```

   ```
## Important Concepts
1. box: like image for docker
2. provision: a set of actions for running box to execute and generate new box

## Cheatsheet

**lifecycle management**
```
vagrant init ubuntu/precise64
vagrant up
vagrant provision # execute actions on the running vms 
vagrant reload # reload to update 
vagrant rdp # rdp into runnning vms
```

**box management**
```
vagrant box add ubuntu/precise64 
vagrant box list
```

**create box from vms**
```
cd VirtualBox\ VMs/ && vagarnt package --base Win10x64 --output Win10x64.box # 从vm创建box
vagrant box add dagrons/windows10 Win10x64.box # 添加到box list
```

## FAQ

**关于网络**

搜索Proxy Setting, 然后在里面设置号好IP和端口就好了

**关于一些无法用choco安装的软件**

如果不能用answerfile, 就只好自己定制base box, 然后基于定制的box编写Vagrantfile

