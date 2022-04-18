# DashboardDeutschland.GeoApi

All URIs are relative to *https://www.dashboard-deutschland.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geo**](GeoApi.md#geo) | **GET** /geojson/de-all.geo.json | Zugriff auf Geojson-Daten zu Deutschland und den Ländern


# **geo**
> [Geo] geo()

Zugriff auf Geojson-Daten zu Deutschland und den Ländern

Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).

### Example


```python
import time
from deutschland import DashboardDeutschland
from deutschland.DashboardDeutschland.api import geo_api
from deutschland.DashboardDeutschland.model.geo import Geo
from pprint import pprint
# Defining the host is optional and defaults to https://www.dashboard-deutschland.de
# See configuration.py for a list of all supported configuration parameters.
configuration = DashboardDeutschland.Configuration(
    host = "https://www.dashboard-deutschland.de"
)


# Enter a context with an instance of the API client
with DashboardDeutschland.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = geo_api.GeoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Zugriff auf Geojson-Daten zu Deutschland und den Ländern
        api_response = api_instance.geo()
        pprint(api_response)
    except DashboardDeutschland.ApiException as e:
        print("Exception when calling GeoApi->geo: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Geo]**](Geo.md)

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

