Microservices
=============
# How do we decide we need to adopt Microservices or not?
We need to understand that Microservices are not suitable all the time. The following scenarios may not be appropriate to use or adopt microservices:
* Developing a MVP
* Entire application effort is with short term goals
* Application does not have much interaction with external systems

# When Microservices would be a good bet ?
* MVP is tested and tried out want to have larger scalable application
* Need to have interaction with multiple services together
* Leverage APIs to extend the features to an ecosystem
* Would like to make changes quickly and test it out
* Large number of people are working on it
* Support required for loosely coupled business operations 
* Simplified approach towards update, replace, remove, augment
* Requirement of granular monitoring of functional components
* Rapid deployment requirements

# Service Registry
Service Registry plays a critical role in the Service Discovery. Two types of service discovery happens one is through Client Side and other one is through the Server side based on the Load Balancer

##Need
Service registry patterns is needed because client need to lookup for the appropriate service instance. 

## When to use
* REST API
* Thrift API

## Approach (Client Side)
ServiceClient->ServiceRegistry->ServiceEndPoint(Dynamically Served) 

## Examples
* etcd
* Apache Zookeeper
* Consul
* Kubernetes

# API Gateway Pattern

##Need
The services interaction needs to happen over the API Gateway 

# Best Practice Repository for Microservices
* Providing meaningful name in the request header which would help in tracing the problem with request origin. 
* Version Control - 

