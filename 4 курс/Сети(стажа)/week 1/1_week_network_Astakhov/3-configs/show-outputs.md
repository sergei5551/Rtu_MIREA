```
SW-CORE#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/2, Et0/3
10   USERS                            active
20   SERVERS                          active
99   MGMT                             active
999  PARKING                          active
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
1004 fddinet-default                  act/unsup
1005 trnet-default                    act/unsup
SW-CORE#show interfaces trunk

Port        Mode             Encapsulation  Status        Native vlan
Et0/0       on               802.1q         trunking      999
Et0/1       on               802.1q         trunking      999

Port        Vlans allowed on trunk
Et0/0       2-4094
Et0/1       2-4094

Port        Vlans allowed and active in management domain
Et0/0       10,20,99,999
Et0/1       10,20,99,999

Port        Vlans in spanning tree forwarding state and not pruned
Et0/0       10,20,99,999
Et0/1       10,20,99,999
SW-CORE#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       -=SW-1-AS;e0/0=-
Et0/1                          up             up       -=SW-2-AS;e0/0=-
Et0/2                          up             up
Et0/3                          up             up
Vl10                           up             up       gateway workstations
Vl20                           up             up       gateway servers
Vl99                           up             up       gateway control equipment
SW-CORE#show ip interfaces brief
                         ^
% Invalid input detected at '^' marker.

SW-CORE#show ip interface
SW-CORE#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up
Ethernet0/1            unassigned      YES unset  up                    up
Ethernet0/2            unassigned      YES unset  up                    up
Ethernet0/3            unassigned      YES unset  up                    up
Vlan10                 10.150.104.1    YES NVRAM  up                    up
Vlan20                 10.150.105.1    YES NVRAM  up                    up
Vlan99                 10.150.110.1    YES NVRAM  up                    up
SW-CORE#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
C        10.150.104.0/24 is directly connected, Vlan10
L        10.150.104.1/32 is directly connected, Vlan10
C        10.150.105.0/24 is directly connected, Vlan20
L        10.150.105.1/32 is directly connected, Vlan20
C        10.150.110.0/24 is directly connected, Vlan99
L        10.150.110.1/32 is directly connected, Vlan99
SW-CORE#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    aabb.cc00.0100    DYNAMIC     Et0/1
  20    aabb.cc00.0100    DYNAMIC     Et0/1
  99    aabb.cc00.0100    DYNAMIC     Et0/1
 999    aabb.cc00.0100    DYNAMIC     Et0/1
Total Mac Addresses for this criterion: 4
SW-CORE#

```