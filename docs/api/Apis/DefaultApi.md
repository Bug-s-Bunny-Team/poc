# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationsGet**](DefaultApi.md#locationsGet) | **GET** /locations | Returns all Location |
| [**locationsLocationIdGet**](DefaultApi.md#locationsLocationIdGet) | **GET** /locations/{locationId} | Returns a Location by ID |
| [**postsGet**](DefaultApi.md#postsGet) | **GET** /posts | Returns all Post |
| [**postsPost**](DefaultApi.md#postsPost) | **POST** /posts | Scrape and analyze a new Post |
| [**postsPostIdGet**](DefaultApi.md#postsPostIdGet) | **GET** /posts/{postId} | Returns a Post by ID |


<a name="locationsGet"></a>
# **locationsGet**
> List locationsGet()

Returns all Location

### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/Location.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="locationsLocationIdGet"></a>
# **locationsLocationIdGet**
> Location locationsLocationIdGet(locationId)

Returns a Location by ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locationId** | **Integer**|  | [default to null] |

### Return type

[**Location**](../Models/Location.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postsGet"></a>
# **postsGet**
> List postsGet()

Returns all Post

### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/Post.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postsPost"></a>
# **postsPost**
> postsPost(\_posts\_get\_request)

Scrape and analyze a new Post

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **\_posts\_get\_request** | [**_posts_get_request**](../Models/_posts_get_request.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="postsPostIdGet"></a>
# **postsPostIdGet**
> Post postsPostIdGet(postId)

Returns a Post by ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **postId** | **Integer**|  | [default to null] |

### Return type

[**Post**](../Models/Post.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

