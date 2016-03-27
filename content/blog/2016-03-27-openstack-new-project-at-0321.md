Title: OpenStack New Project at 0321
Date: 2016-03-27 22:47
Category: Community
Tags: openstack, big tent
Slug: openstack-new-project-at-0321
Summary: 이번에 새롭게 official project로 등록된 프로젝트들.

해당 내용 나온 곳 : [Technical Committee Highlights March 21, 2016](http://www.openstack.org/blog/2016/03/technical-committee-highlights-march-21-2016/)

## Dragonflow
* [Main wiki](https://wiki.openstack.org/wiki/Dragonflow)
* [Documentation](http://docs.openstack.org/developer/dragonflow/centralized_dragonflow.html)
* [Github](https://github.com/openstack/dragonflow)
* OpenStack® Neutron™ 에서 사용하는 fully distributed virtual router.

### 기능
* API for routing IPv4 East-West traffic
* Performance improvement for inter-subnet network by removing the amount of kernel layers (namespaces and their TCP stack overhead)
* Scalability improvement for inter-subnet newtork by offloading L3 East-West routing from the Network Node to all Compute Nodes
* Reliability improvement for inter-subnet network by removal of Network Node from the East-West traffic
* Simplified virtual routing management
* Support for all type dirvers GRE/VXLAN/LAN
* Support for centralized shared public network (SNAT) based on the legacy L3 implementation
* Support for centralized floating IP (DNAT) based on the legacy L3 implementation
* Support for HA, in case the connection to the legacy L3 HA. (Controller HA will be supported in the next rlease).
* Support for centralized IPv6 based on the legacy L3 implementation

## Kuryr
* [Main wiki](https://wiki.openstack.org/wiki/Kuryr)
* [Documentation](http://docs.openstack.org/developer/kuryr/)
* [Github](https://github.com/openstack/kuryr)
* Docker 네트워크 플러그인

## Tacker
* [Main wiki](https://wiki.openstack.org/wiki/Tacker)
* [Dcoumentation](http://tacker-docs.readthedocs.org/en/latest/index.html)
* [Github](https://github.com/openstack/tacker)
* OpenStack service for NFV Orchestration with a general purpose VNF Manager to deploy and operate Virtual Network Functions (VNFs) and Network Services on an NFV Platform. It is based on ETSI MANO Architectural Framework.

### Feature
* [Tracker Monitoring Framework](http://tacker-docs.readthedocs.org/en/latest/devref/monitor-api.html)
* [VNFD Template Parameterization](http://tacker-docs.readthedocs.org/en/latest/devref/vnfd_template_parameterization.html)

## EC2API
* [Main wiki](https://wiki.openstack.org/wiki/EC2API)
* [Github](https://github.com/openstack/ec2-api)
* AWS EC2 and VPC API support in standalone service for OpenStack.
