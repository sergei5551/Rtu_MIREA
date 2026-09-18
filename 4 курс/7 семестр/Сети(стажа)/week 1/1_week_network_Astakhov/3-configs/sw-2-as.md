```
SW-2-AS#sh run
Building configuration...

Current configuration : 1413 bytes
!
! Last configuration change at 00:55:57 UTC Mon Sep 14 2026
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW-2-AS
!
boot-start-marker
boot-end-marker
!
!
enable secret 8 $8$Y/4hVXS8HRGRNR$qPH43Kc4FIt3BPvRcnve6BwMzGdOYysmfcEek.uLOgY
!
username itcore secret 8 $8$3YRpKYYWFQLnYx$WpNQkXS7Tlzz4sXuBLvFSFGPBUACI2grYZ2tBCC1Qtc
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
 description -=SW-CORE;e0/1=-
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
 switchport access vlan 20
 switchport mode access
!
interface Ethernet0/3
!
interface Vlan99
 ip address 10.150.110.12 255.255.255.0
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