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

