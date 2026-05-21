# DND 5e CR versus player calculator

## description
used to calculate combat difficulty in dungeons

## custom monster CR pipeline
start  
-->  
create monster stat block via google docs  
-->  
create dict variable based on monster stat block in PyCharm  
-->  
plug dict variable into plugger function, which goes into he CR crafter  
-->  
put result of CR crafter into the csv file, and update the file on PyCharm  
-->  
call the csv file's CR values to use in the encounter difficulty calculations  
-->  
end  

## TODOs
```pycon
#TODO: port this to java
```
i'm running into scenarios where i have to make custom variables / classes, and if i'm doing that a lot i might as well do java
maybe i could make a python to java converter?  
no.  
that would be a very not good way to see god.   
he would pull up and say:  
"holy canola bro, go outside."