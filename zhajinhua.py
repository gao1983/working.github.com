#作者A芒果
import random
pai_list = ['2','3','4','5','6','7','8','9','10']
name_list = ['A','J','Q','K']
na_list = ['红桃','黑桃','红方','草花']
all_cards = [na + pai for na in na_list for pai in pai_list + name_list]
random.shuffle(all_cards)
payer = ['大郎','武松','西门庆','王干娘','金莲']
payer_card = [pay for pay in payer]
for i in range(5):  # 循环5次
        card1 = random.choice(all_cards)  # Random 1card
        card2 = random.choice(all_cards)  # Another random 2card
        card3 = random.choice(all_cards)
        cardw =card1 + card2 + card3
        payerwu = random.choice(payer)
        print(f'我{payerwu}的牌:{cardw}')
        #print(f"Iteration {i + 1}: Card 1 = {card1}, Card 2 = {card2},card 3 = {card3}")
        if cardw == card1+card1+card1 or cardw == card2+card2+card2 or cardw == card3+card3+card3:
            print(f'{payerwu} is winner')#炸金花规则if不太熟悉
            break
        elif cardw != card1+card1+card2+card2+card3:
            print(f'{payerwu} is loseter')
        elif cardw == card1+card1+card2+card2+card3:
            print(f'{payerwu} is draw')
        elif cardw != card1 + card1 + card2 + card2 + card3:
            print(f'{payerwu} is loseter')
