```
C-1-BR#show run
Building configuration...

Current configuration : 1475 bytes
!
! Last configuration change at 12:27:05 UTC Tue Sep 22 2026
!
version 15.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname C-1-BR
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
ip dhcp pool pool_address_192_168_88
 network 192.168.88.192 255.255.255.224
 default-router 192.168.88.193
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
 description -=C-SW-1-AS;e0/0=-
 no ip address
!
interface Ethernet0/0.10
 description USERS GATEWAY - SW-CORE
 encapsulation dot1Q 10
 ip address 192.168.88.193 255.255.255.240
!
interface Ethernet0/0.99
 description MNG GATEWAY - SW-CORE
 encapsulation dot1Q 99
 ip address 192.168.88.209 255.255.255.248
!
interface Ethernet0/1
 description -=A-1-BR;e0/3=-
 ip address 172.17.5.26 255.255.255.248
!
interface Ethernet0/2
 no ip address
 shutdown
!
interface Ethernet0/3
 no ip address
 shutdown
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip route 10.150.104.0 255.255.248.0 172.17.5.25
ip route 77.88.8.8 255.255.255.255 172.17.5.25
ip route 192.168.5.64 255.255.255.192 172.17.5.25
!
!
!
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

C-1-BR#
```