### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  #should be == 1, = is used for assignment
      return True
    else #missing :
      return False
   

  dif highest_card(self, card1 card2): #missing comma between card1 and card2, also should be def instead of dif, also def/dif is indented one tab forward
  if card1.value > card2.value:
    return card #should be return card1
  else:
    return card2
  


def cards_total(self, cards): #entire function should be indented one tab further
  total  #should be total = 0 to initialize the variable
  for card in cards:
    total += card.value
    return "You have a total of" + total #Overindented. Also will fail due to being unable to add ints and strings, should be + str(total).
  
```
