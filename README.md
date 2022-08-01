# Pymap

## Public Notice 🦉
PyMap was a fun project that I worked on as a part of my Major Work. It was originally much more complex but then I had to cut it down. This version was built in a lot shorter amount of time as i wasn't very smart about putting stuff in the cloud. Anyhow, the features come pretty basic but there is still refining to do. You can install it however you will need to run a requirements file. 
## Demo

[![demo](https://yt-embed.herokuapp.com/embed?v=pKOSG7_dsTw)](https://www.youtube.com/watch?v=pKOSG7_dsTw "Thing i made")


## Data dictionaries
### src.player.Player
| Name                         	| Type                 	| Description                                                                                                                                                                                                                                                                       	| Value                                                   	|
|------------------------------	|----------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|---------------------------------------------------------	|
| console_thread               	| threading.Thread     	| Allows for the console to run concurrently to the main program                                                                                                                                                                                                                    	| threading.Thread                                        	|
| player                       	| class object         	| player is a redundant class object that was intended to allow for songs to be played but instead this was done through the window class                                                                                                                                           	| object                                                  	|
| player.song-index            	| int                  	| allows for a list of songs to be indexed                                                                                                                                                                                                                                          	| 0                                                       	|
| player.volume                	| int                  	| allows for the volume to be changed when using pygame.Mixer.Channel                                                                                                                                                                                                               	| 1                                                       	|
| player.shuffle               	| boolean              	| if songs are to be shuffled or not                                                                                                                                                                                                                                                	| False                                                   	|
| player.crossfade             	| boolean              	| if songs are to be faded in between each other. This can also be done by creating 2 channel instances and fading both in/out relatively                                                                                                                                           	| False                                                   	|
| player.song_list             	| str array            	| an array of strings which can be then loaded with pygame.mixer to play an audio file                                                                                                                                                                                              	| null                                                    	|
| player.song_channel          	| pygame.mixer.Channel 	| A channel object which controls audio, volume etc                                                                                                                                                                                                                                 	| pygame.mixer.Channel                                    	|
| player.songs                 	| null                 	| not implemented in final release                                                                                                                                                                                                                                                  	| null                                                    	|
### src.window.Window
| Name                         	| Type                 	| Description                                                                                                                                                                                                                                                                       	| Value                                                   	|
|------------------------------	|----------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|---------------------------------------------------------	|
| window.settings              	| dict                 	| a list of settings that contain things such as the last window state etc. this was not implemented very well in the end                                                                                                                                                           	| {}                                                      	|
| window.running               	| boolean              	| for the program loop. This flag dictates the program state as running or not. When this flag is changed then the loop ceases to repeat.                                                                                                                                           	| True                                                    	|
| window.display               	| pygame.display       	| pygame uses various C features of SDL and allows for windows to be drawn onto the screen. self.display is for such purpose.                                                                                                                                                       	| pygame.display                                          	|
| window.dw,window.dh          	| int, int             	| the window dimensions that are then passed into the above variable of window.display                                                                                                                                                                                              	| 1280,720                                                	|
| window.clock                 	| time.Clock           	| This controls when a frame is allowed to refresh. It means that an fps vale can be set and instead of being bottlenecked by the speed of the hardware it is now set so that it is capped at the fps                                                                               	| pygame.Clock                                            	|
| window.toolbar_group_icon    	| pygame.Group         	| This group icon holds all of the toolbar icons that are made which are handled in seperate classes                                                                                                                                                                                	| object                                                  	|
| window.preview_popup         	| pygame.GroupSingle   	| This contains a single group. The reason why i did it this way and inheristed pygmame.sprite.Sprite instead of  just making an object is because this allows for inherited functions such as draw and update which is just one more thing that i don't really have to worry about 	|``` pygame.sprite.GroupSingle ```                              	|
| self.tb_w,self.tb_h          	| int, int             	| This is the dimensions of the popup windows                                                                                                                                                                                                                                       	| 450,250                                                 	|
| window.install_wizard_page   	| int                  	| The install wizard screens are controlled by integers. in window.py file, the conditionals dictate whether a screen has been updated or not. By incrementing this variable, a conditional is released.                                                                            	| 0                                                       	|
| window.main_program_font     	| pygmae.font          	| The font object, this does not render stuff nor is a ttf file or anything like that. This just sets a constant value containing paramaters: font type, size, bold, italic.                                                                                                        	| ```pygame.font.SysFont('candara', 24, bold=True)```           	|
| window.program_h1_title_text 	| pygame.surface       	| This is a rendered surface of specific text. with different parameters to the variable above such as antialiasing, color, bg color etc and things that as specific  to a surface                                                                                                  	| ```self.main_program_font.render("PyMap", 1, (255,255,255))``` 	|
### src.utils.load_settings
| Name          	| Type     	| Description                                                       	| Value           	|
|---------------	|----------	|-------------------------------------------------------------------	|-----------------	|
| data          	| dict     	| This data dictionary is for storing the settings file information 	| {}              	|
| file          	| str      	| the file to load in pythons fileio system with open(file)         	| 'settings.json' 	|
| load_settings 	| function 	| the function that stores the information and does the processing  	|                 	|               	|          	|                                                                   	|                 	|

### src.utils.save_settings
| Name          	| Type       	| Description                                                       	| Value    	|
|---------------	|------------	|-------------------------------------------------------------------	|----------	|
| save_settings 	| function   	| The function that stores the information and does the processing. 	| function 	|
| file          	| str        	| the file to load in pythons fileio system with open(file)         	| (anychar).json   	|
| data          	| dictionary 	| data stores the loaded information that is passed from the file   	| {}       	|
| f             	| object     	| the file object that can be accessed and loaded information from  	| file.io  	|

### src.utils.get_display_size
| Name              	| Type           	| Description                                                                                                                	| Value                 	|
|-------------------	|----------------	|----------------------------------------------------------------------------------------------------------------------------	|-----------------------	|
| get_display_size  	| function       	| The function that stores the information and does the processing.                                                          	| function              	|
| screen            	| pygame.Surface 	| the display that is made temporary and is just for getting the size of the window so that sys does not have to be imported 	| class(pygame.display) 	|
| x                 	| int            	| the saved x value from screen.get_size()                                                                                   	| {}                    	|
| y                 	| int            	| the saved y value from screen.get_size()                                                                                   	| file.io               	|
| screen.get_size() 	| tuple          	| returns the x and y of a surface                                                                                           	| relative to screen    	|

### src.utils.install_samples
| Name            	| Type       	| Description                                                                                                                                  	| Value        	|
|-----------------	|------------	|----------------------------------------------------------------------------------------------------------------------------------------------	|--------------	|
| install_samples 	| function   	| function which holds, loads sends and processes data. This function is for installing songs using the requests module                        	| returns null 	|
| progress        	| global     	| inherited from global scope. Progress is set in conjunction with the src.progressBar class                                                   	| 0            	|
| done            	| global     	| inherited from global scope. 'Done' is a boolean value to state if the samples install has been completed.                                   	| False        	|
| data            	| dictionary 	| data is a value to store the loaded data from file. In this case the data is then later indexed in a for loop  in the following code segment 	| {}           	|

### src.utils.data_size
| Name      	| Type       	| Description                                                                                                                                                                                     	| Value       	|
|-----------	|------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|-------------	|
| data_size 	| function   	| Function which loads holds sends and processes data. in this case data_size is to get the amount of install sample songs for the progress bar later referenced in src.progbar.ProgressBar class 	| returns int 	|
| data      	| dictionary 	| data is for holding the json data that is passed into the data_size function as a file argument (file bieng a string but not referenced in this data dictionary as it is a parameter            	| {}          	|
| songs     	| list       	| contains string song urls which are loaded from aforementioned data variable                                                                                                                    	| []          	|

### src.textbox.TextBox.__init__
| Name                            	| Type                                        	| Description                                                                                                                                                                                                   	| Value                       	|
|---------------------------------	|---------------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------	|
| TextBox                         	| object(inherited from pygame.sprite.Sprite) 	| class which as stated previously, inherits both functions and class variables of the pygame.sprite.Sprite class which now allocates text box as a class which is treated as a sprite by the program           	| does not have a return type 	|
| ```__init__```                  	| constructor                                 	| this constructor holds the class variables as well as inherits the inherited class by doing ```pygame.sprite.Sprite.__init__(self)```                                                                         	| {}                          	|
| TextBox.constructor.image       	| pygame.Surface                              	| whenever a sprite is created, pygame will need a default image value. In this case, it is set as pygmae.Surface                                                                                               	| pygame.Surface              	|
| TextBox.constructor.rect        	| pygame.Rect                                 	| similar to the previous variable, pygame also recommends a rect value as each surface only has a width and a height so it is needing a rect to have (x, y, width, height) which can be updated as the surface 	| pygame.Rect                 	|
| TextBox.constructor.description 	| str                                         	| This description is a string value that is later rendered as an actual piece of text that can be drawn on the pygame display.                                                                                 	| null                            	|


## Data flow diagram

<img src="https://raw.githubusercontent.com/JoshuaDRose/PYMAP/41a7af1627227ab8e981cd2968a038c3eb784e91/docs/MAJOR%20WORK%20DFD.svg"
     alt="Markdown Monster icon"
     width="500"
     style="float: left; margin-right: 10px;" />

## Credits 
Credit where credit is due so i dont fail :)


### Art
The art that I used in this project was sourced directly from https://opengameart.org/content/game-icons. 
The author of the icons on the site has the copyright section as the following.<br>
**Copyright/Attribution Notice:**<br>
Credit "Kenney.nl" or "www.kenney.nl"<br>
So full credit goes to the individual above.
### Colors 
I got the colors from https://www.schemecolor.com/ as well as https://freebiesupply.com/free-psd-misc/music-player-web-ui-design-psd-freebie/

### Inspiration 
Some inspriation for the UI/design layout of this project came from this image: https://i.pinimg.com/originals/20/29/24/202924ad793b1e89670539cfaa4e0d4f.png

Side note:
> I regretfully spent only 12 hours building this as I left my computer at school and it was exams and i dislike myself. Its almost 1 am and i have exams tomorrow.




<img src="https://raw.githubusercontent.com/JoshuaDRose/JoshuaDRose/main/image_2022-07-31_235732925.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
