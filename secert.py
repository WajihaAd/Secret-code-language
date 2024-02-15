import random
def main():
  sentence=input("Enter the secret code:\n")
  options=int(input("Enter 1 for encoding and 2 for decoding and 3 for quit: "))
  if options==1 and options==2 and option==3:
    raise ValueError("Enter a valid option")
  match options:
    case 1:
      encoding(sentence)
    case 2:
      decode(sentence)
    case 3:
      exit()


def encoding(sent):
  if not sent:
    raise ValueError("Please enter a valid string")
    
  if len(sent) >= 3:
      words=sent.split()
      list1 = list(words)
      for word in words:
        list1 = list(sent)  
        # print(list1)       
        firstchar=list1.pop(0)        
        # print(l)       
        # print(g)
        list1.append(firstchar)
        # print(list1) 
      for i in range(3):
        list2 = ['a','b','c','d','e','f','g','h','i','j','k','l' ,'m','n','o','p','q','r','s','t','u','v','w','x' ,'y','z','@','!','$','%','^','&','*','(',')','#']
        random.shuffle(list2)  
        g=random.choice(list2)
        j=random.choice(list2)
        list1.insert(i,g)
        list1.append(j)
      # print(list1)
      sent1=''.join(list1)
      print(sent1)
    
  elif len(sent) < 3:
    list1=list(sent)
    list1.reverse()
    sent1=''.join(list1)
    print(sent1)
    
 
  else:
    raise ValueError("Please enter a valid string")
  
  main()
 



def decode(sent):
  if len(sent)>=3:
    list1=list(sent)
    # print(list1)
    for i in range(2,-1,-1):
      list1.pop(i)
    # print(list1)
    for i in range(3):
      list1.pop()
    # list1=list1[:-3]
    # print(list1)
    g=list1.pop()
    # print(g)
    list1.insert(0,g)
    # print(list1)
    sent=''.join(list1)
    print(sent)
  
  else:
    list1=list(sent)
    list1.reverse()
    sent=''.join(list1)
    print(sent)
 
  main()

   
    
    
      

main()
    
# # import random
# seq = ['a', 'b', 'c', 'd', 'e']
# random.shuffle(seq)
# print(seq)
# import random
# seq = ['apple', 'banana', 'orange']
# print(random.choice(seq))
# string = ''.join(char_list) is used to change list into string
