# DashboardDeutschland.IndicatorsApi

All URIs are relative to *https://www.dashboard-deutschland.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indicators**](IndicatorsApi.md#indicators) | **GET** /api/tile/indicators | Zugriff auf unterschiedliche Indikatoren


# **indicators**
> [Indicators] indicators()

Zugriff auf unterschiedliche Indikatoren

Die API ermöglicht Zugriff auf unterschiedliche Indikatoren im JSON-Format über einfache GET-request.

### Example


```python
import time
from deutschland import DashboardDeutschland
from deutschland.DashboardDeutschland.api import indicators_api
from deutschland.DashboardDeutschland.model.indicators import Indicators
from pprint import pprint
# Defining the host is optional and defaults to https://www.dashboard-deutschland.de
# See configuration.py for a list of all supported configuration parameters.
configuration = DashboardDeutschland.Configuration(
    host = "https://www.dashboard-deutschland.de"
)


# Enter a context with an instance of the API client
with DashboardDeutschland.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = indicators_api.IndicatorsApi(api_client)
    id = "tile_1648135639982" # str | Id des gewünschten Indikators. Mehrere Semikolon-getrennte Angaben sind möglich. Gesundheitsindikatoren (beginnend mit \"ginsy_ges\") lassen sich neben der o.g. Variante auch nach Regionen von Bundesländern unterteilt anfordern, durch einen Unterstrich, gefolgt von einer das Bundesland repräsentierenden Zahl (z.B. 9 für Bayern). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Zugriff auf unterschiedliche Indikatoren
        api_response = api_instance.indicators(id=id)
        pprint(api_response)
    except DashboardDeutschland.ApiException as e:
        print("Exception when calling IndicatorsApi->indicators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id des gewünschten Indikators. Mehrere Semikolon-getrennte Angaben sind möglich. Gesundheitsindikatoren (beginnend mit \&quot;ginsy_ges\&quot;) lassen sich neben der o.g. Variante auch nach Regionen von Bundesländern unterteilt anfordern, durch einen Unterstrich, gefolgt von einer das Bundesland repräsentierenden Zahl (z.B. 9 für Bayern). | [optional]

### Return type

[**[Indicators]**](Indicators.md)

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

