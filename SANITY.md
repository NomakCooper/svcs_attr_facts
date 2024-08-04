### ANSIBLE SANITY TEST
#### Sanity test on CentOS Stream release 9 Ansible Control Node.

```shell
[root@ansiblecn ~]# uname -r
5.14.0-480.el9.x86_64

[root@ansiblecn ~]# cat /etc/redhat-release
CentOS Stream release 9

[root@ansiblecn ~]# ansible --version
ansible [core 2.15.12]
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /root/.local/lib/python3.9/site-packages/ansible
  ansible collection location = /root/.ansible/collections:/usr/share/ansible/collections
  executable location = /root/.local/bin/ansible
  python version = 3.9.19 (main, Jul 18 2024, 00:00:00) [GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] (/usr/bin/python3)
  jinja version = 3.1.4
  libyaml = True
```

```shell
[root@ansiblecn general]# ansible-test sanity --docker -v plugins/modules/svcs_attr_facts.py
Configured locale: en_US.UTF-8
Run command: podman -v
Detected "podman" container runtime version: podman version 5.1.2
Run command: podman system connection list --format=json
Run command: podman info --format '{{ json . }}'
Run command: podman version --format '{{ json . }}'
Container runtime: podman client=5.1.2 server=5.1.2 cgroup=v2
Assuming Docker is available on localhost.
Run command: podman image inspect quay.io/ansible/ansible-test-utility-container:2.0.0
Run command: podman run --volume /sys/fs/cgroup:/probe:ro --name ansible-test-probe-8Kl8uCCG --rm quay.io/ansible/ansible-test-utility-container:2.0.0 sh -c 'audit-status && cat /proc/sys/fs/nr_open && ulimi ...
Container host audit status: EPERM (-1)
Container host max open files: 1048576
Container loginuid: 0
Starting new "ansible-test-controller-8Kl8uCCG" container.
Run command: podman image inspect quay.io/ansible/default-test-container:7.14.0
Run command: podman network inspect podman
Run command: podman run --tmpfs /tmp:exec --tmpfs /run:exec --tmpfs /run/lock --cap-add SYS_CHROOT --cap-add AUDIT_WRITE --systemd always --cgroupns private -dt --ulimit nofile=10240 --name ansible-test-cont ...
Adding "ansible-test-controller-8Kl8uCCG" to container database.
Run command: podman container inspect ansible-test-controller-8Kl8uCCG
Stream command with data: podman exec -i ansible-test-controller-8Kl8uCCG /bin/sh
Loaded configuration: tests/config.yml
Scanning collection root: /root/dev/ansible_collections
Including collection: community.general (3176 files)
Creating a payload archive containing 4122 files...
Created a 4011576 byte payload archive containing 4122 files in 0 seconds.
Run command with stdin: podman exec -i ansible-test-controller-8Kl8uCCG tar oxzf - -C /root
Creating container database.
Stream command: podman exec ansible-test-controller-8Kl8uCCG /usr/bin/env ANSIBLE_TEST_CONTENT_ROOT=/root/ansible_collections/community/general LC_ALL=en_US.UTF-8 /usr/bin/python3.11 /root/ansible/bin/ansibl ...
Configured locale: en_US.UTF-8
Parsing container database.
Read 11 sanity test ignore line(s) for Ansible 2.15 from: tests/sanity/ignore-2.15.txt
Running sanity test "action-plugin-docs"
Initializing "/tmp/ansible-test-7fh6upmv-injector" as the temporary injector directory.
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/action-plugin-docs.py
Running sanity test "ansible-doc"
Run command: ansible-doc -t module community.general.svcs_attr_facts
Run command: ansible-doc -t module --json community.general.svcs_attr_facts
Running sanity test "changelog"
No tests applicable.
Running sanity test "compile" on Python 2.7
Run command with data: /usr/bin/python2.7 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "compile" on Python 3.5
Run command with data: /usr/bin/python3.5 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "compile" on Python 3.6
Run command with data: /usr/bin/python3.6 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "compile" on Python 3.7
Run command with data: /usr/bin/python3.7 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "compile" on Python 3.8
Run command with data: /usr/bin/python3.8 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "compile" on Python 3.9
Run command with data: /usr/bin/python3.9 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "compile" on Python 3.10
Run command with data: /usr/bin/python3.10 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "compile" on Python 3.11
Run command with data: /usr/bin/python3.11 /root/ansible/test/lib/ansible_test/_util/target/sanity/compile/compile.py
Running sanity test "empty-init"
No tests applicable.
Running sanity test "future-import-boilerplate"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/future-import-boilerplate.py
Running sanity test "ignores"
Running sanity test "import" on Python 2.7
Run command: /usr/bin/python2.7 -m virtualenv --version
Run command with data: importer.py
Running sanity test "import" on Python 3.5
Run command with data: importer.py
Running sanity test "import" on Python 3.6
Run command with data: importer.py
Running sanity test "import" on Python 3.7
Run command with data: importer.py
Running sanity test "import" on Python 3.8
Run command with data: importer.py
Running sanity test "import" on Python 3.9
Run command with data: importer.py
Running sanity test "import" on Python 3.10
Run command with data: importer.py
Running sanity test "import" on Python 3.11
Run command with data: importer.py
Running sanity test "line-endings"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/line-endings.py
Running sanity test "metaclass-boilerplate"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/metaclass-boilerplate.py
Running sanity test "no-assert"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-assert.py
Running sanity test "no-basestring"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-basestring.py
Running sanity test "no-dict-iteritems"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-dict-iteritems.py
Running sanity test "no-dict-iterkeys"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-dict-iterkeys.py
Running sanity test "no-dict-itervalues"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-dict-itervalues.py
Running sanity test "no-get-exception"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-get-exception.py
Running sanity test "no-illegal-filenames"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-illegal-filenames.py
Running sanity test "no-main-display"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-main-display.py
Running sanity test "no-smart-quotes"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-smart-quotes.py
Running sanity test "no-unicode-literals"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/no-unicode-literals.py
Running sanity test "pep8"
Run command: /root/.ansible/test/venv/sanity.pep8/3.11/0a3ec4c3/bin/python -m pycodestyle --max-line-length 160 --config /dev/null --ignore E203,E402,E741,W503,W504 plugins/modules/svcs_attr_facts.py
Running sanity test "pslint"
No tests applicable.
Running sanity test "pylint"
Run command: /root/.ansible/test/venv/sanity.pylint/3.11/0b767470/bin/python /root/ansible/test/lib/ansible_test/_util/controller/tools/collection_detail.py /root/ansible_collections/community/general
Checking 1 file(s) in context "modules" with config: /root/ansible/test/lib/ansible_test/_util/controller/sanity/pylint/config/collection.cfg
Run command: /root/.ansible/test/venv/sanity.pylint/3.11/0b767470/bin/python -m pylint --jobs 0 --reports n --max-line-length 160 --max-complexity 20 --rcfile /root/ansible/test/lib/ansible_test/_util/contro ...
Running sanity test "replace-urlopen"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/replace-urlopen.py
Running sanity test "runtime-metadata"
No tests applicable.
Running sanity test "shebang"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/shebang.py
Running sanity test "shellcheck"
No tests applicable.
Running sanity test "symlinks"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/symlinks.py
Running sanity test "use-argspec-type-path"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/use-argspec-type-path.py
Running sanity test "use-compat-six"
Run command with data: /root/.ansible/test/venv/sanity/3.11/4f53cda1/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/code-smell/use-compat-six.py
Running sanity test "validate-modules"
Run command: /root/.ansible/test/venv/sanity.validate-modules/3.11/1f621867/bin/python /root/ansible/test/lib/ansible_test/_util/controller/tools/collection_detail.py /root/ansible_collections/community/general
Run command: /root/.ansible/test/venv/sanity.validate-modules/3.11/1f621867/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/validate-modules/validate.py --format json --arg-spec --coll ...
Running sanity test "yamllint"
Run command with data: /root/.ansible/test/venv/sanity.yamllint/3.11/61ebfb13/bin/python /root/ansible/test/lib/ansible_test/_util/controller/sanity/yamllint/yamllinter.py
Run command with stdout: podman exec -i ansible-test-controller-8Kl8uCCG sh -c 'tar cf - -C /root/ansible_collections/community/general/tests --exclude .tmp output | gzip'
Run command with stdin: tar oxzf - -C /root/dev/ansible_collections/community/general/tests
Run command: podman stop --time 0 ansible-test-controller-8Kl8uCCG
Run command: podman rm ansible-test-controller-8Kl8uCCG
```
