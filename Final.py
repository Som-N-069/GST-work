import os
import pyttsx3
import webbrowser
import pandas as pd
from docx import Document









while True:
    print('\nWelcome to our Gst composition counselling')
    print("Hello sir ! How can I help you ?")
    pyttsx3.speak("Hello sir ! How can I help you ?")

    
    while True:
        print("\n1. Want  To  Know  About  GST  Composition Scheme !")
        print("2. Want To Check the applicability For Opting of Cmposition Scheme under GST !")
        print("3. Exit")
        pyttsx3.speak("Want  To  Know  About  GST  Composition Scheme !")
        pyttsx3.speak("Want  To  Check  the  applicability  For  Opting  in  Cmposition Scheme  under  GST !")

        p=input("Please input number")


        if("1" in p):
            print("Opening the file ")
            pyttsx3.speak("Opening the file ")
            url = 'https://gstcouncil.gov.in/sites/default/files/e-version-gst-flyers/composition-levy-scheme.pdf'
            Edge_Path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
            webbrowser.get(Edge_Path).open(url)
            os.system('') 
            print("You have closed the file. Anything else sir?")
            pyttsx3.speak("You have closed the file. Anything else sir?")



        
            

    
        elif('2' in p):
            print("\nIf you want to check the applicability then first enter GSTIN")
            pyttsx3.speak("if you want to check the applicability then first enter GST Identification number")

            t=input("Enter GSTIN NO.")
            if len(t)==15:
                print("\nWhich activity Business involved ")
                print(" 1) In Manufacture")
                print(" 2) In Restaurants Services")
                print(" 3) In Trading Services ")
                print(" 4) In Other Services")
                pyttsx3.speak("which activity business is involved ")
                pyttsx3.speak(" In Manufacture")
                pyttsx3.speak(" In Restaurants Services")
                pyttsx3.speak(" In Trading Services ")
                pyttsx3.speak(" or In Other Services")
                s=input("Enter which activity business or indivisual involved (1-4)")

                
                #subMain 1
                if("1" in s):
                    print("\nIf you are doing any Activity which is Restricted under Composition Scheme Press Yes else Press No")
                    bold_s="\033[1m"
                    bold_e="\033[0m"
                    z="Common restrictions are given in About Section of Composition Scheme."
                    print(bold_s+z+bold_e)
                    pyttsx3.speak("If you are doing any Activity which is Restricted under Composition Scheme ! then ! Type yes !  else !  Type No")
                    r=input("enter")
                    if("no" in r):
                        print("\nPlease enter the state in which business is operating") 
                        pyttsx3.speak("Please enter the state in which business is operating")
                        L=["Arunachal Pradesh","Assam","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura","Himachal Pradesh","Uttarakhand","Jammu amd Kashmir"]
                        b=input("enter the state")
                        if(b in L):
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))  
                            if(v<7500000):
                                print("As per Composition Scheme. Your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")        
                        else:
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))
                            if(v<15000000):
                                print("As per Composition Scheme your Aggregate Turnover is less than specified amount so you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                
                    elif("yes" in r):
                        print("Sorry ! But you are not eligible to opt for Composition scheme ")
                        pyttsx3.speak("Sorry ! But you are not eligible to opt for Composition scheme ")
                    else:
                        print("Sorry ! woring Input")
                        pyttsx3.speak("Sorry ! woring Input")




                #submain 2
                elif("2" in s):
                    print("\nIf you are doing any Activity which is Restricted under Composition Scheme Press Yes else Press No")
                    bold_s="\033[1m"
                    bold_e="\033[0m"
                    z="Common restrictions are given in About Section of Composition Scheme."
                    print(bold_s+z+bold_e)
                    pyttsx3.speak("If you are doing any Activity which is Restricted under Composition Scheme ! then ! Type yes !  else !  Type No")
                    r=input("enter")
                    if("no" in r):
                        print("\nPlease enter the state in which business is operating") 
                        pyttsx3.speak("Please enter the state in which business is operating")
                        L=["Arunachal Pradesh","Assam","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura","Himachal Pradesh","Uttarakhand","Jammu amd Kashmir"]
                        b=input("enter the state")
                        if(b in L):
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))  
                            if(v<7500000):
                                print("As per Composition Scheme. Your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")        
                        else:
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))
                            if(v<15000000):
                                print("As per Composition Scheme your Aggregate Turnover is less than specified amount so you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                
                    elif("yes" in r):
                        print("Sorry ! But you are not eligible to opt for Composition scheme ")
                        pyttsx3.speak("Sorry ! But you are not eligible to opt for Composition scheme ")
                    else:
                        print("Sorry ! woring Input")
                        pyttsx3.speak("Sorry ! woring Input")





                #submain 3
                elif("3" in s):
                    print("\nIf you are doing any Activity which is Restricted under Composition Scheme Press Yes else Press No")
                    bold_s="\033[1m"
                    bold_e="\033[0m"
                    z="Common restrictions are given in About Section of Composition Scheme."
                    print(bold_s+z+bold_e)
                    pyttsx3.speak("If you are doing any Activity which is Restricted under Composition Scheme ! then ! Type yes !  else !  Type No")
                    r=input("enter")
                    if("no" in r):
                        print("\nPlease enter the state in which business is operating")
                        pyttsx3.speak("Please enter the state in which business is operating") 
                        L=["Arunachal Pradesh","Assam","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura","Himachal Pradesh","Uttarakhand","Jammu amd Kashmir"]
                        b=input("enter the state")
                        if(b in L):
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))  
                            if(v<7500000):
                                print("As per Composition Scheme. Your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")        
                        else:
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))
                            if(v<15000000):
                                print("As per Composition Scheme your Aggregate Turnover is less than specified amount so you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                
                    elif("yes" in r):
                        print("Sorry ! But you are not eligible to opt for Composition scheme ")
                        pyttsx3.speak("Sorry ! But you are not eligible to opt for Composition scheme ")
                    else:
                        print("Sorry ! woring Input")
                        pyttsx3.speak("Sorry ! woring Input")







                elif("4" in s):
                    print("\nIf you are doing any Activity which is Restricted under Composition Scheme Press Yes else Press No")
                    bold_s="\033[1m"
                    bold_e="\033[0m"
                    z="Common restrictions are given in About Section of Composition Scheme."
                    print(bold_s+z+bold_e)
                    pyttsx3.speak("If you are doing any Activity which is Restricted under Composition Scheme ! then ! Type yes !  else !  Type No")
                    r=input("enter")
                    if("no" in r):
                        print("\nPlease enter the state in which business is operating")
                        pyttsx3.speak("Please enter the state in which business is operating") 
                        L=["Arunachal Pradesh","Assam","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura","Himachal Pradesh","Uttarakhand","Jammu amd Kashmir"]
                        b=input("enter the state")
                        if(b in L):
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))  
                            if(v<5000000):
                                print("As per Composition Scheme. Your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")        
                        else:
                            print("Now ! Enter the Aggregate Turnover of the Business")
                            pyttsx3.speak("Now Enter the Aggregate Turnover of the Business")
                            v=int(input("Rs."))
                            if(v<5000000):
                                print("As per Composition Scheme your Aggregate Turnover is less than specified amount so you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                print("Thankyou for using the Application")
                                pyttsx3.speak("As per Composition Scheme ! your Aggregate Turnover is less than specified amount ! So you are now Eligible to opt for Composition Scheme as per CGST act 2017")
                                pyttsx3.speak("Thankyou for using the Application")
                                break;   
                            else:
                                print("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                pyttsx3.speak("Sorry ! You are not eligible to opt for ! Composition Scheme ! As your Aggregate Turnover is Exceeding the prescribed Limit")
                                
                    elif("yes" in r):
                        print("Sorry ! But you are not eligible to opt for Composition scheme ")
                        pyttsx3.speak("Sorry ! But you are not eligible to opt for Composition scheme ")
                    else:
                        print("Sorry ! woring Input")
                        pyttsx3.speak("Sorry ! woring Input")

                else:
                    print("Please put numbers between 1-4")
                    pyttsx3.speak("Please put numbers between 1-4")
                    break;
                
            else:
                print("Please put a valid GSTIN number")
                pyttsx3.speak("Please put a valid GST Identification number")
                break;



        elif("3" in p):
            pyttsx3.speak("Thankyou for using the Application")
            break;
        else:
            pyttsx3.speak("Thankyou for using the Application")






