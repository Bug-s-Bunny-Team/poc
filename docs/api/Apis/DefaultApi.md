# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postsGet**](DefaultApi.md#postsGet) | **GET** /posts | Returns all Post |
| [**postsPostIdGet**](DefaultApi.md#postsPostIdGet) | **GET** /posts/{postId} | Returns a Post by ID |


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

