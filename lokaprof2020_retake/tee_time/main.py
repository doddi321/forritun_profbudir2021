from tee_time import TeeTime

def print_error_when_adding(the_tee_time, player):
    # Here we try to add the given player to the tee time
    success = the_tee_time.add_player(player)
    if not success:
        print("Could not add player {} to tee time {}".format(player, the_tee_time.get_time()))

# Main starts here
# First create a tee time at 09:00 with three players
first_tee_time = TeeTime("09:00")
print_error_when_adding(first_tee_time, "Gummi")
print_error_when_adding(first_tee_time, "Magga")
print_error_when_adding(first_tee_time, "Sigga")
print(first_tee_time)

# Adding the fourth player is ok, but we should get an error when adding the fifth player
print_error_when_adding(first_tee_time, "Bjössi")
print_error_when_adding(first_tee_time, "Einsi")
print(first_tee_time)

# Remove two players
first_tee_time.remove_player("Magga")
first_tee_time.remove_player("Sigga")
# Trying to remove a player that is not part of the tee time does not have any effect
first_tee_time.remove_player("Bull")
print(first_tee_time)

# Create a second tee time at 09:10 and add three players to it
second_tee_time = TeeTime("09:10")
print_error_when_adding(second_tee_time, "Tom")
print_error_when_adding(second_tee_time, "Rachel")
print_error_when_adding(second_tee_time, "Bob")
print(second_tee_time)

# Merging means that we add players from the second tee time to the first until the first tee time is full. 
# We also have to remove the players from the second tee time that were added to the first.
first_tee_time.merge(second_tee_time)
print(first_tee_time)
print(second_tee_time)