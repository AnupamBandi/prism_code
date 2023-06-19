# this is the pseudo code or algo which i have come up with in recursion
# Here this code gives us all the possible ways to handle the situation 

# circle represents the value of circle he is in.
# p be the regenerative or initial power
#  currPower is the power of abhimanyu at that instant
# enemy power an array which contains the value of enemies at each circle
# skip remaining tells the number of skips remaining(a)
# recharge remaining tells number of recharges are remained(b)




def rec(circle, p, curr_power, enemy_powers, skips_remaining, recharge_remaining):
    if circle == 12:
        return True  # Abhimanyu successfully crossed all circles
    
    # Default: set the value of answer as False
    ans = False
    
    # defend is the amount of power Abhimanyu needs to defeat the enemy
    # If circle is 4 or 8, he needs to fight both enemies (at that circle and the previous circle with half power)
    defend = enemy_powers[circle] + (enemy_powers[circle - 1] // 2 if circle == 4 or circle == 8 else 0)
    
    if curr_power < defend:
        if recharge_remaining > 0 and p >= defend:
            # Update the circle, set curr_power to p - defend, decrement the recharge
            ans |= rec(circle + 1, p, p - defend, enemy_powers, skips_remaining, recharge_remaining - 1)
        
        if skips_remaining > 0:
            # Update the circle, decrement the skips
            ans |= rec(circle + 1, p, curr_power, enemy_powers, skips_remaining - 1, recharge_remaining)
    else:
        # If curr_power >= defend, defend and move to the next circle
        ans |= rec(circle + 1, p, curr_power - defend, enemy_powers, skips_remaining, recharge_remaining)
        
        if recharge_remaining > 0:
            # If recharge is possible, recharge
            ans |= rec(circle + 1, p, p - defend, enemy_powers, skips_remaining, recharge_remaining - 1)
        
        if skips_remaining > 0:
            # If skipping is possible, skip
            ans |= rec(circle + 1, p, curr_power, enemy_powers, skips_remaining - 1, recharge_remaining)
    
    return ans

# Test case
# enemy_powers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
# p = 100
# skips_remaining = 3
# recharge_remaining = 2
# print(rec(1, p, curr_power, enemy_powers, skips_remaining, recharge_remaining))  # Output: True
# as u can go till circle 4 and regenerate and go to circle 6 and regenerate go to 7 and skip 8 can defend 9th and move to 9 and can skip 10 and 11.

#  test case 2
#  enemy_powers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
#  p = 150
#  skips_remaining = 2
#  recharge_remaining = 1
#  print(rec(1, p, curr_power,enemy_powers, skips_remaining, recharge_remaining)) # Output: False
# cannot proceed till last in any case  