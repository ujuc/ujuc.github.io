Title: Spec Architecture Design Guide Restructure (번역)
Date: 2016-05-29 13:43
Category: Cloud
Tags: openstack, documents, spec, architecture design guide
Slug: spec-architecture-design-guide-restructure (번역)
Summary: 이번 스펙문서로 Architecture Design Guide를 새롭게 구축하는 것에 대해서 올라왔다.

[Architecture Design Guide](http://docs.openstack.org/arch-design/)가 새롭게 작성이되려나보다. 그것에 대한 스펙문서 번역이다.

원문: [Architecture Design Guide Restructure](http://specs.openstack.org/openstack/docs-specs/specs/newton/arch-guide-restructure.html)

---

## 문제점 설명
지금의 Architecture Design Giude는 주로 사용 사례를 중심으로 구성되어 있습니다. 그러나 OpenStack 클라우드를 설계함에 있어 여러 사용 사례에서 기능들이 조합되어 사용되는 경우가 있습니다.

사용자가 모든 요구 사항을 고려할 수 있는 OpenStack 클라우드 아키텍처를 결정하는 것을 돕기위한 정보로 재구성하는 것이 필요합니다. 개발중이거나 단계적으로 반영을 하거나, 실제 서비스하고 있는 환경에서 OpenStack을 설계할때 필요한 정보를 추가해야합니다. 이번 제안은 클라우드에대한 아키텍처 컨셉과 다양한 OpenStack 프로젝트 추상화에 대한 더 상세한 구조를 개발하는 것입니다. 이것을 통해서 쉽게 가이드를 유지하고 업데이트 할 수 있습니다.

## 변경사항 제안
이번 가이드에서 제안되는 구조는 일반적인 클라우드 사용사례, 일반적인 아키텍처 컨셉, 주요 클라우드 아키텍처 구성요소에서 장애가 발생하였을때에 대한 자세한 설명과 그것에 대한 설계 방법 등을 설명합니다.

각 장은 다음과 같이 설계됩니다:

1. Technical Detail
2. Capacity and Scale
3. High Availablility
4. Operator Requirements
5. Deployment Considerations
6. Maintenance Considerations

표제에서 제공될 정보에 대한 형식은 따로 가이드라인을 제공할 예정입니다. 이것을 이용하여 정보를 호출하기위해 특정한 필요학 있는 경우에만 사용됩니다.

## 목차 제안
새로운 Architecture Design Guide는 다음과 같이 새롭게 구성됩니다:

1. General Overview
2. Use Cases
	1. Development Cloud
		1. Stackeholder
		2. User Stories
		3. Designe Model
		4. Component Block Diagram
	2. General Compute Cloud
		1. Stakeholders
		2. User Stories
		3. Design Model
		4. Component Block Diagram
	3. Web Scale Cloud
		1. Stakeholders
		2. User Stories
		3. Design Model
		4. Component Block Diagram
	4. Public Cloud
		1. Stakeholders
		2. User Stories
		3. Design Model
		4. Component Block Diagram
3. High Availability
	1. Overview
4. Capacity and Scale
	1. Overview
5. Design
	1. Compute
	2. Storage
	3. Networking
	4. Identity
	5. Iamge
	6. Control Plane
	7. Dashboard and APIs

---

뭐 이정도까지... 더해봤자... 의미가 없다...
