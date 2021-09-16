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
```

**box management**
```
vagrant box add ubuntu/precise64 
vagrant box list
```