function wow(){
    a=['!','@','#','$','%','/','^','&','*','>','<','{','}',']','[',"'",'"',",",'-',"|",'~',"`"];
    s=document.getElementById("deck_name").value;
    if (s == "") {
alert("front field must be filled out");
return false;
}
for (i in s){
if (a.includes(s[i])){
alert("invalid input");
return false;
}
}
}
