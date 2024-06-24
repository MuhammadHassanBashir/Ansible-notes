Introduction
------------

All ansible play book will be written in YAML.

Configuration and Basic Concepts
--------------------------------

jb ap ansible install kerty hn tu y config file create kerti ha "/etc/ansible/ansible.cfg"  --> default location of ansible configuration file.

configuration file is divided into several section.

ansible.cfg
-----------

[default]

inventory          =  /etc/ansible/hosts
log_path           =  /var/log/ansible.log 

library            =  /usr/share/my_modules/
roles_path         =  /etc/ansible/roles
action_plugins     =  /usr/share/ansible/plugins/action

gathering          =  implicit

#SSH timeout       
timeout            =  10   --> ssh timeout
forks              =  5    ---> how many host should ansible target at a time when execute ansible playbook.

[inventory]        ---> enabling certain plugins

enable_plugins     = host_list, virtualbox, yaml, constructed

[privilege_escalaton]

[paramiko_connnection]

[ssh_connection]

[persistent_connnection]

[colors]


- ab sir kha rhy hn k let say k apki ansible host machine ma different directory ma differnt play books hn like for (web , database , network)

  ab ap sab playbooks k lye configuration ko apny according set kerna chahty hn tu isk lye ap ansible ki default configuration file(/etc/ansible/ansible.cfg) ki copy us us directory ma rakhty jis jis directory ma apki play book ha or apny playbook ma jo ap change dekhna chahty hn usky according ansible ki configuration file ma changes implement ker dye.. 

  usky bd jb ap play ko run kery gye tu wo apny directory ma majood ansible ki configuration file sa value pick ker ka implement kery gi..  "this is a one way"

- ab sir khty hn k ap na playbook ki directory ma ansible ki configuration file ko ni rakh bilky kisi or directory(/opt/ansible-web.cfg) ma rakh hn tu ap playbook run kerny sa phily "enviroment varible" k through is file ka playbook ko btye gye.. tky wo configuration file sa value pick ker usky us new directory sa...

"$ANSIBLE_CONFIG=/opt/ansible-web.cfg ansible-playbook playbook.yaml"

- ab sir khty hn k let say ap na default ansible configuration file ko playbook ki directory ma b rakha ha or kisi or directory ma b rakh ker ansible playboook ma enviromental variables k through call b kerwa rhy hn file ma. tu ansible "priorty" kis ko dye ga... "enviromental variable k through jis ansible ki default configuration file jo kisi b directory ma pari ha ko playbook ma call krway hoga ansible usko priorty dye ga " 

playbook priority chain:

1- wo env k through called configuration file ko first priorty dye ga or values ko yha sa pick kery ga..
2- isky bd wo playbook ki directory ma pari configuration file ko priority dye ga or remaining other values ko pick kery ga jo playbook ma env sa called file sa ni mili
3- then ".ansible.cfg" ko priorty dye ga..
4- /etc/ansible/ansible.cfg ko priorty dye ga..


let us now look values within files itself...

-  ab sir khty hn k let sa hum na aik playbook storage k lye create ki ha. jb hum isko run kery gye tu ansible phily "default configuration file" ko playbook ki directory ma find kerta ha value pick kerny k lye ab jb waha file ni milti tu wo default path "/etc/ansible/ansible.cfg" sa values pick kerta ha.. ab sir khty hn k let say ap na values sari file ko waha sa copy ni kerwana sirf aik parameter ko lena ha tu isky lye ap kya kro gye...

   "jis parameter ko ap na file sa lena ha ap usko CAPITAL ma _ ansible k sath playbook run kerty time likh sakhty hn" tu wo sirf aik value ko hi file sa ley rha hoga...


   let sa ansible ki configuration file sa hum sirf "gathering   = implicit" lena ha tu ap playbook run kerty time isko ko capital ma _ ansible ka sath lye gye tu wo playbook k lye wohi sirf value configuration file sa ley rha hoga,,

   like: ASNIBLE_GATHERING = explicit(i have used explicit instead of implicit because i make it off..)

   "remember koi b value ap asy do gye "it takes the higer precedence(mean isko sab sa zayada priorty mily gi...) is k against is k lye other configuration file ma pari values ignore hojye gi..""

    running playbook "ASNIBLE_GATHERING = explicit ansible-playbook playbook.yml"   ->> mean playbook run kerty time CAPITAL ma asy ap values ko configuration file sa pick kerwa sakhty hn.. "but you can use it to run for single playbook"

    agr ap shell ma y active ker na chahty hn tu ap isko export k through ker sakhty hn like 
    "export ASNIBLE_GATHERING = explicit"
    "ansible-playbook playbook.yml"

Command to veiw Configuration:
------------------------------

    "ansible-config list"  ->>list all configuration

    with this you can see all different configuration their default values and values you can set 

command to see the config file that currently active:
------------------------------------------

    "ansible-config view"  --> sir khty hn k different playbook system ma hoti hn. ap is command ka through dekh sakhty hn k kon si playbook "active" ha,.


command to show the current setting
-----------------------------------

    ab sir khty hn k hum na learn kya ha k ansible apny priorty k according values ko files sa pick kerta ha.. what if k apko ni horha k ansible currently kya value pick ker rha ha. tu wo ap is command sa dekh sakhty hn
    
    "ansible-config dump"  --> it will show you the list ko current setting that ansible picked up.. and where it pick that from.. (mean kya or kha sa value pick ki hn)

     e.g export ANSIBLE_GATHERING = explicit
         ansible-config dump | grep gathering

         RESULT: DEFAULT_GATHERING(env:ANSIBLE_GATHERING) = explicit

         it is use full when you are troubleshooting issue.   


UNDERSTANDING YAML
------------------

key Value pair:
--------------

Fruit: Apple
Vegetable: Carrot
Meat:  Chicken

Array/lists
-----------

Fruits:
-   Orange
-   Apple
-   Banana

Vegetables:
-   Carrot
-   Cauliflower
-   Tomato

Dictionary/MAP
------------

Banana:
    Calories: 105
    Fat: 0.4g  
Grapes:
    Calories: 105
    Fat: 0.4g  

further sa further detail k lye hum Dictionary use kerty hn.

remember: Dictionary are "Unordered" format ma b 2nd Dictionary k eqaul hosakhty hn unless k values same na ho.
          array are "ordered" foramt ma hi 2nd array k equal hoti hn. 


Ansible Inventory
-----------------

we will now look at configuring ansible inventory..

ansible aik waqt ma multiple server k sath kam ker rha hota ha. is k lye ansible ko multiple server k sath connectivity established kerna hoti ha.. y connectivity ap "linux ma ssh k through established ker skahty hn" or "windows ma powershell k through"

y cheez ansible ko agentless bnati ha. mean k apko ansible k lye koi agent targeted machine ma dalny ki zaroort ni hoti...

"so targeted machine k lye information "inventory file" ma store hoti ha" . default inventory file ki location "/etc/ansible/hosts" hoti ha. agr ap new inventory file ko create ni kerty tu ansible default inventory file ko use kery ga...

inventory file "ini" k format ma hoti hn. ap inventory file ma single or group machines k lye information dye sakhty hn..

inventory file
--------------

server1.company.com
server2.company.com

[mail]  ---> for group
server3.company.com
server4.company.com

[db]
server5.company.com
server6.company.com

[web]
server7.company.com
server8.company.com

more on inventory files:
-----------------------

web  ansible_host=server1.company.com
db   ansible_host=server2.company.com
mail ansible_host=server3.company.com
web2 ansible_host=server4.company.com
   
ab sir na btya ha k is tarha sa ap alise create ker sakhty hn. "mean targeted machine ka address k against name". so ap easily name ko use ker sakhty hn for calling or applying ansible playbook to the targeted machine. like we have use (web name for server1 ) 

and "ansible_host" -->  y inventory parameter ha. jo k FQDN(domain) or ip address k lye use hota ha (targeted server k)

"ansible k lye other inventory parameters b hoty hn" 

like:
----

ansible_connection- ssh/winrm/localhost  --> ansible connection define how ansible connect to the targeted server..
ansible_port- 22/5986   ---> it defines which port to connect to. mean ansible targeted machine ki kis port per connectionn established kery ga. or phir waha per playbook run keryga ..
ansible_user- root/admistrator  --> it define ssh user for linux(targeted machine)
ansible_ssh_pass- password    ----> it define ssh password for linux(targeted machine) 


web  ansible_host=server1.company.com ansible_connection=ssh   ansible_user=root
db   ansible_host=server2.company.com ansible_connection=winrm  ansible_user=admin
mail ansible_host=server3.company.com ansible_connection=ssh    ansible_ssh_pass=p@Ss   --> not that is tarha sa plain password dena sahi ni ha.. you need to create key base password b/w server. "for security we can use "Ansible vault""
web2 ansible_host=server4.company.com ansible_connection=winrm

localhost ansible_connection=localhost


"ansible_connection" --> ansible connection define how ansible connect to the targeted server..
"ansible_connection=localhost" --> we will also set to localhost indicate that not connect to remote host.


Different inventory format
--------------------------

2 inventory format will be using for ansible.

1- ini       --------> it will use for simple structure(mean for less complex work)
2- YAML       --------> it will use for complex structure(mean for complex work)  it is more structured and flexible then the INI format. 

This is INI format
------------------

web  ansible_host=server1.company.com ansible_connection=ssh   ansible_user=root
db   ansible_host=server2.company.com ansible_connection=winrm  ansible_user=admin
mail ansible_host=server3.company.com ansible_connection=ssh    ansible_ssh_pass=p@Ss   --> not that is tarha sa plain password dena sahi ni ha.. you need to create key base password b/w server. "for security we can use "Ansible vault""
web2 ansible_host=server4.company.com ansible_connection=winrm

localhost ansible_connection=localhost

This is YAML format
-------------------

all:
   children:
      webservers:
         hosts:
            web1.example.com:
            web2.example.com:
      dbservers:
         hosts:
            db1.example.com:           
            db2.example.com:   

"Note: For Linux based hosts, use ansible_ssh_pass parameter and for Windows based hosts, use ansible_password parameter.
|
Solution
------------
# Sample Inventory File

# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Dbp@ss123!

Group
------

# Sample Inventory File

# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

# Database Servers
db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!


[web_servers]
web1
web2
web3

[db_servers]
db1

Group of the group
------------------

# Web Servers
web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

# Database Servers
db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!


[web_servers]  --> represent group
web1
web2
web3

[db_servers]   --> represent group
db1

[all_servers:children] -------> [parentgroup:childgroup]  --> represent group of the group
web_servers
db_servers

command to delete all stop container:
-------------------------------------
docker container prune -f


command to delete all container images:
--------------------------------------

docker image prune -a -f

Grouping and Parent-Child Relations
-----------------------------------

why we need Grouping..

let say k ap k multiple webservers hn. ab ap aik group create ker lety hn. us ma webserver ko add kerty hn. jb changing k wqt hoga tu ap group ma changes kery gye jo k webservers per implement hogjye gi..

"In INI format groups are define using "[]" and parent and child relation are define using ":" [parent:child]"

"In YAML format groups are define using keyword "hosts" and parent and child relation are define using keyword "children""

YAML format
-----------

all:
   children:        --------> representing parent(parent and child relation are define using keyword "children)--> for group of group
      webservers:   --------> parent name
        children:   --------> parent k childs.
           webservers_us:    --------> group name
              hosts:       --------> representing groups in YAML
                server1_us.com: ---> group members(alis name)
                        ansible_host: 192.168....
                server2_eu.com:  ---> group members(alis name)
                        ansible_host: 192.168....

           webservers_eu:  --------> group name
              hosts:       --------> representing groups in YAML
                server1_us.com:   ---> group members(alis name)
                        ansible_host: 192.168....
                server2_eu.com:   ---> group members(alis name)
                        ansible_host: 192.168.... 
Variable
--------

    1- It is use to store information that varies with each host.
    2- it's the variable that stores information about the user, host and password. that are different for each server..

web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

ansible_host , ansible_password , ansible_connection all are sample of variable....

playbook ma b hum variables ko add ker sakhty hn.. 

playbook.yml
------------

-   
    name: Add DNS server to resolv.conf
    hosts: localhost
    vars:   ---> defining variables
        dns_server: ip-address
    tasks:
        -  lineinfile:
                path: /etc/resolv.conf
                line: "nameserver {{dns_server}}"  ---> it is a way to use variable in ansible.


more example:

let say we have playbook for openport from firewall.

    -   
        name: Set firewall Configuration
        hosts: web
        tasks:
         - firewalld:
             service: https
             parmanant: true
             stats: enabled

           firewalld:
             service: '{{ http_port }}'/tcp        ---> assigning variable
             parmanant: true
             stats: disabled

           firewalld:
             service: '{{ snmp_port }}'/udp       ---> assigning variable
             parmanant: true
             stats: disabled

           firewalld:
             service: '{{ inter_ip_range }}'/24  ---> assigning variable (mean calling the variable from inventory file or variable file)
             Zone: internal
             stats: enabled 
           


you can define variables in "inventory file" and "variable file"

inventory file:
--------------

#Sample Inventory file   ----> defining variables

    web http_port=8081 snmp_port=161-162 inter_ip_range=192.0.2.0    ----> defining variables

#Sample variable file  ---named web.yml   ----> defining variables

    http_port: 8081
    snmp_port: 161-162
    inter_ip_range: 192.0.2.0       ----> defining variables







this format of using variable to playbook is called "jinja2 Templating"


"hum "variables" name ki file ma variables ko define kerty hn"
like: 

    variable1: value1
    variable2: value2


Variable TYPE
-------------

- String variable 

    1- String variables in ansible are sequences of characters.
    2- They can be defined in a playbook inventory, or passed as command line arguments.
    
    like: username: "admin" 

- Number Variables 

    1- Number variables in ansible can hold integer or floating-point values.
    2- They can be used in mathematical operations.

    like: max_connections: 100

- Boolean Variables

    1- Boolean variables in ansible can hold either true or false.
    2- They are often used in conditional statements.

    like: debug_mode: true

    valid values: True , 'true' , 't', 'yes', 'y', 'on', '1', 1 , 1.0 
    Description: Truthy values
    valid values: False, 'false', 'f', 'no', 'n', 'off', '0', 0, 0.0
    Description: falsy values