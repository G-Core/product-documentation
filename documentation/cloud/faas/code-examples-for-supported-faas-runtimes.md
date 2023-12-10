---
title: code-examples-for-supported-faas-runtimes
displayName: Function examples
published: true
order: 30
toc:
   --1--C#: "c#"
   --2--Basic C# function: "basic-c-hello-world-function"
   --2--C# function with deps: "c-function-with-dependencies"
   --2--C# function with data requests: "c-function-accessing-the-data-request"
   --1--Go: "go"
   --2--Basic Go function: "basic-go-hello-world-function"
   --2--Go function with deps: "go-function-with-dependencies"
   --2--Go function with request/response objects: "go-function-accessing-requestresponse-objects"
   --1--Java: "java"
   --2--Basic Java function: "basic-java-hello-world-function"
   --2--Java function with deps: "java-function-with-dependencies"
   --2--Java function with requests: "java-function-accessing-the-request"
   --1--Node.js: "nodejs"
   --2--Basic Node.js function: "basic-nodejs-hello-world-function"
   --2--Node.js function with deps: "nodejs-function-with-dependencies"
   --2--Node.js function with object requests: "nodejs-function-accessing-object-requestresponse"
   --1--Python: "python"
   --2--Basic Python function: "basic-python-hello-world-function"
   --2--Python function with deps: "python-function-with-dependencies"
   --2--Python function with object requests: "python-function-accessing-object-requestresponse"
pageTitle: FaaS Runtimes Code Examples for C#, Go, Java, Node.js, and Python | Gcore
pageDescription: Explore basic functions, functions with dependencies, and data request/response handling for different runtimes.
---
# Code examples for supported FaaS runtimes

This article introduces developers to the capabilities of <a href="https://gcore.com/docs/cloud/faas/about-function-as-a-service" target="_blank">FaaS</a> for all supported runtimes: .NET, Go, Java, Node.js, and Python. For each runtime, we provide examples of three abstract functions of ascending levels of complexity: 

- A basic function (“Hello world!”)
- A function with dependencies 
- A function for accessing a data request/response 

## C#

### Basic C# “hello world” function

```
using System;
using System.Collections.Generic;
using System.Threading.Tasks;


// main method will be module.handler
public class module
{
    public Task<object> handler(Dictionary<string, object> k8Event, Dictionary<string, string> k8Context)
    {
        return Task.FromResult<object>("hello world");
    }
}
```

### C# function with dependencies

This function uses the ```YamlDotNet``` dependencies.

```
using System;
using System.Collections.Generic;
using YamlDotNet.Serialization;
using System.Threading.Tasks;


public class module
{
    public Task<object> handler(Dictionary<string, object> k8Event, Dictionary<string, string> k8Context)
    {
        var person = new Person()
        {
            Name = "Michael J. Fox",
            Age = 56
        };
       
        var serializer = new SerializerBuilder().Build();
        return Task.FromResult<object>(serializer.Serialize(person)); // yaml
    }
}
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}
```

To build this function, specify the dependencies in the .csproj format:

```
<Project Sdk="Microsoft.NET.Sdk">
    <PropertyGroup>
        <TargetFramework>net6.0</TargetFramework>
        <AssemblyName>dependency-yaml</AssemblyName>
    </PropertyGroup>
    <ItemGroup>
        <PackageReference Include="YamlDotNet" Version="13.7.1" />
    </ItemGroup>
</Project>
```

### C# function accessing the data request 

For all runtimes, you can find the request object in the ```event``` map field. Each language has a unique type. For C#, it's ```HttpRequest``` from ```Microsoft.AspNetCore.Http```.

```
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;


// main method module.handler
public class module
{
    public Task<object> handler(Dictionary<string, object> k8sEvent, Dictionary<string, string> k8Context)
    {  
        var extension = (Dictionary<string, object>)k8sEvent["extension"];
        HttpRequest request = (HttpRequest)extension["request"];
        Console.WriteLine(request);
       
        if (request.Method == "POST") {
            return Task.FromResult<object>(create());
        } else if (request.Method == "GET") {
            return Task.FromResult<object>(get());
        } else {
            return Task.FromResult<object>("Method not allowed");
        }
    }


    public string create() {
        return "Creating something on POST request";
    }


    public string get() {
        return "Getting something on GET request";
    }
}
```

The dependencies should be structured as follows:

```
<Project Sdk="Microsoft.NET.Sdk">


  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
    <AssemblyName>access-request</AssemblyName>
  </PropertyGroup>


<ItemGroup>
    <FrameworkReference Include="Microsoft.AspNetCore.App" />
  </ItemGroup>


</Project>
```

## Go

### Basic Go “hello world” function

```
package kubeless


// main function: Handler
func Handler(event map[string]interface{}, context map[string]string) (string, error) {
    return "Hello world!", nil
}
```

### Go function with dependencies

This function uses the ```yaml``` dependencies.

```
package kubeless


import (
    "gopkg.in/yaml.v3"
)


type Person struct {
    Name string
    Age int
}


func Handler(event map[string]interface{}, context map[string]string) (string, error) {
    person := Person{Name: "John", Age: 55}
    data, err := yaml.Marshal(&person)
    return string(data), err
}
```

Dependencies should be defined as follows:

```
module function


go 1.20


require (
    gopkg.in/yaml.v3 v3.0.1
)
```

### Go function accessing request/response objects

The event extension includes request, response, and context objects. These can be accessed for improved precision in function management:

```
package kubeless


import (
    "net/http"
    "context"
    "fmt"
)


type Person struct {
    Name string
    Age int
}


func create() string {
    return "Use POST to create something"
}


func get() string {
    return "Use GET to get something"
}


func Handler(event map[string]interface{}, k8sContext map[string]string) (string, error) {
    extension := event["extension"].(map[string]interface{})
    r := extension["request"].(*http.Request)
    w := extension["response"].(http.ResponseWriter)
    ctx := extension["context"].(context.Context)
   
    fmt.Println(r, w, ctx)
    if r.Method == "GET" {
        return get(), nil
    } else if r.Method == "POST" {
        return create(), nil
    }
   
    return "Method not allowed", nil
}
```

## Java

### Basic Java “hello world” function

```
package io.kubeless;


import java.util.HashMap;


public class Module {
    public String handler(HashMap<String, Object> event, HashMap<String, String> context) {
        return "Hello world!";
    }
}
```

### Java function with dependencies

```
package io.kubeless;


import java.util.HashMap;


import org.joda.time.LocalTime;


public class Module {
    public String handler(HashMap<String, Object> event, HashMap<String, String> context) {
        LocalTime currentTime = new LocalTime();
        return "Hello world! Current local time is: " + currentTime;
    }
}
```

Dependencies should be defined as follows:

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <artifactId>function</artifactId>
  <name>function</name>
  <version>1.0-SNAPSHOT</version>
  <dependencies>
     <dependency>
       <groupId>joda-time</groupId>
       <artifactId>joda-time</artifactId>
       <version>2.9.2</version>
     </dependency>
  </dependencies>
  <parent>
    <groupId>io.kubeless</groupId>
    <artifactId>kubeless</artifactId>
    <version>1.0-SNAPSHOT</version>
  </parent>
</project>
```

### Java function accessing the request

```
package io.kubeless;


import java.util.HashMap;
import com.sun.net.httpserver.HttpExchange;

public class Module {
    public String handler(HashMap<String, Object> event, HashMap<String, String> context) {
        // Access to Request/Response
        HashMap<String, Object> extension = (HashMap) event.get("extension");
        HttpExchange he = (HttpExchange) extension.get("exchange");
        // Request&Resposne can be manipulated through HttpExchange


        String requestMethod = he.getRequestMethod();
        System.out.println("HTTP Method: " + requestMethod);


        if ("GET".equals(requestMethod)) {
            return "Get some objects";
        } else if ("POST".equals(requestMethod)) {
            return "Create some objects";
        }


        return "Method not allowed";
    }
}
```

## Node.js

### Basic Node.js “hello world” function

```
module.exports = {
  handler: function (event, context) {
    return 'hello world!';
  }
}
```

### Node.js function with dependencies

```
'use strict';


const _ = require('lodash');


module.exports = {
    handler: (event, context) => {
        _.assign(event.data, {date: new Date().toTimeString()})
        return JSON.stringify(event.data);
    },
};
```

The dependencies should be structured as follows:

```
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "A simple project with Lodash dependency",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "lodash": "^4.17.21"
  }
}
```

### Node.js function accessing object request/response

```
'use strict';


module.exports = {
    handler: (event, context) => {
        request = event.extension.request;
        response = event.extension.response;
        // Manipulate request/response as you wish
       
        return "some message"
    },
};
```

## Python

### Basic Python “hello world” function

```
def handler(event, context):
    return "hello world"
```

### Python function with dependencies

```
import yaml


def handler(event, context):
    person = {
        "name": "John",
        "age": 55
    }
   
    return yaml.dump(person)
```

The dependencies should be structured as follows:

```
PyYAML==6.0.1
```

### Python function accessing object request/response

```
import yaml
from aiohttp import web


def handler(event, context):
    request: web.Request = event["extension"]["request"]
    response: web.Response = event["extension"]["response"]
   
    print(request, response)
    return "Some result"
```
