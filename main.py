# my manifesto about how much i hate 

import random
import asyncio
import warnings
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)


BANNER = """
 333333333333333      1111111         000000000                  CCCCCCCCCCCCC                AAA                   SSSSSSSSSSSSSSS  IIIIIIIIII NNNNNNNN        NNNNNNNN      OOOOOOOOO     
3:::::::::::::::33   1::::::1       00:::::::::00             CCC::::::::::::C               A:::A                SS:::::::::::::::S I::::::::I N:::::::N       N::::::N    OO:::::::::OO   
3::::::33333::::::3 1:::::::1     00:::::::::::::00         CC:::::::::::::::C              A:::::A              S:::::SSSSSS::::::S I::::::::I N::::::::N      N::::::N  OO:::::::::::::OO 
3333333     3:::::3 111:::::1    0:::::::000:::::::0       C:::::CCCCCCCC::::C             A:::::::A             S:::::S     SSSSSSS II::::::II N:::::::::N     N::::::N O:::::::OOO:::::::O
            3:::::3    1::::1    0::::::0   0::::::0      C:::::C       CCCCCC            A:::::::::A            S:::::S               I::::I   N::::::::::N    N::::::N O::::::O   O::::::O
            3:::::3    1::::1    0:::::0     0:::::0     C:::::C                         A:::::A:::::A           S:::::S               I::::I   N:::::::::::N   N::::::N O:::::O     O:::::O
    33333333:::::3     1::::1    0:::::0     0:::::0     C:::::C                        A:::::A A:::::A           S::::SSSS            I::::I   N:::::::N::::N  N::::::N O:::::O     O:::::O
    3:::::::::::3      1::::l    0:::::0 000 0:::::0     C:::::C                       A:::::A   A:::::A           SS::::::SSSSS       I::::I   N::::::N N::::N N::::::N O:::::O     O:::::O
    33333333:::::3     1::::l    0:::::0 000 0:::::0     C:::::C                      A:::::A     A:::::A            SSS::::::::SS     I::::I   N::::::N  N::::N:::::::N O:::::O     O:::::O
            3:::::3    1::::l    0:::::0     0:::::0     C:::::C                     A:::::AAAAAAAAA:::::A              SSSSSS::::S    I::::I   N::::::N   N:::::::::::N O:::::O     O:::::O
            3:::::3    1::::l    0:::::0     0:::::0     C:::::C                    A:::::::::::::::::::::A                  S:::::S   I::::I   N::::::N    N::::::::::N O:::::O     O:::::O
            3:::::3    1::::l    0::::::0   0::::::0      C:::::C       CCCCCC     A:::::AAAAAAAAAAAAA:::::A                 S:::::S   I::::I   N::::::N     N:::::::::N O::::::O   O::::::O
3333333     3:::::3 111::::::111 0:::::::000:::::::0       C:::::CCCCCCCC::::C    A:::::A             A:::::A    SSSSSSS     S:::::S II::::::II N::::::N      N::::::::N O:::::::OOO:::::::O
3::::::33333::::::3 1::::::::::1  00:::::::::::::00         CC:::::::::::::::C   A:::::A               A:::::A   S::::::SSSSSS:::::S I::::::::I N::::::N       N:::::::N  OO:::::::::::::OO 
3:::::::::::::::33  1::::::::::1    00:::::::::00             CCC::::::::::::C  A:::::A                 A:::::A  S:::::::::::::::SS  I::::::::I N::::::N        N::::::N    OO:::::::::OO   
 333333333333333    111111111111      000000000                  CCCCCCCCCCCCC AAAAAAA                   AAAAAAA  SSSSSSSSSSSSSSS    IIIIIIIIII NNNNNNNN         NNNNNNN      OOOOOOOOO\n\n\n\n"""
 
run_banner = True   #? Set this to False if you dont want to emulate loading screen

while run_banner == True:
    async def print_banner():
        stop_delay = 0
        stop_delay_num = random.randint(100, 250)
        print(stop_delay_num)
        BANNER_PRINT = """ """
        for letter in BANNER:
            print('\n\n\nLOADING GAME')
            BANNER_PRINT += letter
            os.system('cls')
            print(BANNER_PRINT)
            if stop_delay < stop_delay_num:
                delay_random = random.randint(1, 15)
                print('\n\n\nInitalizing Assets')
                print(stop_delay, '/', stop_delay_num )
                
                stop_delay += 1
                await asyncio.sleep(delay_random * .01)
        
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(print_banner())
    run_banner = False


    
run_game = True
wallet_amount = int(100)

while run_game == True:
    print(f"Wallet: {wallet_amount}")
    print('==========\nWelcome to 310 Casnio\nSelect game to play\n\n1: Coin Flip\n2: BlackJack\n==========')
    def SLOTS(input1= int(input("Select Game: "))):
        end_game_decision =  ''
        global wallet_amount
        global run_game
        if input1 == 1:
            while run_game == True:
                os.system('clear')
                print(BANNER)
                print(f"Wallet: {wallet_amount}\n\n")
                coin_flip = random.randint(1, 2)
                bet_amount = int(input("Enter Bet amount: "))
                while bet_amount > wallet_amount and bet_amount > 0:
                    if bet_amount > wallet_amount:
                        print('Insufficent Funds')
                        bet_amount = int(input("Enter Bet amount: "))
                    else:
                        print('No negatives or non numberical values')
                        bet_amount = int(input("Enter Bet amount: "))
                if bet_amount == wallet_amount:
                    are_you_sure = str(input('ALL IN?\nAre you sure you want to go all in? y/n\n(y:Yes | n:No)'))
                    if are_you_sure.upper() == "N":
                        bet_amount = int(input("Enter Bet amount: "))
                user_decision = int(input("Heads or Tails?\n\n1: Heads\n2: Tails\n\n"))
                if user_decision == 1 and coin_flip == 1:
                    wallet_amount += bet_amount
                    print(f"\nCongradulations it was Heads! ${bet_amount} has been added to your wallet. \n\nCurrent Wallet Balance: {wallet_amount}\n" )
                    end_game_decision = input('Continue playing? y/n\n(y:Yes | n:No)')
                if user_decision == 2 and coin_flip == 2:
                    wallet_amount += bet_amount
                    print(f"\nCongradulations it was Tails! ${bet_amount} has been added to your wallet! \n\nCurrent Wallet Balance: {wallet_amount}\n")
                    end_game_decision = input('Continue playing? y/n\n(y:Yes | n:No)')
                else:
                    if user_decision == 1:
                        wallet_amount -= bet_amount
                        print(f"\nSorry, it was Tails. ${bet_amount} has been deducted from your wallet. \n\nCurrent Wallet Balance: {wallet_amount}\n")
                        end_game_decision = input('Continue playing? y/n\n(y:Yes | n:No)')
                    else:
                        wallet_amount -= bet_amount
                        print(f"\nSorry, it was heads. ${bet_amount} has been deducted from your wallet. \n\nCurrent Wallet Balance: {wallet_amount}\n")
                        end_game_decision = input('Continue playing? y/n\n(y:Yes | n:No)')
                if end_game_decision.upper() == 'N':
                     run_game = False
                        
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(SLOTS())