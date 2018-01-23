# Service Registry
API Gateway in AWS is used as service register when we are dealing with AWS Serverless architectures for microservices 

##Need
Service registry patterns is needed because client need to lookup for the appropriate service instance. 

## When Used
--When we need to invoke the REST API
--When we need to invoke the Thrift API

## Approach (Client Side)
ServiceClient->ServiceRegistry->ServiceEndPoint(Dynamically Served) 

## Examples
### Apache Zookeeper
### Consul
