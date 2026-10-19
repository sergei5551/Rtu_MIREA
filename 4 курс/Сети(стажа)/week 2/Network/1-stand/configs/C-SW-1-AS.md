```
C-SW-1-AS#
*Sep 22 12:27:03.933: %SYS-5-CONFIG_I: Configured from console by console
C-SW-1-AS#show run
Building configuration...

Current configuration : 1186 bytes
!
! Last configuration change at 12:27:03 UTC Tue Sep 22 2026
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname C-SW-1-AS
!
boot-start-marker
boot-end-marker
!
!
!
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
 switchport trunk allowed vlan 2-4094
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 999
 switchport mode trunk
 switchport nonegotiate
 duplex full
!
interface Ethernet0/1
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/2
 shutdown
!
interface Ethernet0/3
 shutdown
!
interface Vlan99
 ip address 192.168.88.210 255.255.255.248
 no ip route-cache
!
ip default-gateway 192.168.88.209
ip forward-protocol nd
!
ip http server
ip http secure-server
!
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
 login
!
!
!
end

C-SW-1-AS#
```