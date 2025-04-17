import time
import random

print("""
         .--.
    .-._;.--.;_.-.
   (_.'_..--.._'._)
    /.' . 60 . '.\
   // .      / . \\
  |; .      /   . |;
  ||45    ()    15||
  |; .          . |;
   \\ .        . //
    \'._' 30 '_.'/
     '-._'--'_.-'
         `""` 
      
     made by Ohno
     
""")


print("Instructions: Wait for the computer to say 'GO', then press ENTER as fast as humanly possible.\n")
input("Press ENTER when you're ready to begin...\n")


delay = random.uniform(2, 5)  # Random delay between 2 and 5 seconds
print("Get ready...")
time.sleep(delay)  # Wait for the random delay


start_time = time.time()
print("GO!")
input()
end_time = time.time()
reaction_time = end_time - start_time
print(f"Your reaction time is: {reaction_time:.3f} seconds")
print("")
if reaction_time < 0.2:
    print("Insane!")
elif reaction_time < 0.5:
    print("Medium speed")
else:
    print("Your trash kid")
print("")
print("Feel free to join my Discord")
print("         👇👇👇")
print("discord.gg/FgM4zAw4qP")
print("")
input("Press enter to exit❌: ")
