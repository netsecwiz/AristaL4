This is not the L4 class. This is an ATD instance for advanced routing I am using to supplement some of the L4 knowledge.<br>
**This is my 1st attempt at a decent looking readme. *<br>

In the backup playbook i just change the name of the file path as I go per lab. 
Here is the topology.

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/c9b2258b-46e2-4e76-971d-21940e722e47)

_**I am only doing the MESH lab guiides.**_<br>

Speicifically:<br>
**Routing ATD - Mesh Topology - Full ISIS-SR and EVPN Lab Guide**<br>
![image](https://github.com/netsecwiz/AristaL4/assets/123339313/8479682c-cdcd-4cae-a169-37b8a887b34d)<br>
**Routing ATD - Mesh Topology - Full LDP and IP-VPN Lab Guide**<br>
![image](https://github.com/netsecwiz/AristaL4/assets/123339313/908a4342-1fec-40c2-9793-37924a5976a1)<br>


From my understanding the difference of SR and VPN between LDP and IP-VPN are:<br>

**The difference between Segment Routing (SR) and Label Distribution Protocol (LDP) in the context of providing VPN services like IP-VPN involves the underlying technology used for label distribution and path determination within an MPLS network.
In summary, SR offers a more modern and scalable approach that integrates well with traffic engineering and simplifies the management of paths through the network. In contrast, LDP is an older protocol that works well for distributing labels but may require additional complexity for traffic engineering and can be less scalable in large networks.**<br>

For more deatils look at appendix:<br>

************************************LABS*****************************************<br>
My explenations on the topics of the demo:<br>
![image](https://github.com/netsecwiz/AristaL4/assets/123339313/9ae11423-2c16-4209-9a65-34cc6887bb5e)<br>

Deploy IS-IS as the Service Provider Underlay IGP:<br>
**IS-IS (Intermediate System to Intermediate System)**: This is a routing protocol used to determine the best path for data through a network of routers. In the context of a service provider, IS-IS is often used as the underlay network, meaning it's the foundational routing protocol that runs beneath other services, providing basic connectivity and route information.<br>

Establish MPLS Transport Label Distribution via Segment-Routing:<br>
**MPLS (Multi-Protocol Label Switching)**:<br>
 A method for speeding up and shaping traffic flows across enterprise and service provider networks.
Segment Routing (SR): An MPLS-based forwarding paradigm that simplifies routing, reduces state held on routers, and offers enhanced traffic engineering capabilities by encoding paths as sequences of "segments", which are pre-defined paths or instructions.
Prepare to Offer VPN Services to Customers via MP-BGP EVPN Control-Plane:<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/2991bed2-cf62-45fa-af9b-2d709dc9646b)<br>

**MP-BGP (Multi-Protocol Border Gateway Protocol)**: <br>
An extension of BGP that supports multiple address families (like unicast, multicast, VPN) and is used to exchange routing information in large and interconnected networks.
EVPN (Ethernet VPN): A BGP-based control plane for Ethernet traffic that allows for scalable Layer 2 VPN services.<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/6a6f2123-9b2a-4675-a564-55a66626a7fb)<br>

Deploy L3VPN Service for Customer-1:<br>
**L3VPN (Layer 3 Virtual Private Network)**: This service uses BGP to distribute VPN routing information across the provider's backbone, allowing for separation between different customers' networks on the same physical infrastructure.<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/92af0f3b-6510-46f8-9b3d-5d770f962625)<br>

Deploy L2VPN Service for Customer-2:<br>
**L2VPN (Layer 2 Virtual Private Network)**: This provides a point-to-point or point-to-multipoint service over the service provider's network, extending a customer's LAN and its Layer 2 traffic between geographically separate sites.<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/c2a6bcf9-1768-4132-bc18-3463648b3282)<br>

Deploy E-LINE Service for Customer-3:<br>
**E-LINE**: A type of Ethernet VPN that provides a point-to-point Ethernet virtual connection between two customer sites, often used for dedicated capacity and privacy.<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/98fb36fa-d21c-4179-9099-0d315844435d)<br>

Enable TI-LFA Fast Reroute for ISIS-SR:<br>
**TI-LFA (Topology Independent Loop-Free Alternate):** A fast reroute mechanism that provides protection against link or node failures in the network by pre-computing backup paths.
**ISIS-SR (IS-IS with Segment Routing)**: This combines traditional IS-IS routing with the traffic engineering capabilities of Segment Routing.<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/47febc36-bc4d-4c87-953c-7f28fc7dc185)<br>

Leverage SR-TE to Steer VPN Traffic:<br>
**SR-TE (Segment Routing Traffic Engineering)**: Allows network operators to define paths through the network that can optimize and steer traffic based on specific requirements or constraints, used particularly for efficient and optimized VPN traffic handling.<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/bbac312a-cb92-42b0-8c20-3a25f8b8e3b7)<br>
Deploy L3VPN Service for Customer-4<br>
Repeat of customer 1, but seperated.<br>

![image](https://github.com/netsecwiz/AristaL4/assets/123339313/8b76d161-a863-481c-97cc-585bf9655a76)<br>

Offer Centralized Services to L3VPN Customers:<br>
**Centralized services** could include centralized internet access, cloud services, or other shared resources that L3VPN customers can utilize without the need to deploy them individually for each customer, often leading to cost savings and easier management.


***********APPENDIX**********<br>
**Segment Routing (SR)**:<br>
Path Control: SR allows for more granular path control. The path a packet will take through the network is encoded in the packet header as a list of segments by the source router. This is often referred to as source routing.
Simplification: It simplifies the network by reducing the amount of state information required on each router because the path is determined at the edge of the network.
Traffic Engineering: SR naturally integrates with traffic engineering because it can steer traffic through a specified path without requiring additional protocols like RSVP-TE.
Scalability: As networks grow, SR scales better because it doesn't require a full mesh of LDP sessions between routers.
Fast Reroute: SR supports fast reroute capabilities like TI-LFA, making the network more resilient to failures.
Label Distribution Protocol (LDP):

**Label Distribution: LDP** <br>
Is used specifically for the distribution of labels in an MPLS network. It operates by creating a session between neighboring nodes and exchanging label binding information for reachable routes.
Network State: With LDP, each router in the network needs to maintain label information for each reachable destination, which can increase the amount of state maintained in larger networks.
Traffic Engineering: While LDP can be used in conjunction with traffic engineering, it typically requires additional protocols like RSVP-TE (Resource Reservation Protocol-Traffic Engineering) to set up explicit traffic-engineered paths.
Full Mesh Requirement: In some VPN implementations, LDP requires a full mesh of peerings to distribute labels, which can be cumbersome to manage in large-scale deployments.
When comparing SR with LDP in the context of VPN services:

**SR for VPNs**: <br>
VPNs can leverage SR for more efficient routing and path selection. SR can be used to influence the path traffic takes through the network and can be particularly useful in Segment Routing MPLS (SR-MPLS) VPNs.

**IP-VPN with LDP**: <br>
In traditional IP-VPNs, LDP is used alongside protocols like MP-BGP to distribute VPN labels for MPLS VPN services. Each router must learn the labels for the VPN routes, which can require more overhead and complex configurations as the network scales.


