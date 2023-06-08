

let x = 0
if(x == 0){
    console.log("condition x==0 is true, so we are inside the if statement")   
}


if(x != 0){
    console.log("we will never reach the inside of this if statement because the condition is false")
}else{
    console.log("we will always reach the inside of this else statement since the if condition is false")
}



if(x == 1){

}else if(x == 2){

}else if(x == 0){

}else{

}


switch(x){
    case 0:
        console.log("x == 0 from a switch statement")
        break
    case 1:
        console.log("this will NEVER execute")
        break
    case 2:
        console.log("this will NEVER execute")
        break;
}