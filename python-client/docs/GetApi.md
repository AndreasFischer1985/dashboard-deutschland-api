# DashboardDeutschland.GetApi

All URIs are relative to *https://www.dashboard-deutschland.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](GetApi.md#get) | **GET** /api/dashboard/get | Zugriff auf alle gültigen Einträge des id-Parameters


# **get**
> [Get] get()

Zugriff auf alle gültigen Einträge des id-Parameters

Die API ermöglicht Zugriff auf alle gültigen Einträge des id-Parameters (siehe unten, Indikatoren).

### Example


```python
import time
from deutschland import DashboardDeutschland
from deutschland.DashboardDeutschland.api import get_api
from deutschland.DashboardDeutschland.model.get import Get
from pprint import pprint
# Defining the host is optional and defaults to https://www.dashboard-deutschland.de
# See configuration.py for a list of all supported configuration parameters.
configuration = DashboardDeutschland.Configuration(
    host = "https://www.dashboard-deutschland.de"
)


# Enter a context with an instance of the API client
with DashboardDeutschland.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = get_api.GetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Zugriff auf alle gültigen Einträge des id-Parameters
        api_response = api_instance.get()
        pprint(api_response)
    except DashboardDeutschland.ApiException as e:
        print("Exception when calling GetApi->get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Get]**](Get.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

