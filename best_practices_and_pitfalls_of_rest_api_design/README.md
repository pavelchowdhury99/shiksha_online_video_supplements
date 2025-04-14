# Building RESTful APIs: Best Practices and Common Pitfalls

## Best Practices 
1. Know the fundamental concepts of [REST](https://restfulapi.net/) and do not consider REST to be confined to HTTP.
2. Using JSON as your resource sharing format wherever applicable.
3. For CRUD applications use nouns to identify to resources as we already have the HTTP methods like GET,POST,DELETE,PUT and PATCH to suggest the type of operation.<br>
So instead of ```https://testsite.com/create-article``` make a post endpoint of ```https://testsite.com/article```
4. For a collection of resources of similar type e.g tweets, make the endpoint noun plural to suggest that.
```https://testsite.com/tweets/33```
5. To show nesting of resources e.g tweets and author of tweet nest them in the endpoint
e.g
```https://testsite.com/tweets/33/author```
6. Even after releasing newer versions of the API always thoroughly test and maintain the previous versions as well, as your client might be using older version and might not be able to migrate to latest one.
7. Try not share large object over HTTP rather share a link to the object from a CND bucket.


## Common Pitfalls
1. Not provide appropriate status/error messages in response body.
2. Not maintaing clear and concise documentation along with examples and FAQ for each released version.
3. Not having any authentication from client.
4. Not validating the data/request parameters received from client.
5. Not using filters, pagination or data limit while sharing the data in response.
