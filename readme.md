# Python API Package

This is a simple Python API package that allows you to make HTTP requests without using any external libraries.

## Installation

To install the package, simply copy the `api.py` file into your project directory.

## Usage

To use the package, import it into your Python script using the following code:

```python
import api
```

Once you have imported the package, you can use it to make API requests. For example, the following code would make a GET request to the `/api/v1/users` endpoint of the `example.com` API:

```python
api = api.API("example.com")
response = api.request("GET", "/api/v1/users")
print(response.status_code)
print(response.headers)
print(response.body)
```

This code would print the status code, headers, and body of the response to the console.

## API Reference

### `API()`

The `API()` constructor takes a single argument, which is the base URL of the API.

### `request()`

The `request()` method takes the following arguments:

* `method`: The HTTP method to use (e.g. "GET", "POST", "PUT", "DELETE")
* `path`: The path of the API endpoint (e.g. "/api/v1/users")
* `params` (optional): A dictionary of query parameters to include in the request
* `data` (optional): The body of the request
* `headers` (optional): A dictionary of headers to include in the request

The `request()` method returns a `Response` object, which contains the following attributes:

* `status_code`: The HTTP status code of the response
* `headers`: A dictionary of the response headers
* `body`: The body of the response

## Example

The following is a complete example of how to use the package to make an API request:

```python
import api

# Create an API object
api = api.API("example.com")

# Make a GET request to the /api/v1/users endpoint
response = api.request("GET", "/api/v1/users")

# Print the status code, headers, and body of the response
print(response.status_code)
print(response.headers)
print(response.body)
```

This code would print the following output:

```
200
{
  "Content-Type": "application/json",
  "Server": "nginx/1.16.1"
}
[
  {
    "id": 1,
    "name": "John Doe"
  },
  {
    "id": 2,
    "name": "Jane Smith"
  }
]
```
