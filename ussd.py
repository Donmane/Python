comment = """    
                 1. Data Plans
                 2. Social Bundles
                 3. Hot Deals
                 4. Chat Zigi """
  
comment1 = """    
                 Buy Data Plans
                 1. Daily
                 2. Weekly
                 3. Montly
                 4. 2-3 Month
                 5. Always On Plans
                 6. Mifi Plans
                 7. Family Packs
                 8. Hot Deals
                 9. Free Youtube
                 10. Manage Data
                 0. Back
                 99. Next
     """     
   
     


comment2 = """   
                  Buy Data Plans
                  1. Daily 50MB
                  2. Daily 100MB+Socials
                  3. Daily 650MB
                  4. Daily 300mb+300sec
                  5. Night & Wknd Plan
                  6. +Social
                  0. Back """
       
comment3 = """
                  Buy Data Plans
                  1. Wkly 250MB
                  2. Weekly Data Plan + Social
                  3. Data+Content
                  4. Weekly Boomplay Data 
                  0. Back"""
                    
     
comment4 = """
                  Buy Data Plans
                  1. Mnthly 500mb
                  2. Mnthly 1.5GB - 4.5GB
                  3. Mnthly 11GB - 125GB
                  4. Mnthly Boomplay Data
                  0. Back """
 
comment5 = """
                  Buy Data Plans
                  1. 225GB Bi-monthly data plan for N30000
                  0. Back """

comment6 = """
                 Buy Data Plans
                 1. WhatsApp
                 2. Opera 
                 3. Tiktok
                 4. Instagram
                 5. All Social Bundles
                 6. Youtube, Instagram, and TikTok
                 7. Opera Mini & News
                 8. Social Mega Bundle
                 0. Back
                 99. Next """
                
comment7 = """
                  20MB WhatsApp / 1day / N25. what should happen
                  when your bundle finishes?
                  1. Continue browsing from airtime / 160MB Extra
                  2. Stop my data
                  0. Back """           

comment8 = """
                 Buy Data Plans
                 1. Opera Bundle Daily
                 2. Opera Bundle Weekly
                 3. Opera Bundle Montly
                 0. Back """

comment9 = """
                 Buy Data Plans
                 1. N100 / 400MB / 3 days
                 2. N200 / 1GB / 14 days
                 0. Back """

comment10 = """
                 Buy Data Plans
                 1. 250MB for Instagram/N100/Daily
                 2. 1GB for Instagram/N200/Daily
                 0. Back
                 00. Done
                 000. Back to menu """
inpu = input('Enter ussd code:')


def ussd():
     if inpu == '*131#':
      print(comment)
      inpu1 = input('>>>') 
      
      if inpu1 == '1':
        print(comment1)
        
        inpu2 = input('>>>') 
        if inpu2 == '0' :
         print(comment) 
        elif inpu2 == '1':
         print(comment2)
        elif inpu2 == '2':
         print(comment3)
        elif inpu2 == '3':
         print(comment4)
        elif inpu2 == '4':
         print(comment5)
        elif inpu2 == '':
          quit()  
  
        inpu3 = input('>>>') 
        if inpu3 == '0' :
         print(comment1) 
        elif inpu3 == '1':
         print(comment2)
        elif inpu3 == '2':
         print(comment3)
        elif inpu3 == '3':
         print(comment4)
        elif inpu3 == '4':
         print(comment5)
        elif inpu3 == '':
         quit()  
 
        if inpu2 == '1' or '2' or '3' or '4':      
         inpu4 = input('>>>')
        elif inpu2 != '1' or '2' or '3' or '4':
         print('')
         quit()
 
        if inpu4 == '0':
         print(comment1)
        elif inpu4 == '1':
         print(comment2)
        elif inpu4 == '2':
         print(comment3)
        elif inpu4 == '3':
         print(comment4)
        elif inpu4 == '4':
         print(comment5)
        elif inpu3 == '':
         quit()
        input1 = input('>>>')
        if input1 == '0':
          print(comment1)
        elif input1 == '1':
         print(comment2)
        elif input1 == '2':
         print(comment3)
        elif input1 == '3':
         print(comment4)
        elif input1 == '4':
          print(comment5)
        elif input1 == '':
           quit()
 
        inpu7 = input('>>>')
        if inpu7 == '0':
         print(comment1)
        elif inpu7 == '1':
         print(comment2)
        elif inpu7 == '2':
         print(comment3)
        elif inpu7 == '3':
         print(comment4)
        elif inpu7 == '4':
         print(comment5)
        elif inpu7 == '':
          quit()
        input3 = input('>>>')
        if input3 == '0':
         print(comment1)
 
        input4 = input('>>>')
        if input4 == '0':
         print(comment1)
        elif input4 == '1':
         print(comment2)
        elif input4 == '2':
         print(comment3)
        elif input4 == '3':
         print(comment4)
        elif input4 == '4':
         print(comment5)
        input3 = input('>>>')
        if input3 == '0':
           print(comment1)         
           input5 = input('>>>')      
        if input5 == '0':
           print(comment)
        else:
           quit()
      elif inpu1 == '2':
       print(comment6) 
       input6 = input('>>>')
       if input6 == '1':
         print(comment7)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input6 == '2':
         print(comment8)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input6 == '3':
         print(comment9)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()     
     
       elif input6 == '4':
         print(comment10)      
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()

       elif input6 == '0':
         print(comment6)
       else:
         quit()  
       input9 = input('>>>') 
       if input9 == '1':
         print(comment7)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input9 == '2':
         print(comment8)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input9 == '3':
         print(comment9)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()     
     
       elif input9 == '4':
         print(comment10)      
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()

       elif input9 == '0':
         print(comment6)
       else:
         quit()         

       input8 = input('>>>') 
       if input8 == '1':
         print(comment7)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input8 == '2':
         print(comment8)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input8 == '3':
         print(comment9)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()     
     
       elif input8 == '4':
         print(comment10)      
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()

       elif input8 == '0':
         print(comment6)
       else:
         quit()         


       input10 = input('>>>') 
       if input10 == '1':
         print(comment7)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input10 == '2':
         print(comment8)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()
       
       elif input10 == '3':
         print(comment9)
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()     
     
       elif input10 == '4':
         print(comment10)      
         input7 = input('>>>')
         if input7 == '0':
            print(comment6)
         else:
            quit()

       elif input10 == '0':
            quit()
       else:
         quit()         
       if input10 == '000':
        print(comment)
      # inpu3 = input('>>>')  
      # if inpu3 == '0':
      #  print(comment)
      # elif inpu3 == '2':
      #  print(comment3)   
      #  inpu4 = input('>>>')  
      # elif inpu3 == '3':
      #  inpu4 = input('>>>')  
      #  print(comment4)   
      #  inpu4 = input('>>>')  
      # elif inpu3 == '4':
      #  print(comment5)   
      
      # inpu4 = input('>>>')  
      # if inpu4 == '0':
      #    print(comment1) 
     elif inpu != '*131#':
      print("error")
     else:
         quit()

   
ussd()
     

     