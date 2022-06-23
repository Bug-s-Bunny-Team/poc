# Documentation for PoC API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *DefaultApi* | [**locationsGet**](Apis/DefaultApi.md#locationsget) | **GET** /locations | Returns all Location |
*DefaultApi* | [**locationsLocationIdGet**](Apis/DefaultApi.md#locationslocationidget) | **GET** /locations/{locationId} | Returns a Location by ID |
*DefaultApi* | [**postsGet**](Apis/DefaultApi.md#postsget) | **GET** /posts | Returns all Post |
*DefaultApi* | [**postsPost**](Apis/DefaultApi.md#postspost) | **POST** /posts | Scrape and analyze a new Post |
*DefaultApi* | [**postsPostIdGet**](Apis/DefaultApi.md#postspostidget) | **GET** /posts/{postId} | Returns a Post by ID |
*DefaultApi* | [**profilesGet**](Apis/DefaultApi.md#profilesget) | **GET** /profiles | Returns all SocialProfile |
*DefaultApi* | [**profilesProfileIdGet**](Apis/DefaultApi.md#profilesprofileidget) | **GET** /profiles/{profileId} | Returns a SocialProfile by ID |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Location](./Models/Location.md)
 - [Post](./Models/Post.md)
 - [SocialProfile](./Models/SocialProfile.md)
 - [_posts_get_request](./Models/_posts_get_request.md)
 - [_posts_get_request_oneOf](./Models/_posts_get_request_oneOf.md)
 - [_posts_get_request_oneOf_1](./Models/_posts_get_request_oneOf_1.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
