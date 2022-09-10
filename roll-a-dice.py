import random 
  
# Take a variable to store response to keep rolling a dice
response = "y"
   
while response == "y": 
      
    # Gnenerates a random number 
    # between 1 and 6 (including 
    # both 1 and 6) 
    no = random.randint(1,6) 

    # conditions to check the number value  
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  ●  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ ●   ]") 
        print("[     ]") 
        print("[   ● ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[● ● ●]") 
        print("[     ]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[●   ●]") 
        print("[     ]") 
        print("[●   ●]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[●   ●]") 
        print("[  ●  ]") 
        print("[●   ●]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[● ● ●]") 
        print("[     ]") 
        print("[● ● ●]") 
        print("[-----]") 
          
    # Ask user to enter a response      
    response=input("press y to roll again and n to exit:") 
    print("\n") 