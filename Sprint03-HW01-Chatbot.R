greeting_bot <- function()  {
  username = readline("What's your name: ")
  print(paste(username , "Welcome to GG’s Pizza"))
  

your_order  = readline(" what would you like to order today?  ")
print(paste(" okay, you will have ", your_order  , "."))


your_drinks = readline("What would you like to drinks? ")
  print(paste("your drink is ", your_drinks , "."))
  
  
  your_address = readline("Can I have your address please? ")
  print(paste("Your address is: ", your_address, "."))
  
  cf_order = readline("type Yes! to confirm your oder. ")
  print("Our delivery guy will be over in about thirty minutes. Thank you for calling. Keep on rockin' with GG's Pizza!.")
 
}
