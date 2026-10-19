```
A-1-BR#show run
Building configuration...

*Sep 22 12:20:12.562: %SYS-5-CONFIG_I: Configured from console by console
Current configuration : 1720 bytes
!
! Last configuration change at 12:20:12 UTC Tue Sep 22 2026
!
version 15.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname A-1-BR
!
boot-start-marker
boot-end-marker
!
aqm-register-fnf
!
!
no aaa new-model
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
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
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
redundancy
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
 description -=Internet;e0/0=-
 ip address 203.0.113.10 255.255.255.0
 ip nat outside
 ip virtual-reassembly in
!
interface Ethernet0/1
 description -=A-SW-CORE;e1/0=-
 ip address 10.150.111.254 255.255.255.252
 ip nat inside
 ip virtual-reassembly in
!
interface Ethernet0/2
 description -=B-1-BR;e0/1=-
 ip address 172.16.1.1 255.255.255.252
 ip nat inside
 ip virtual-reassembly in
!
interface Ethernet0/3
 description -=C-1-BR;e0/1=-
 ip address 172.17.5.25 255.255.255.248
 ip nat inside
 ip virtual-reassembly in
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip nat inside source list 1 interface Ethernet0/0 overload
ip nat inside source static 10.150.105.10 203.0.113.20
ip route 0.0.0.0 0.0.0.0 203.0.113.1
ip route 10.150.104.0 255.255.248.0 10.150.111.253
ip route 192.168.5.64 255.255.255.192 172.16.1.2
ip route 192.168.88.192 255.255.255.224 172.17.5.26
!
!
!
access-list 1 permit 10.150.104.0 0.0.7.255
access-list 1 permit 192.168.5.64 0.0.0.63
access-list 1 permit 192.168.88.192 0.0.0.31
access-list 1 permit 172.16.0.0 0.15.255.255
!
control-plane
!
!
!
!
!
!
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input none
!
!
end

A-1-BR#
```