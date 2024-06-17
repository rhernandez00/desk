^!+a::
    ; Create an HTTP POST request
    url := "http://192.168.86.113:5000/command"
    jsonData := "{""command"": ""Up_b""}"
    
    ; Create a COM object to handle the HTTP request
    httpObj := ComObjCreate("MSXML2.ServerXMLHTTP.6.0")
    
    ; Open the HTTP connection
    httpObj.open("POST", url, false)
    
    ; Set the request headers
    httpObj.setRequestHeader("Content-Type", "application/json")
    
    ; Send the request with the JSON data
    httpObj.send(jsonData)
    
return

^!+b::
    ; Create an HTTP POST request
    url := "http://192.168.86.113:5000/command"
    jsonData := "{""command"": ""Down_b""}"
    
    ; Create a COM object to handle the HTTP request
    httpObj := ComObjCreate("MSXML2.ServerXMLHTTP.6.0")
    
    ; Open the HTTP connection
    httpObj.open("POST", url, false)
    
    ; Set the request headers
    httpObj.setRequestHeader("Content-Type", "application/json")
    
    ; Send the request with the JSON data
    httpObj.send(jsonData)
    
return
