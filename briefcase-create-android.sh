#!/bin/bash

command="sudo chmod 755"

$command /home/interceptx/.briefcase/tools/jdk8u242-b08/jre/lib/cmm/*.pf
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/jre/lib/currency.data
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/jre/lib/management/jmxremote.password.template
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/jre/lib/management/snmp.acl.template
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/jre/LICENSE
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/jre/ASSEMBLY_EXCEPTION
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/jre/THIRD_PARTY_README
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/ASSEMBLY_EXCEPTION
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/LICENSE
$command /home/interceptx/.briefcase/tools/jdk8u242-b08/THIRD_PARTY_README
briefcase create android
