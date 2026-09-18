```
SW-1-AS#sh run
Building configuration...

Current configuration : 1413 bytes
!
! Last configuration change at 00:53:36 UTC Mon Sep 14 2026
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW-1-AS
!
boot-start-marker
boot-end-marker
!
!
enable secret 8 $8$cg77kWnklB20nB$fxk353NmYZaJrCg5hZsRj1/8dNXvln8gZrKZ5cJ4U8k
!
username itcore secret 8 $8$oV2tAL1jqqY2sh$8YdOkbRRSZijLsDtjFCXrs.FEoAhQ9pCYScVw5hANRw
no aaa new-model
!
!
!
!
!
no ip routing
!
!
!
ip domain-name skills.local
no ip cef
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
 description -=SW-CORE;e0/0=-
 switchport trunk allowed vlan 2-4094
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 999
 switchport mode trunk
 switchport nonegotiate
!
interface Ethernet0/1
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/3
!
interface Vlan99
 ip address 10.150.110.11 255.255.255.0
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