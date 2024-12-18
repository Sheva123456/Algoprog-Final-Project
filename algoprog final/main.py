import pygame , time , random
from sys import exit 
from random import randint 
import random 

pygame.init()
screen = pygame.display.set_mode((1200,550))

pygame.display.set_caption("Friday Night Fightin'")

font = pygame.font.Font(None, 50)

notes = []
#starting player and enemy hp 
hp_x = 550
e_hp_x = 650 

NOTE_SIZE = (100, 100)


perfect = False 
great = False 
good = False
miss = False 

# Game states
Game_Over = False 
Game_Active = False 
Win = False 
Lose = False



#loading images for animation
#punch 1 
is_punching =False
punch1 = pygame.image.load('Animations/P_PUNCH_1/frame_0.gif')
punch2 =pygame.image.load('Animations/P_PUNCH_1/frame_1.gif')
punch3 =pygame.image.load('Animations/P_PUNCH_1/frame_2.gif')
punch4 =pygame.image.load('Animations/P_PUNCH_1/frame_3.gif')
punch5 =pygame.image.load('Animations/P_PUNCH_1/frame_4.gif')

#idle
idle1 = pygame.image.load('Animations/P_IDLE/f0.gif')
idle2 = pygame.image.load('Animations/P_IDLE/f1.gif')
idle3 = pygame.image.load('Animations/P_IDLE/f2.gif')
idle4 = pygame.image.load('Animations/P_IDLE/f3.gif')
idle5 = pygame.image.load('Animations/P_IDLE/f4.gif')
idle6 = pygame.image.load('Animations/P_IDLE/f5.gif')
idle7 = pygame.image.load('Animations/P_IDLE/f6.gif')
idle8 = pygame.image.load('Animations/P_IDLE/f7.gif')
idle9 = pygame.image.load('Animations/P_IDLE/f8.gif')

#kick
is_kicking=False
kick1 = pygame.image.load('Animations/P_KICK/kick 0.gif')
kick2 =pygame.image.load('Animations/P_KICK/kick 1.gif')
kick3 =pygame.image.load('Animations/P_KICK/kick 2.gif')
kick4 =pygame.image.load('Animations/P_KICK/kick 3.gif')
kick5 =pygame.image.load('Animations/P_KICK/kick 4.gif')
kick6 =pygame.image.load('Animations/P_KICK/kick 5.gif')

#hit 
player_hitted = False 
p_hit1 = pygame.image.load('Animations/P-HIT/phit 1.gif')
p_hit2 = pygame.image.load('Animations/P-HIT/phit 2.gif')
p_hit3 = pygame.image.load('Animations/P-HIT/phit 3.gif')
p_hit4 = pygame.image.load('Animations/P-HIT/phit 4.gif')
#block 
is_blocking = False 
p_block1 = pygame.image.load('Animations/P_BLOCK/block 0.gif')
p_block2 = pygame.image.load('Animations/P_BLOCK/block 1.gif')
p_block3 = pygame.image.load('Animations/P_BLOCK/block 2.gif')
p_block4 = pygame.image.load('Animations/P_BLOCK/block 3.gif')

#e idle 
e_idle1 = pygame.image.load('Animations/E-IDLE/idle 0.gif')
e_idle2 = pygame.image.load('Animations/E-IDLE/idle 1.gif')
e_idle3 = pygame.image.load('Animations/E-IDLE/idle 3.gif')
e_idle4 = pygame.image.load('Animations/E-IDLE/idle 4.gif')
e_idle5 = pygame.image.load('Animations/E-IDLE/idle 5.gif')
e_idle6 = pygame.image.load('Animations/E-IDLE/idle 6.gif')
e_idle7 = pygame.image.load('Animations/E-IDLE/idle 7.gif')
e_idle8 = pygame.image.load('Animations/E-IDLE/idle 8.gif')
e_idle9 = pygame.image.load('Animations/E-IDLE/idle 9.gif')
e_idle10 = pygame.image.load('Animations/E-IDLE/idle 10.gif')


#e block 
e_blocking = False 
hold_block = False 
e_block1 = pygame.image.load('Animations/E-BLOCK/eblock 0.gif')
e_block2 = pygame.image.load('Animations/E-BLOCK/eblock 1.gif')
e_block3 = pygame.image.load('Animations/E-BLOCK/eblock 2.gif')
e_block4 = pygame.image.load('Animations/E-BLOCK/eblock 3.gif')
e_block5 = pygame.image.load('Animations/E-BLOCK/eblock 4.gif')

e_block7 = pygame.image.load('Animations/E-BLOCK/eblock 6.gif')


#e hit
enemy_hit = 0 
e_hit1 = pygame.image.load('Animations/E-HIT/ehit 1.gif')
e_hit2 = pygame.image.load('Animations/E-HIT/ehit 2.gif')
e_hit3 = pygame.image.load('Animations/E-HIT/ehit 3.gif')
e_hit4 = pygame.image.load('Animations/E-HIT/ehit 4.gif')

#e kick 
e_kicking = False 
e_kick1 =  pygame.image.load('Animations/E-KICK/ekick 0.gif')
e_kick2 =  pygame.image.load('Animations/E-KICK/ekick 1.gif')
e_kick3 =  pygame.image.load('Animations/E-KICK/ekick 2.gif')
e_kick4 =  pygame.image.load('Animations/E-KICK/ekick 3.gif')
e_kick5 =  pygame.image.load('Animations/E-KICK/ekick 4.gif')
e_kick6 =  pygame.image.load('Animations/E-KICK/ekick 5.gif')







#=== PLAYER ANIMATIONS ===
player_punch1 = [punch1, punch2, punch3, punch4, punch5]
player_idle = [idle1, idle2, idle3, idle4, idle5, idle6, idle7, idle8, idle9]
player_kick = [kick1,kick2,kick3,kick4,kick5,kick6]
player_hit = [p_hit1, p_hit2, p_hit3, p_hit4]
player_block = [p_block1, p_block2, p_block3, p_block4]
player_die = []

for i in range (1, 26):
    framep = pygame.image.load(f'Animations/P-DIE/die {i}.gif')
    player_die.append(framep)

#===ENEMY ANIMATIONS ===
enemy_idle = [e_idle1, e_idle2, e_idle3, e_idle4,e_idle5, e_idle6,e_idle7,e_idle8,e_idle9,e_idle10]
enemy_block = [e_block1, e_block2, e_block3, e_block4, e_block5]
e_hit = [e_hit1, e_hit2, e_hit3, e_hit4]
e_kick = [e_kick1,e_kick2,e_kick3,e_kick4,e_kick5,e_kick6]
e_die = []

for i in range(1, 18):  
    frame = pygame.image.load(f'Animations/E-DIE/e_die{i}.gif')
    e_die.append(frame)



#note images 
note_Q = pygame.image.load('keyQ.png').convert_alpha()
note_W = pygame.image.load('keyW.png').convert_alpha()
note_A = pygame.image.load('keyA.png').convert_alpha()
note_S= pygame.image.load('keyS.png').convert_alpha()
note_Q= pygame.transform.scale(note_Q, NOTE_SIZE)
note_W=pygame.transform.scale(note_W, NOTE_SIZE)
note_A=pygame.transform.scale(note_A, NOTE_SIZE)
note_S=pygame.transform.scale(note_S, NOTE_SIZE)
# Define hit range thresholds (adjust these values as needed)
PERFECT_HIT_THRESHOLD = 200  # Distance in pixels for a perfect hit
GREAT_HIT_THRESHOLD =230    # Distance in pixels for a great hit
GOOD_HIT_THRESHOLD = 265     # Distance in pixels for a good hit
MISS_HIT_THRESHOLD = 266    # Distance in pixels for a good hit
hit_count_font = pygame.font.SysFont("Courier New", 50)
FPS = 50
# Class Note 
# Class Note
class Note: 
    def __init__(self , key, spawn_time, speed, image, length =0 ):
        # Initialize the note with its properties: key, spawn time, speed, image, and optional length
        self.key = key 
        self.spawn_time = spawn_time - 1000/(speed*FPS)  # Adjust spawn time to match game speed
        self.x = 1200  # Starting X position of the note
        self.speed = speed  # Speed of the note
        self.image = image  # Image associated with the note
        self.length = length  # Length of the note (defaults to 0 for regular notes)
        self.adjust_y_position()  # Adjust Y position based on the key
    
    def adjust_y_position(self):
        # Adjust Y position based on the key ('a' and 's' have different Y positions)
        if self.key == 'a' or self.key =='s':
            self.y = 450  
        else:
            self.y = 365  # Default Y for other notes
    
    def move(self):
        # Move the note leftward based on its speed
        self.x = self.x - self.speed  
    
    def current_position(self, x ):
        # Check if the current X position matches the given X
        return self.x == x 
    
    def remove_note_and_calculate_score(self, key):
        # Remove the note and calculate the score based on key match and position
        global  perfect, great, good, miss, enemy_hit, player_hitted  # Use global variables
        
        if key == self.key:  # Only check for scoring if the key matches
            if self.x <= PERFECT_HIT_THRESHOLD:
                # Award perfect score if the note is hit at the perfect position
                perfect = True 
                removed.append(self)  # Remove the note
            elif self.x <= GREAT_HIT_THRESHOLD: 
                # Award great score if the note is hit at the great position
                great = True
                removed.append(self)  # Remove the note
            elif self.x <= GOOD_HIT_THRESHOLD:
                # Award good score if the note is hit at the good position
                good = True
                removed.append(self)  # Remove the note
        else:
            if self.x < 100:  # Check for miss if the key does not match
                # Award miss score if the note is not hit in time
                miss = True 
                removed.append(self)  # Remove the note
    
    def block_remove_note_and_calculate_score(self):
        # Handle blocking notes and score calculations for 'a' and 's' keys
        global perfect_block, miss, player_hitted  # Use global variables
        
        if self.x <= 200:
            # Award perfect block score if the note is blocked successfully
            perfect_block = True 
            removed.append(self)  # Remove the note
        
        else:
            # Award miss score if the note is not blocked in time
            miss = True 
            player_hitted = True  # Set player hit flag
            removed.append(self)  # Remove the note

game_time = 0 
travel_time = 100  

# Class LongNote extends Note to handle long notes (which span over time)
class LongNote(Note):
    def __init__(self , key, spawn_time, speed, image, end_time):
        # Initialize the long note with properties like key, spawn time, speed, image, and end time
        super().__init__(key, spawn_time, speed, image, length = 0)
        self.x = 1200  # Starting X position of the long note
        self.length = (end_time - spawn_time) * speed*FPS  # Calculate length based on duration and speed
        self.initial_length = self.length  # Store initial length for reference
        self.height = 20  # Set height for long notes
        self.end_time = end_time  # End time of the long note
        self.length = (end_time - spawn_time) * speed*FPS  # Recalculate length to match duration
        self.adjust_y_position()  # Adjust Y position based on key
        self.hit_count = 0  # Track key presses for this long note
        self.required_hits = int((end_time - spawn_time) * 5)  # Required hits for scoring
        
    def move(self):
        # Move the note leftward and update the length to reflect its fading over time
        super().move()  # Call the move method from the parent class (Note)
        self.length = max(0, min(self.length + self.speed, self.initial_length))  # Update length
    
    def adjust_y_position(self):
        # Adjust Y position based on the key; call parent class method
        return super().adjust_y_position()
    
    def fade(self, amount):
        # Fade out the long note by reducing length and adjusting X position
        self.length -= amount + 40  # Determines how much the note fades away
        self.x += amount + 5  # Adjust position to simulate fading
    
    def check_active(self, game_time):
        # Check if the long note is active based on the current game time
        if self.spawn_time <= game_time <= self.end_time:
            return True
        return False 
    
    def draw(self):
        # Draw the long note on the screen based on its key
        if self.key == 'w':
            pygame.draw.line(screen, (242, 174, 182), (note.x + 25, (note.y + 50)), (note.x + 25 + note.length, note.y + 50), 50)  # Draw the line for 'w' key
        elif self.key == 'q':
            pygame.draw.line(screen, (95, 205, 228), (note.x + 25, (note.y + 50)), (note.x + 25 + note.length, note.y + 50), 50)  # Draw the line for 'q' key
    
    def register_hit(self):
        # Register a hit for the long note when it is pressed correctly
        self.hit_count += 1
        
    def long_remove_note_and_calculate_score(self):
        # Remove the long note and calculate the score based on hit count
        global  perfect, great, good , miss, player_hitted

        if self.hit_count >= self.required_hits:
            # Award perfect score if the required hits are met
            perfect = True 
        elif self.hit_count >= self.required_hits * 0.8:  # 80% threshold for great hit
            # Award great score for 80% hit threshold
           
            great = True 
        elif self.hit_count >= self.required_hits * 0.5:  # 50% threshold for good hit
            # Award good score for 50% hit threshold
            
            good = True 
        elif self.hit_count < self.required_hits * 0.5:  # Below 50% for miss
            # Award miss score if not enough hits
            miss = True 
        
        removed.append(self)  # Remove the long note



#======================PLAYER FUNCTIONS==================================# 
animation_speed = 2
animation_timer = 0 
current_frame_punch = 0
current_frame_idle = 0 
current_frame_kick = 0 
current_frame_hit = 0
current_frame_block = 0
current_frame_p_die = 0 
p_animation_timer = 0
def PPunch ():
    
    global  animation_timer, screen, is_punching, current_frame_punch, is_kicking, player_hitted
    if is_punching and not is_kicking and not player_hitted:
        animation_timer += 1 
        if current_frame_punch < len(player_punch1):
                        screen.blit( player_punch1[current_frame_punch], (450,120))
                        
                        if animation_timer >= animation_speed:
                            current_frame_punch += 1
                            animation_timer = 0 
        if current_frame_punch > len(player_punch1)-1: is_punching = False 
    else: 
        current_frame_punch = 0
        is_punching = False
def PKick ():
    global animation_timer, screen, is_kicking, current_frame_kick ,is_punching, player_hitted
    if is_kicking and not is_punching and not  player_hitted:
        animation_timer += 1
        if current_frame_kick < len(player_kick):
            screen.blit( player_kick[current_frame_kick], (450,120)) 
            
            if animation_timer >= animation_speed:
                            current_frame_kick += 1
                            animation_timer = 0 
        if current_frame_kick > len(player_kick)-1: is_kicking = False 
    else: 
        current_frame_kick = 0
        is_kicking = False
def PIdle ():
    global current_frame_idle, animation_timer, screen, is_punching, is_kicking, Lose 
    animation_speed = 4 
    if not is_punching and not is_kicking and not player_hitted and not is_blocking and not Lose :
        animation_timer += 1 
        if current_frame_idle < len(player_idle):
                        screen.blit( player_idle[current_frame_idle], (450,120))
                        
                        if animation_timer >= animation_speed:
                            current_frame_idle += 1
                            animation_timer = 0
        if current_frame_idle >= 9:
            current_frame_idle = 0
def PHit():
    global  is_kicking, current_frame_hit, player_hitted,animation_timer, is_blocking, Game_Over
    animation_speed = 5
    
    if player_hitted ==  True and not Game_Over:  
        is_blocking = False # If a miss has occurred
        animation_timer += 1
        if current_frame_hit < len(player_hit):
            screen.blit(player_hit[current_frame_hit], (380, 120))

            if animation_timer >= animation_speed:
                current_frame_hit += 1
                p_animation_timer = 0

        # Reset the animation after all frames are played
        if current_frame_hit >= len(player_hit):
            current_frame_hit = 0
            player_hitted= False  # Reset miss count after the animation ends
            
            

def PBlock():
    global   current_frame_block, is_blocking,animation_timer ,player_hitted, hold_block
    animation_speed = 4
    if is_blocking and not is_kicking and not is_punching and not player_hitted: 
        player_hitted = False # If a miss has occurred
        animation_timer += 1
        if current_frame_block < len(player_block):
            screen.blit(player_block[current_frame_block], (420, 120))

            if animation_timer >= animation_speed:
                current_frame_block += 1
                animation_timer = 0

        # Reset the animation after all frames are played
        if current_frame_block > len(player_block) - 1:
            current_frame_block = 0
            is_blocking= False
                # Reset miss count after the animation ends
            

            
def PDie():
    global current_frame_p_die, Game_Over, p_animation_timer, Lose 
    animation_speed = 3 
    p_animation_timer += 1  # Increment animation timer

    if Game_Over and Lose :
        text = font.render("Thanks for playing!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(600, 100))
        screen.blit(text, text_rect)
        if current_frame_p_die < len(player_die):  # Correct check for kicking animation
           
            screen.blit(player_die[current_frame_p_die], (320, 120))  # Display the current frame of the kick

            # Move to the next animation frame after waiting for the animation speed
            if p_animation_timer >= animation_speed:
                current_frame_p_die += 1 
                p_animation_timer = 0  # Reset the timer after advancing the frame

        # Once the kick animation finishes
        if current_frame_p_die >= len(player_die):  # If the animation is done

            current_frame_p_die = len(player_die) - 1 
            screen.blit(player_die[current_frame_p_die], (320,120))


    else:
        current_frame_p_die = 0  # Reset kick frame


#======================================ENEMY FUNCTIONS===================================# 
current_frame_e_block = 0 
current_frame_e_idle = 0 
current_frame_e_hit = 0
current_frame_e_kick = 0
current_frame_e_die = 0
e_animation_timer = 0
ek_animation_timer = 0
eh_animation_timer = 0
ed_animation_timer = 0 


def EBlock():
    global e_animation_timer, current_frame_e_block, e_blocking, e_kicking
    # Current time in milliseconds
    animation_speed = 0.2
    if e_blocking and not e_kicking:
        if current_frame_e_block < len(enemy_block):
            screen.blit(enemy_block[current_frame_e_block], (600, 120))
            e_animation_timer += 0.1
            if e_animation_timer >= animation_speed:
                current_frame_e_block += 1
                e_animation_timer = 0
        else:  # Animation finished
            current_frame_e_block = 0
            e_blocking = False

def EIdle():
    global current_frame_e_idle, e_animation_timer
    animation_speed = 3
    if not is_punching and not is_kicking and not e_blocking and not enemy_hit and not e_kicking and not Win:
        e_animation_timer += 1
        if current_frame_e_idle < len(enemy_idle):
            screen.blit(enemy_idle[current_frame_e_idle], (580, 120))

            if e_animation_timer >= animation_speed:
                current_frame_e_idle += 1
                e_animation_timer = 0
        if current_frame_e_idle >= 10:
            current_frame_e_idle = 0

def EHit():
    global eh_animation_timer, current_frame_e_hit, e_blocking, e_hit, e_hp_x, enemy_hit
    animation_speed = 6

    # Check if enemy is hit and play animation
    if enemy_hit:
        # Increment enemy health if hit
        e_hp_x += 10  # Decrease health when hit

        # Increment animation timer
        eh_animation_timer += 1

        # Play the hit animation
        if current_frame_e_hit < len(e_hit):
            screen.blit(e_hit[current_frame_e_hit], (580, 120))

            # Advance frame based on animation timer
            if eh_animation_timer >= animation_speed:
                current_frame_e_hit += 1
                eh_animation_timer = 0  # Reset animation timer
                enemy_hit = False

        # If animation is finished, reset variables
        if current_frame_e_hit >= len(e_hit):
            current_frame_e_hit = 0  # Reset animation frame
            enemy_hit = False        # Reset enemy hit status      
            e_blocking = False       # Reset blocking status
    else:
        # Reset to idle if no hit is happening
        current_frame_e_hit = 0
        enemy_hit = False

def EKick():
    global ek_animation_timer, current_frame_e_kick, e_kicking, is_blocking
    animation_speed = 3  # Controls the speed of the animation

    ek_animation_timer += 1  # Increment animation timer

    if e_kicking and not e_blocking:
        # If still kicking, increment the kick frame
        if current_frame_e_kick < len(e_kick):  # Correct check for kicking animation
            screen.blit(e_kick[current_frame_e_kick], (520, 120))  # Display the current frame of the kick

            # Move to the next animation frame after waiting for the animation speed
            if ek_animation_timer >= animation_speed:
                current_frame_e_kick += 1
                ek_animation_timer = 0  # Reset the timer after advancing the frame

        # Once the kick animation finishes
        if current_frame_e_kick >= len(e_kick):  # If the animation is done
            current_frame_e_kick = 0  # Reset the kick frame counter
            e_kicking = False  # Stop the kicking animation

    else:
        # If not kicking, reset the frame to the initial state
        current_frame_e_hit = 0  # Reset hit frame (if used for other purposes)
        current_frame_e_kick = 0  # Reset kick frame
        e_kicking = False  # Stop any animation

def EDie():
    global current_frame_e_die, ed_animation_timer
    
    animation_speed = 3
    ed_animation_timer += 1  # Increment animation timer

    if Game_Over and Win:
        text = font.render("Thanks for playing!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(600, 100))
        screen.blit(text, text_rect)

        # If still kicking, increment the kick frame
        if current_frame_e_die < len(e_die):  # Correct check for kicking animation
            screen.blit(e_die[current_frame_e_die], (520, 120))  # Display the current frame of the kick

            # Move to the next animation frame after waiting for the animation speed
            if ed_animation_timer >= animation_speed:
                current_frame_e_die += 1
                ed_animation_timer = 0  # Reset the timer after advancing the frame

        # Once the kick animation finishes
        if current_frame_e_die >= len(e_die):  # If the animation is done
            current_frame_e_die = len(e_die) - 1 
            screen.blit(e_die[current_frame_e_die], (520, 120))

    else:
        current_frame_e_die = 0  # Reset kick frame



def EKick():
    global perfect, great, good, enemy_hit, current_frame_e_kick, e_blocking, e_hit, successful_hit, e_hp_x, e_kicking, ek_animation_timer, enemy_hit, e_blocking, current_frame_e_hit, e_animation_timer
    animation_speed = 3  # Controls the speed of the animation

    ek_animation_timer += 1  # Increment animation timer


    if e_kicking:
        # If still kicking, increment the kick frame
        if current_frame_e_kick < len(e_kick):  # Correct check for kicking animation
           
            screen.blit(e_kick[current_frame_e_kick], (520, 120))  # Display the current frame of the kick

            # Move to the next animation frame after waiting for the animation speed
            if ek_animation_timer >= animation_speed:
                current_frame_e_kick += 1
                ek_animation_timer = 0  # Reset the timer after advancing the frame

        # Once the kick animation finishes
        if current_frame_e_kick >= len(e_kick):  # If the animation is done
            
            current_frame_e_kick = 0  # Reset the kick frame counter
            e_kicking = False  # Stop the kicking animation

    else:
        # If not kicking, reset the frame to the initial state
        current_frame_e_hit = 0  # Reset hit frame (if used for other purposes)
        current_frame_e_kick = 0  # Reset kick frame
        e_kicking = False  # Stop any animation

def EDie():
    global current_frame_e_die, Game_Over, ed_animation_timer
    
    animation_speed = 3 
    ed_animation_timer += 1  # Increment animation timer

    if Game_Over and Win :
        text = font.render("Thanks for playing!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(600, 100))
        screen.blit(text, text_rect)
        # If still kicking, increment the kick frame
        if current_frame_e_die < len(e_die):  # Correct check for kicking animation
           
            screen.blit(e_die[current_frame_e_die], (520, 120))  # Display the current frame of the kick

            # Move to the next animation frame after waiting for the animation speed
            if ed_animation_timer >= animation_speed:
                current_frame_e_die += 1
                ed_animation_timer = 0  # Reset the timer after advancing the frame

        # Once the kick animation finishes
        if current_frame_e_die >= len(e_die):  # If the animation is done

            current_frame_e_die = len(e_die) - 1 
            screen.blit(e_die[current_frame_e_die], (520,120))


    else:
        current_frame_e_die = 0  # Reset kick frame
        



# spawning notes on the map
note_pattern = [
    Note(spawn_time = 0.23, key='q', speed = 20, image = note_Q, length = 0),
Note(spawn_time = 1.73, key='a', speed = 20, image = note_A, length = 0),
LongNote(spawn_time = 3.48, end_time = 4.79, key='w', speed = 20, image = note_W),
Note(spawn_time = 5.23, key='s', speed = 20, image = note_S, length = 0),
Note(spawn_time = 6.73, key='q', speed = 20, image = note_Q, length = 0),
Note(spawn_time = 8.23, key='a', speed = 20, image = note_A, length = 0),
LongNote(spawn_time = 9.98, end_time = 11.33, key='w', speed = 20, image = note_W),
Note(spawn_time = 11.73, key='s', speed = 20, image = note_S, length = 0),
Note(spawn_time = 13.23, key='q', speed = 20, image = note_Q, length = 0),
LongNote(spawn_time = 14.98, end_time = 16.58, key='w', speed = 20, image = note_W),
Note(spawn_time = 16.73, key='s', speed = 20, image = note_S, length = 0),
Note(spawn_time = 18.23, key='w', speed = 20, image = note_W, length = 0),
Note(spawn_time = 19.73, key='q', speed = 20, image = note_Q, length = 0),
LongNote(spawn_time = 21.23, end_time = 22.73, key='w', speed = 20, image = note_W),
Note(spawn_time = 23.73, key='a', speed = 20, image = note_A, length = 0),
Note(spawn_time = 25.23, key='s', speed = 20, image = note_S, length = 0),
LongNote(spawn_time = 26.98, end_time = 28.28, key='w', speed = 20, image = note_W),
Note(spawn_time = 28.73, key='q', speed = 20, image = note_Q, length = 0),
Note(spawn_time = 30.23, key='s', speed = 20, image = note_S, length = 0),
Note(spawn_time = 31.73, key='w', speed = 20, image = note_W, length = 0),
LongNote(spawn_time = 33.23, end_time = 34.73, key='q', speed = 20, image = note_Q),
Note(spawn_time = 35.23, key='a', speed = 20, image = note_A, length = 0),
Note(spawn_time = 36.73, key='s', speed = 20, image = note_S, length = 0),
Note(spawn_time = 38.23, key='w', speed = 20, image = note_W, length = 0),
LongNote(spawn_time = 40.23, end_time = 41.43, key='q', speed = 20, image = note_Q),
Note(spawn_time = 42.23, key='a', speed = 20, image = note_A, length = 0),
Note(spawn_time = 43.73, key='s', speed = 20, image = note_S, length = 0),
Note(spawn_time = 45.23, key='w', speed = 20, image = note_W, length = 0),
LongNote(spawn_time = 47.23, end_time = 48.53, key='q', speed = 20, image = note_Q),
Note(spawn_time = 49.23, key='a', speed = 20, image = note_A, length = 0),
Note(spawn_time = 50.73, key='s', speed = 20, image = note_S, length = 0),
LongNote(spawn_time = 52.73, end_time = 54.03, key='w', speed = 20, image = note_W),
Note(spawn_time = 54.73, key='q', speed = 20, image = note_Q, length = 0),
Note(spawn_time = 56.23, key='a', speed = 20, image = note_A, length = 0),
Note(spawn_time = 57.73, key='s', speed = 20, image = note_S, length = 0),
Note(spawn_time = 59.23, key='w', speed = 20, image = note_W, length = 0),
Note(spawn_time = 60.73, key='q', speed = 20, image = note_Q, length = 0),

    
    
]   
    
start_time = 60
def display_time():
    
    remaining_time = max(0, start_time - int(game_time))  # Ensure the timer doesn't go below 0
    
    # Render the remaining time
    duration = font.render(f'{remaining_time}', False, 'White')
    
    # Set the position of the text
    dur_rect = duration.get_rect(center=(600, 30))  # Adjust (600, 30) as needed for your screen layout
    
    # Display the time on the screen
    screen.blit(duration, dur_rect)
    
    return duration

duration = 0 

# time and clock
# ------------------------------------
clock = pygame.time.Clock()

gst = time.time()
removed = []  # Temporary list for notes to be removed
miss=[]



running = True
surface = pygame.image.load('Background.png')
hold_start = {} 

game_over_time = 0 
while running:
    print(enemy_hit)  # Print enemy hit status for debugging

    if not Game_Over:
        game_time = time.time() - gst  # Update game time only when the game is running
    else:   
        removed = []  # If game over, remove all notes
        notes = []

    # Event handling
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if not Game_Over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Handle Q key press
                
                    is_kicking = False
                    is_punching = True
                    if not perfect or not great or not good or miss:
                        e_blocking = True
                        enemy_hit = False

                    # Handle notes corresponding to the Q key
                    for note in notes: 
                        if note.length == 0 and note.key == 'q' and 140 < note.x <= GOOD_HIT_THRESHOLD:
                            note.remove_note_and_calculate_score('q')
                            break  # Exit loop after handling one note

                        elif note.length > 0 and note.key == 'q' and note.check_active(game_time):
                            note.register_hit()
                            break

                if event.key == pygame.K_w:  
                    is_punching = False
                    is_kicking = True
                    
                    if not perfect or not great or not good or miss:
                        if not e_blocking:  # Only start blocking if not already blocking
                            e_blocking = True
                            enemy_hit = False 

                    # Handle notes corresponding to the W key
                    for note in notes: 
                        if note.length == 0 and note.key == 'w' and 140 < note.x <= GOOD_HIT_THRESHOLD:
                            note.remove_note_and_calculate_score('w')
                            break  # Exit loop after handling one note
                        
                        elif note.length > 0 and note.key == 'w' and note.check_active(game_time):
                            note.register_hit()
                            break

                if event.key == pygame.K_a:  
                    is_blocking = True
                    # Handle notes corresponding to the A key
                    for note in notes: 
                        if note.length == 0 and note.key == 'a' and 140 < note.x <= GOOD_HIT_THRESHOLD:
                            note.block_remove_note_and_calculate_score()
                            break  # Exit loop after handling one note
                        
                        elif note.length > 0 and note.key == 'a' and note.check_active(game_time):
                            note.register_hit()
                            break

                if event.key == pygame.K_s: 
                    is_blocking = True 
                    # Handle notes corresponding to the S key
                    for note in notes:  
                        if note.length == 0 and note.key == 's' and 120 < note.x <= GOOD_HIT_THRESHOLD:
                            note.block_remove_note_and_calculate_score()
                            break   # Exit loop after handling one note
                        elif note.length > 0 and note.key == 's' and note.check_active(game_time):
                            note.register_hit()
                            break
                
            if event.type == pygame.KEYUP:
                hold_block = False
                if event.key in [pygame.K_q, pygame.K_w]:
                    # When the key is released, evaluate the score for the LongNote
                    for note in notes:
                        if isinstance(note, LongNote) and not note.check_active(game_time):
                            note.long_remove_note_and_calculate_score()
                            break

        # Handle Game Over condition
        if Game_Over:
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_SPACE:
                    pass
                else:
                    Game_Over = False

#============ENEMY HIT PROBABILITY============#

    # Update enemy hit probability for notes with key 'a' or 's' and x position thresholds
    for note in notes: 
        if note.key in ['a', 's'] and note.x < 50 and note.length == 0:
            hp_x -= 80
            player_hitted = True 
            removed.append(note)

    # Update enemy kick probability based on note position
    for note in notes: 
        if note.key in ['a', 's'] and note.x < 350 and note.length == 0: 
            e_kicking = True 

    # Adjust probability of blocking for perfect, great, good, and miss conditions
    if perfect:
        if random.random() <= 0.3:
            e_blocking = True
        else:
            e_blocking = False
            enemy_hit = True
        perfect = False
        
    if great:
        if random.random() < 0.7:
            e_blocking = True
        else:
            e_blocking = False
            enemy_hit = True
        great = False

    if good:
        if random.random() < 0.8:
            e_blocking = True
        else:
            e_blocking = False
            enemy_hit = True
        good = False

    if miss:
        e_blocking = True
        miss = False
    
# Screen updates
    screen.fill((0, 0, 0))
    screen.blit(surface, (0, 0))  # Draw background
    pygame.draw.line(screen, (128, 128, 128), (200, 361), (200, 550), 92)  # Draw the note bar
    health_bar = pygame.draw.line(screen, (9, 121, 105), (20, 30), (hp_x, 30), 30)  # Draw player health bar
    e_health_bar = pygame.draw.line(screen, (9, 121, 105), (e_hp_x, 30), (1180, 30), 30)  # Draw enemy health bar
    
    #=======WIN LOSE CONDITIONS =========#
    if hp_x <= 20:
        hp_x = 20 
        if not Game_Over:
            game_over_time = time.time() - gst  # Capture the time at the game over moment
            Game_Over = True
            Lose = True 
    if e_hp_x >= 1180:
        e_hp_x = 1180
        if not Game_Over:
            game_over_time = time.time() - gst  # Capture the time at the game over moment
            Game_Over = True
            Win = True 
    
    if game_time > 60:
        if not Game_Over:
            game_over_time = time.time() - gst  # Capture the time at the game over moment
            Game_Over = True
            Win = True 
        
    #====================================#

    PPunch()
    PKick()
    PIdle()
    PHit()
    PBlock()
    EIdle()
    EBlock()
    EHit()
    EKick()
    EDie()
    PDie()

    if not Game_Over:
        display_time()  # Display the current game time

    # Spawn notes if it's their time
    for note in note_pattern:
        if game_time >= note.spawn_time and note not in notes:
            notes.append(note)
    
    for note in removed:
        notes.remove(note)

    # Move and draw all notes
    for note in notes:
        if isinstance(note, LongNote):  # Check if it's a LongNote
            note.draw()
            screen.blit(note.image, (note.x, note.y))
            
        note.move()

        if note not in removed:
            screen.blit(note.image, (note.x, note.y))

    pygame.display.flip()  # Update the display
    pygame.display.update()
    clock.tick(FPS)  # Control the game's frame rate
