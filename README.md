# Persona 

## Demo
Demo Video: <https://youtu.be/5pqtKRtyrLo>

## GitHub Repository
GitHub Repo: <https://github.com/epfoshe/Persona.git>

## Description
My original idea for the project was to create a more detailed rain animation with the inspiration of the Persona Games.
However I decided to take this idea and make it into an interactive screensaver with no apparent theme. 

I have multiple python files in my repository denoting different things. The original project file was not able to take the commands I had outlined and reformed, so I had to resave the thunder_test file to the project file.
Besides that mishap, the other files included are the raindrop_2 png file, the jason scheier illustration jpeg images, and both sounds for the rain and the thunder. 

I took the environmental artwork Jason Scheier created and edited it within Clip Studio Paint to make a thunder counterpart for the scene. Then I began coding by initializing pygame functions and creating an outline of what needed to be done. 
The illustration photos had to be implemented through pygame.image.load combined with the ability to convert them since they are jpegs. Also, they had to fit the screen resolution of 1920 x 1080 and had to be changed. 
I defined an area of code dedicted to the rain, raindrops, game event loop, updates, and screen. By doing this I could define what areas would need to be returned to or not. I used a grid method for the rain to have space for the raindrops to fall in the animation.
I created a rain source file detailing the conditions of the raindrop such as the size and speed it would fall. I used random.randrange to achieve random intervals/spacing/speed/etc in my code. 
For the game event loop, I used the event.type features of pygame to distinguish K_SLASH as thunder and produce a sound effect and image along with it. When the button lifted up again, the background and sound would revert back to the original form. 
The raindrops created are looped to reset at the top of y cordinate 0 to then fall again as a rain animation. 

In conclusion, I would have liked to develop more game loop features or animations for my interactive screensaver. These such things could include splash animations or maybe a different weather event. 
Additionally, I believe the cleanliness and organization of my files could have been developed a lot more. I think my code is a bit disorganized and could be considered disorderly. 


