# Mauser

# metadata

name: Mauser  
cr: ????  
url: [https://docs.google.com/document/d/14QU4AysS5lk1mlsOaElzohyduXIW90Csj1U9-URapl4/edit?tab=t.0](https://docs.google.com/document/d/14QU4AysS5lk1mlsOaElzohyduXIW90Csj1U9-URapl4/edit?tab=t.0)   
font: Virasco 2000  
author: Shwifty\_meme\_lord

# core stats

size: small  
type: Robot  
alignment: true neutral  
hp: 20  
ac: 13  
speed: 30

# ability scores

str\_numeric\_stat: 10  
str\_modifier: 10  
dex\_numeric\_stat: 12  
dex\_modifier: 1  
con\_numeric\_stat: 14  
con\_modifier: 2  
int\_numeric\_stat: 10  
int\_modifier: 0  
wis\_numeric\_stat: 10  
wis\_modifier: 10  
cha\_numeric\_stat: 10  
cha\_modifier: 0

# saving throws

dex: 2

# actions

## action \- bite and grab

action\_type: action  
attack\_type: melee\_attack  
hit\_modifier: 4  
damage: 3d4 \+ 5  
damage\_type: piercing   
notes: if it hits you, it grabs you as well. This feeds into the “actually grab” action

## instantaneous \- actually grab

action\_type: instantaneous   
attack\_type: saving\_throw  
save\_dc: 13  
save\_stat: str, dex  
damage: 2d4 \+ 3  
damage\_type: piercing

