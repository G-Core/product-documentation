---
title: manage-cloud-via-ansible
displayName: Ansible
order: 140
published: true
toc:
   --1--Install and configure Ansible: "install-and-configure-ansible"
   --1--Add Gcore collection from Galaxy: "add-gcore-collection-from-galaxy"
   --1--Validate Ansible configuration: "validate-ansible-configuration"
   --1--Manage Cloud resources: "manage-cloud-resources"   
pageTitle: Manage Gcore Edge Cloud via Ansible | Gcore
pageDescription: Learn how to manage your cloud resources using Ansible. Follow the guide to install Ansible and create VMs and manage cloud resources.
---
# Manage cloud resources via Ansible

<a href="https://www.ansible.com/" target="_blank">Ansible</a> is a configuration management tool used for provisioning, deploying, and orchestrating IT resources. Similarly to <a href="https://gcore.com/docs/cloud/manage-cloud-via-terraform" target="_blank">using Terraform</a>, you can use Ansible to create and set up Gcore Cloud services. 

You can find all Ansible modules and plugins required to interact with the Gcore Cloud in the following collection: <a href="https://galaxy.ansible.com/ui/repo/published/gcore/cloud/docs/" target="_blank">Ansible Galaxy Collection for Gcore Cloud</a>. 

## Install and configure Ansible

There are several methods for installing Ansible that depend on the type of your machine’s operating system.

<alert-element type="tip" title="Tip">
 
If you already have Ansible installed, ensure that you’re using the recommended version of Python: 3.11 or higher. To check your Ansible and Python versions and get more details about the configuration, run `ansible –version`.
 
</alert-element>

<tabset-element>

### Install Ansible on Ubuntu

Run the following command: `apt-get install ansible`. 

### Install Ansible on CentOS 

1\. Install Extra Packages for Enterprise Linux (EPEL): 
 
```
yum install epel-release 
```

2\. Install Python 3.11 or higher.  

``` 
yum install python3.11
```

3\. Install Ansible in your environment:  
 
```
yum install ansible 
```

### Install Ansible via Python’s pipx 

You can also use pipx to install Ansible on most systems. For details, check out the <a href="https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-and-upgrading-ansible-with-pipx" target="_blank">official Ansible documentation</a>.

</tabset-element>

## Add Gcore collection from Galaxy 

We have a dedicated <a href="https://galaxy.ansible.com/ui/repo/published/gcore/cloud/docs/" target="-blank">Ansible Galaxy Collection</a> that contains all modules and plugins you need for interacting with the Gcore Cloud.  

To install the collection, run the following command: 

```
ansible-galaxy collection install gcore.cloud  
``` 

You can now use all modules and plugins provided by the collection to manage your resources in the Gcore Cloud. 
 
## Validate Ansible configuration

To ensure that everything works as expected, run a test playbook according to the following instructions. 

1\. Configure the playbook:  

<code-block>
--- 
- name: Gather Gcore instances info 
  hosts: localhost 
  vars: 
    ansible_python_interpreter: /usr/bin/python3.11 
  tasks: 
    - gcore.cloud.instance_info: 
        api_key: "<span style="color:#FF5913">add your api key</span>" 
        region_name: "<span style="color:#FF5913">specify region</span>" 
        project_id: "<span style="color:#FF5913">add your project ID</span>"
</code-block>

<expandable-element title="Descriptions of the configuration parameters">

* `api_key`: The API key created in the Gcore Customer Portal in the profile settings. 
* `region_name`: A region in which your cloud resource is created.  
* `project_id`: An ID of the project that contains your cloud resources. You can check the ID in the Gcore Customer Portal on the Projects page. 
 
</expandable-element>

<alert-element type="info" title="Info">
 
In the playbook configuration, add the ansible_python_interpreter: `/usr/bin/python3.11` variable only if your Python version is lower than the recommended `3.11`.
 
</alert-element>

2\. Start the playbook:  `ansible-playbook ./get_instance.yaml -v`.

3\. If you correctly configured Ansible, you should see one of the following: 

 * If you have any instances created in the specified region, you’ll get a summary of their setup. 
 * In case you have no cloud resources created in the specified region, you'll get an empty response. 

## Manage Cloud resources

Use modules and plugins from our <a href="https://galaxy.ansible.com/ui/repo/published/gcore/cloud/docs/" target="_blank">Ansible Collection</a> to create playbooks customized to your infrastructure requirements and deployment workflows. 

As an example, let’s create a `test.yaml` playbook that checks your quota limits creates a virtual instance if you have sufficient quotas. 

To create and run the playbook: 

1\. Initialize a new “create_vm” role template. 
 
```
ansible-galaxy init create_vm
```

2\. Create a new task file in the tasks directory. 
 
```
touch ./create_vm/tasks/check_quota.yaml
```

3\. Configure the task to check if you have enough quotas to create the instance.

<code-block>
--- 
- name: Check quota before create instance 
  register: returned_data 
  gcore.cloud.instance_quota_info: 
    api_key: "{{ <span style="color:#FF5913">your_api_key</span> }}" 
    region_name: "{{ <span style="color:#FF5913">region_name</span> }}" 
    project_id: "{{ <span style="color:#FF5913">project_id</span> }}" 
    flavor: "{{ <span style="color:#FF5913">flavor</span> }}" 
    names:  ['inst1'] 
    volumes: [ 
        {'size': "{{ size }}", 'source': 'image', 'type_name': "{{ type_name }}"}, 
    ] 
    interfaces: [ 
        {'type': 'external'} 
    ] 
 
- name: Needed quota 
  debug: 
    msg: "{{ returned_data.data }}" 
  when: returned_data.data != {} 
</code-block>

4\. Create another task file `touch ./create_vm/tasks/create_vm.yaml`. 

5\. Configure the task to create an instance. 

<code-block>
--- 
- name: Create instance from volume 
  register: created_vm 
  gcore.cloud.instance: 
    api_key: "{{ <span style="color:#FF5913">your_api_key</span> }}" 
    region_name: "{{ <span style="color:#FF5913">region_name</span> }}" 
    project_id: "{{ <span style="color:#FF5913">project_id</span> }}" 
    command: create 
    flavor: "{{ <span style="color:#FF5913">flavor</span> }}" 
    volumes: [{ 
        'source': 'image', 
        'image_id': "{{ <span style="color:#FF5913">image_id</span> }}", 
        'size': "{{ <span style="color:#FF5913">size</span> }}", 
        'boot_index': 0, 
    }] 
    interfaces: [{ 
        'type': 'external' 
    }] 
    keypair_name: "{{ <span style="color:#FF5913">keypair_name</span> }}" 
  when: returned_data.data == {} 
  
--- 
- name: Created VM Info 
  debug: 
    msg: "{{ created_vm.data }}" 
  when: created_vm is not skipped
</code-block>

6\. Add all required tasks to the `create_vm/tasks/main.yml` file:

<code-block>
--- 
# tasks file for create_vm 
- name: Check quotas to create VM 
  import_tasks: check_quota.yaml 
  
- name: Create VM 
  import_tasks: create_vm.yaml 
 
- name: create_log_file 
  file: 
    path: "{{ path_to_log }}{{ log_filename }}" 
    state: touch 
  
- name: save_log 
  blockinfile: 
    state: present 
    insertafter: EOF 
    dest: "{{ path_to_log }}{{ log_filename }}" 
    marker: "<!-- end_of_task_log -->" 
    content: 
      - "{{ returned_data }}" 
      - "{{ created_vm }}"
</code-block>

7\. Add any required variables to the `create_vm/vars/main.yml` file. For example:

<code-block>
api_key: "PUT_HERE_YOUR_API_KEY" 
region_name: "Frankfurt" 
project_id: "328787" 
flavor: "g2-standard-1-2" 
size: 10 
type_name: "ssd_hiiops" 
image_id: "e72903b6-9b45-463f-834e-7316f7f3ff37" 
keypair_name: "id.rsa" 
path_to_log: "/var/log/" 
log_filename: "create_vm.log" 
</code-block>

8\. Create a playbook `test.yaml` to test the “create_vm” role. 

<code-block>
- hosts: localhost 
  become: true 
  vars: 
    ansible_python_interpreter: /usr/bin/python3.11 
  roles: 
    - create_vm 
</code-block>

9\. Run the playbook: `ansible-playbook test.yaml`.

You should get one of the following outputs:

* If everything is set up correctly, a new virtual instance will be created.  
 
* The information about your instance will appear in the ”Created VM Info” task section, and it’ll also be written to the log file. 

* If you don’t have sufficient quotas, you’ll get the “Needed quota” output, followed by the list of your current and requested quota limits. 
This information will also be stored in logs. 

* If you made a mistake in variables (for example, set a wrong flavor), you’ll get the “Failed” error. In this case, double-check the playbook configuration and rerun it.