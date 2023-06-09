

function callBackFunction(parameter){
    console.log(`${parameter} logged from a callback function`)
}

function callBackUser(normalParameter, callbackParameter){
    callbackParameter(normalParameter)
}

callBackUser("A normal paramter", callBackFunction)

