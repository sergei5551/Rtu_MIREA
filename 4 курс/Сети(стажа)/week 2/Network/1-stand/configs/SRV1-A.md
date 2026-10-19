```
Web#show run
Building configuration...

Current configuration : 965 bytes
!
version 15.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname Web
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
no ip routing
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
no ip cef
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
 ip address 10.150.105.10 255.255.255.0
 no ip route-cache
!
interface Ethernet0/1
 no ip address
 no ip route-cache
 shutdown
!
interface Ethernet0/2
 no ip address
 no ip route-cache
 shutdown
!
interface Ethernet0/3
 no ip address
 no ip route-cache
 shutdown
!
ip default-gateway 10.150.105.1
ip forward-protocol nd
!
!
ip http server
no ip http secure-server
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

Web#
```