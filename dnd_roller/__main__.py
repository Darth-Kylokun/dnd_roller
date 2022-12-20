from random import randint

def roll_dice(dice_str: str) -> tuple[int, int, int, list[int] | None]:
    amount, dice = dice_str.split('d')
    if dice_str[0] == 'i':
        amount = amount[1:]
        
        total = 0
        crits = 0
        crit_fails = 0
        dice = int(dice)
        rolls = []
        
        for _ in range(int(amount)):
            roll = randint(1, dice)
            rolls.append(roll)
            if dice == 20 and roll == 20:
                crits += 1
                
            if dice == 20 and roll == 1:
                crit_fails += 1
            
            total += roll
            
        return total, crits, crit_fails, dice, rolls
    else:
        if amount == '':
            roll = randint(1, int(dice))
            if dice == 20 and roll == 20:
                return roll, 1, dice
            return roll, 0, 0, dice, None
        
        total = 0
        crits = 0
        dice = int(dice)
        crit_fails = 0
        
        for _ in range(int(amount)):
            roll = randint(1, dice)
            if dice == 20 and roll == 20:
                crits += 1
                
            if dice == 20 and roll == 1:
                crit_fails += 1
            
            total += roll
            
        return total, crits, crit_fails, dice, None
        

def main() -> None:
    while 1:
        dice_str = input('Roll: ')
        dice_roll, crits, fails, dice, rolls = roll_dice(dice_str)
        
        print('')
        
        if rolls is None:
            if dice == 20:
                print(f'You rolled a {dice_roll} from {dice_str}, got {crits} crits, and {fails} fails.')
            else:
                print(f'You rolled a {dice_roll} from {dice_str}.')
        else:
            [print(f'Roll {i+1}: {r}') for i, r in enumerate(rolls)]
            print('')
            if dice == 20:
                print(f'You rolled a {dice_roll} from {dice_str[1:]}, got {crits} crits, and {fails} fails.')
            else:
                print(f'You rolled a {dice_roll} from {dice_str}.')
                
        print('')

if __name__ == '__main__':
    main()