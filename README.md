In the backup playbook i just change the name of the file path as I go per lab. 
Here is the topology.

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/c9b2258b-46e2-4e76-971d-21940e722e47)

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/5ed2c128-2247-44a1-ac61-2f6f078328cd)

I am only doign the MESH lab guiides. 

Speicifically:
Routing ATD - Mesh Topology - Full ISIS-SR and EVPN Lab Guide
Routing ATD - Mesh Topology - Full LDP and IP-VPN Lab Guide

From my understainding the difference of SR and VPN between LDP and IP-VPN are:

The difference between Segment Routing (SR) and Label Distribution Protocol (LDP) in the context of providing VPN services like IP-VPN involves the underlying technology used for label distribution and path determination within an MPLS network.

Segment Routing (SR):

Path Control: SR allows for more granular path control. The path a packet will take through the network is encoded in the packet header as a list of segments by the source router. This is often referred to as source routing.
Simplification: It simplifies the network by reducing the amount of state information required on each router because the path is determined at the edge of the network.
Traffic Engineering: SR naturally integrates with traffic engineering because it can steer traffic through a specified path without requiring additional protocols like RSVP-TE.
Scalability: As networks grow, SR scales better because it doesn't require a full mesh of LDP sessions between routers.
Fast Reroute: SR supports fast reroute capabilities like TI-LFA, making the network more resilient to failures.
Label Distribution Protocol (LDP):

Label Distribution: LDP is used specifically for the distribution of labels in an MPLS network. It operates by creating a session between neighboring nodes and exchanging label binding information for reachable routes.
Network State: With LDP, each router in the network needs to maintain label information for each reachable destination, which can increase the amount of state maintained in larger networks.
Traffic Engineering: While LDP can be used in conjunction with traffic engineering, it typically requires additional protocols like RSVP-TE (Resource Reservation Protocol-Traffic Engineering) to set up explicit traffic-engineered paths.
Full Mesh Requirement: In some VPN implementations, LDP requires a full mesh of peerings to distribute labels, which can be cumbersome to manage in large-scale deployments.
When comparing SR with LDP in the context of VPN services:

SR for VPNs: VPNs can leverage SR for more efficient routing and path selection. SR can be used to influence the path traffic takes through the network and can be particularly useful in Segment Routing MPLS (SR-MPLS) VPNs.

IP-VPN with LDP: In traditional IP-VPNs, LDP is used alongside protocols like MP-BGP to distribute VPN labels for MPLS VPN services. Each router must learn the labels for the VPN routes, which can require more overhead and complex configurations as the network scales.

In summary, SR offers a more modern and scalable approach that integrates well with traffic engineering and simplifies the management of paths through the network. In contrast, LDP is an older protocol that works well for distributing labels but may require additional complexity for traffic engineering and can be less scalable in large networks.

My expelantions on the topics of the demo:
Deploy IS-IS as the Service Provider Underlay IGP:

IS-IS (Intermediate System to Intermediate System): This is a routing protocol used to determine the best path for data through a network of routers. In the context of a service provider, IS-IS is often used as the underlay network, meaning it's the foundational routing protocol that runs beneath other services, providing basic connectivity and route information.
Establish MPLS Transport Label Distribution via Segment-Routing:

MPLS (Multi-Protocol Label Switching): A method for speeding up and shaping traffic flows across enterprise and service provider networks.
Segment Routing (SR): An MPLS-based forwarding paradigm that simplifies routing, reduces state held on routers, and offers enhanced traffic engineering capabilities by encoding paths as sequences of "segments", which are pre-defined paths or instructions.
Prepare to Offer VPN Services to Customers via MP-BGP EVPN Control-Plane:

MP-BGP (Multi-Protocol Border Gateway Protocol): An extension of BGP that supports multiple address families (like unicast, multicast, VPN) and is used to exchange routing information in large and interconnected networks.
EVPN (Ethernet VPN): A BGP-based control plane for Ethernet traffic that allows for scalable Layer 2 VPN services.


Deploy L3VPN Service for Customer-1:
L3VPN (Layer 3 Virtual Private Network): This service uses BGP to distribute VPN routing information across the provider's backbone, allowing for separation between different customers' networks on the same physical infrastructure.

Deploy L2VPN Service for Customer-2:
L2VPN (Layer 2 Virtual Private Network): This provides a point-to-point or point-to-multipoint service over the service provider's network, extending a customer's LAN and its Layer 2 traffic between geographically separate sites.

Deploy E-LINE Service for Customer-3:
E-LINE: A type of Ethernet VPN that provides a point-to-point Ethernet virtual connection between two customer sites, often used for dedicated capacity and privacy.

Enable TI-LFA Fast Reroute for ISIS-SR:
TI-LFA (Topology Independent Loop-Free Alternate): A fast reroute mechanism that provides protection against link or node failures in the network by pre-computing backup paths.
ISIS-SR (IS-IS with Segment Routing): This combines traditional IS-IS routing with the traffic engineering capabilities of Segment Routing.

Leverage SR-TE to Steer VPN Traffic:
SR-TE (Segment Routing Traffic Engineering): Allows network operators to define paths through the network that can optimize and steer traffic based on specific requirements or constraints, used particularly for efficient and optimized VPN traffic handling.


Offer Centralized Services to L3VPN Customers:
Centralized services could include centralized internet access, cloud services, or other shared resources that L3VPN customers can utilize without the need to deploy them individually for each customer, often leading to cost savings and easier management.
