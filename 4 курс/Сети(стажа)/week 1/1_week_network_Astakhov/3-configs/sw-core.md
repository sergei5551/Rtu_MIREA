```
SW-CORE#show running-config
Building configuration...

Current configuration : 1698 bytes
!
! Last configuration change at 00:34:37 UTC Mon Sep 14 2026
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW-CORE
!
boot-start-marker
boot-end-marker
!
!
enable secret 8 $8$jyGsQNUjHanzTx$4I./nYSUcDecCbw4sDrnrXmIW0b/92CnQCWEw3E5l92
!
username itcore secret 8 $8$ib7y8XZSc32kwx$F9j8nMbTcNtDboetpUyCdp98aIpaBuQO5iXKFie/n8.
no aaa new-model
!
!
!
!
!
!
!
!
ip domain-name skills.local
ip cef
no ipv6 cef
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
description -=SW-1-AS;e0/0=-
switchport trunk allowed vlan 2-4094
switchport trunk encapsulation dot1q
switchport trunk native vlan 999
switchport mode trunk
switchport nonegotiate
!
interface Ethernet0/1
description -=SW-2-AS;e0/0=-
switchport trunk allowed vlan 2-4094
switchport trunk encapsulation dot1q
switchport trunk native vlan 999
switchport mode trunk
switchport nonegotiate
!
interface Ethernet0/2
!
interface Ethernet0/3
!
interface Vlan10
description gateway workstations
ip address 10.150.104.1 255.255.255.0
!
interface Vlan20
description gateway servers
ip address 10.150.105.1 255.255.255.0
!
interface Vlan99
description gateway control equipment
ip address 10.150.110.1 255.255.255.0
!
ip forward-protocol nd
!
ip http server
ip http secure-server
!
ip ssh version 2
ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
!
!
!
!
!
control-plane
!
!
line con 0
logging synchronous
line aux 0
line vty 0 4
login local
transport input ssh
!
!
!
end
```
