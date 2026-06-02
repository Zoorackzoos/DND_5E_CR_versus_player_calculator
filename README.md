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

## major TODOS
```pycon
#TODO: make the databse be in .tsv instead of .csv
#TODO: consult a clanker on if that would be a good idea or not
```
to plug cells from pycharm into google sheets withotu making  
a whole new file you need the file to be separated by tabs, not commas.  

so that has me thinking we just have it one way. just .tsv.