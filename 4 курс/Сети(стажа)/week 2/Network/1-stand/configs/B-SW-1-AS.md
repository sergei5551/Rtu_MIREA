```
B-SW-1-AS#show run
Building configuration...

Current configuration : 1182 bytes
!
! Last configuration change at 11:37:22 UTC Tue Sep 22 2026
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname B-SW-1-AS
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
 ip address 192.168.5.98 255.255.255.240
 no ip route-cache
!
ip default-gateway 192.168.5.97
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

B-SW-1-AS#
```