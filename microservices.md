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


## Best Practice Repository for Microservices
* Providing meaningful name in the request header which would help in tracing the problem with request origin. 
* Version Control - 


