; This script will send a commands (words) to the Flask server (raspberry pi) based on the key combination used.
; It will send commands based on the variables to change in the light (up, down : brightness [l], red [r], green [g], blue [b] )
; Author: Raul Hernandez, 16/06/2024

; Define the Raspberry Pi IP address
raspberryIP := "http://192.168.86.113:5000/command"

; Define a function to send a command to the Flask server
SendCommand(command) {
    global raspberryIP ; Ensure the raspberryIP variable is accessible inside the function
    ; Create an HTTP POST request
    url := raspberryIP
    jsonData := "{""command"": """ command """}"
    
    ; Create a COM object to handle the HTTP request
    httpObj := ComObjCreate("MSXML2.ServerXMLHTTP.6.0")
    
    ; Open the HTTP connection
    httpObj.open("POST", url, false)
    
    ; Set the request headers
    httpObj.setRequestHeader("Content-Type", "application/json")
    
    ; Send the request with the JSON data
    httpObj.send(jsonData)
    
}

; Command for hotkey combination: Control + Alt + Shift + a, up_l
^!+a::
    SendCommand("up_l") ; Call the SendCommand
return

; Command for hotkey combination: Control + Alt + Shift + b, down_l
^!+b::
    SendCommand("down_l") ; Call the SendCommand
return

; Command for hotkey combination: Control + Alt + Shift + c, up_r
^!+c::
    SendCommand("up_r") ; Call the SendCommand
return

; Command for hotkey combination: Control + Alt + Shift + d, down_r
^!+d::
    SendCommand("down_r") ; Call the SendCommand
return

; Command for hotkey combination: Control + Alt + Shift + e, up_g
^!+e::
    SendCommand("up_g") ; Call the SendCommand
return

; Command for hotkey combination: Control + Alt + Shift + f, down_g
^!+f::
    SendCommand("down_g") ; Call the SendCommand
return

; Command for hotkey combination: Control + Alt + Shift + g, up_b
^!+g::
    SendCommand("up_b") ; Call the SendCommand
return

; Command for hotkey combination: Control + Alt + Shift + h, down_b
^!+h::
    SendCommand("down_b") ; Call the SendCommand
return
