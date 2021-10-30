from tkinter import *
class inventory:
    user = {
        "HP": 90,
        "EXP": 0,
        "Keys": 0,
        "Gold": 0,
        "Silver": 0,
        "Dollars": 0,
        "Deer": 0,
        "Meat": 0
    }
    store_items = {
        "Knife": 10,
        "Pistol": 2,
        "Riffle": 3
    }
    Store = True
    def stats():
        root = Tk()
        root.title('Stats')
        HP = Text(root, height=2, width=20, bg='greenyellow', fg='darkgoldenrod')
        EXP = Text(root, height=2, width=20, bg='greenyellow', fg='darkgoldenrod')
        Keys = Text(root, height=2, width=20, bg='lightblue', fg='darkgoldenrod')
        Gold = Text(root, height=2, width=20, bg='lightblue', fg='darkgoldenrod')
        Silver = Text(root, height=2, width=20, bg='lightblue', fg='darkgoldenrod')
        Dollars = Text(root, height=2, width=20, bg='lightblue', fg='darkgoldenrod')
        Deer = Text(root, height=2, width=20, bg='gray', fg='gold')
        Meat = Text(root, height=2, width=20, bg='gray', fg='gold')
        HP.pack()
        EXP.pack()
        Keys.pack()
        Gold.pack()
        Silver.pack()
        Dollars.pack()
        Deer.pack()
        Meat.pack()
        Players_HP = "HP:" + str(inventory.user.get("HP"))
        Players_EXP = "EXP:" + str(inventory.user.get("EXP"))
        Players_Keys = "Keys:" + str(inventory.user.get("Keys"))
        Players_Gold = "Gold:" + str(inventory.user.get("Gold"))
        Players_Silver = "Silver:" + str(inventory.user.get("Silver"))
        Players_Dollars = "$" + str(inventory.user.get("Dollars"))
        Players_Deer = "Deer:" + str(inventory.user.get("Deer"))
        Players_Meat = "Meat:" + str(inventory.user.get("Meat"))
        HP.insert(END, Players_HP)
        EXP.insert(END, Players_EXP)
        Keys.insert(END, Players_Keys)
        Gold.insert(END, Players_Gold)
        Silver.insert(END, Players_Silver)
        Dollars.insert(END, Players_Dollars)
        Deer.insert(END, Players_Deer)
        Meat.insert(END, Players_Meat)
    def add_keys(Keys,Gold):
        inventory.user["Keys"] = Keys + inventory.user.get("Keys")
        inventory.user["Gold"] = Gold + inventory.user.get("Gold")
    def add_gold(Gold,Silver):
        inventory.user["Gold"] = Gold + inventory.user.get("Gold")
        inventory.user["Silver"] = Silver + inventory.user.get("Silver")
    def add_silver(Silver,Dollars):
        inventory.user["Silver"] = Silver + inventory.user.get("Silver")
        inventory.user["Dollars"] = Dollars + inventory.user.get("Dollars")
    def get_stuff_on_load():
        inventory.add_keys(10,10)
        inventory.add_gold(0,10)
        inventory.add_silver(0,10)
    def game_keys_and_gold():
        import random
        keys_amount = [1,2,3,4,5,6,7,8,9,10]
        keys = random.choice(keys_amount)
        gold_amount = [1,2,3,4,5,6,7,8,9,10]
        gold = random.choice(gold_amount)
        inventory.add_keys(keys,gold)
    def game_gold_and_silver():
        import random
        gold_amount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        gold = random.choice(gold_amount)
        silver_amount = [1,2,3,4,5,6,7,8,9,10]
        silver = random.choice(silver_amount)
        inventory.add_gold(gold,silver)
    def game_silver_and_dollar():
        import random
        silver_amount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        silver = random.choice(silver_amount)
        dollars_amount = [100,200,300,400,500]
        dollars = random.choice(dollars_amount)
        inventory.add_silver(silver,dollars)
    def generate_knife_price():
        import random
        import sys
        if inventory.store_items.get("Knife") >= 1:
            generate_dollar_ammount = [5,10,15,20,25,30]
            generate_ammount = random.choice(generate_dollar_ammount)
            if inventory.user.get("Dollars") >= generate_ammount:
                print("You Have Bought A Hunting Knife")
                inventory.user["Knife"] = 0
                inventory.user["Knife"] = 1 + inventory.user.get("Knife")
                inventory.user["Dollars"] = inventory.user.get("Dollars") - generate_ammount
            elif inventory.user.get("Dollars") <= generate_ammount:
                print("You Do Not Have Enough Money To Buy This")
                inventory.store()
        if inventory.store_items.get("Knife") <= 0:
           sys.exit()
    def generate_Pistol_price():
        import random
        import sys
        if inventory.store_items.get("Pistol") >= 1:
            generate_silver_ammount = [5,10,15,20,25,30]
            generate_ammount = random.choice(generate_silver_ammount)
            if inventory.user.get("Silver") >= generate_ammount:
                print("You Have Bought A Hunting Pistol")
                inventory.user["Pistol"] = 0
                inventory.user["Pistol"] = 1 + inventory.user.get("Pistol")
                inventory.user["Silver"] = inventory.user.get("Silver") - generate_ammount
            elif inventory.user.get("Silver") <= generate_ammount:
                print("You Do Not Have Enough Money To Buy This")
                inventory.store()
        if inventory.store_items.get("Pistol") <= 0:
           sys.exit()
    def generate_Riffle_price():
        import random
        import sys
        if inventory.store_items.get("Riffle") >= 1:
            generate_gold_ammount = [5,10,15,20,25,30]
            generate_ammount = random.choice(generate_gold_ammount)
            if inventory.user.get("Gold") >= generate_ammount:
                print("You Have Bought A Hunting Riffle")
                inventory.user["Riffle"] = 0
                inventory.user["Riflle"] = 1 + inventory.user.get("Riffle")
                inventory.user["Gold"] = inventory.user.get("Gold") - generate_ammount
            elif inventory.user.get("Gold") <= generate_ammount:
                print("You Do Not Have Enough Money To Buy This")
                inventory.store()
        if inventory.store_items.get("Pistol") <= 0:
           sys.exit()
    def store():
        print("You Are At The Hunting Store And You Must Buy An Item")
        pick_item = input("Knife,Pistol,Riffle\n")
        if pick_item == "Knife":
            inventory.generate_knife_price()
            inventory.Store = False
        if pick_item == "Pistol":
            inventory.generate_Pistol_price()
            inventory.Store = False
        if pick_item == "Riffle":
            inventory.generate_Riffle_price()
            inventory.Store = False
    def hunting():
        import random
        if "Knife" in inventory.user:
            deer_attack_chance = ["Success","Fail","Fail"]
            deer_attack = random.choice(deer_attack_chance)
            if deer_attack == "Success":
                print("You Have Killed A Deer")
                inventory.user["Deer"] = 1 + inventory.user["Deer"]
            if deer_attack == "Fail":
                print("You Didn't Kill The Deer")
                inventory.user["Deer"] = 0 + inventory.user["Deer"]
        if "Pistol" in inventory.user:
            deer_attack_chance = ["Success","Success","Fail"]
            deer_attack = random.choice(deer_attack_chance)
            if deer_attack == "Success":
                print("You Have Killed A Deer")
                inventory.user["Deer"] = 1 + inventory.user["Deer"]
            if deer_attack == "Fail":
                print("You Didn't Kill The Deer")
                inventory.user["Deer"] = 0 + inventory.user["Deer"]
        if "Riffle" in inventory.user:
            deer_attack_chance = ["Success","Success","Success","Fail"]
            deer_attack = random.choice(deer_attack_chance)
            if deer_attack == "Success":
                print("You Have Killed A Deer")
                inventory.user["Deer"] = 1 + inventory.user["Deer"]
            if deer_attack == "Fail":
                print("You Didn't Kill The Deer")
                inventory.user["Deer"] = 0 + inventory.user["Deer"]
    def cooking(deer,serving,HP,EXP):
        print("This Is How Much Cooked Deer Meat You Have:")
        print (deer/serving)
        inventory.user["HP"] = deer/serving + HP
        inventory.user["EXP"] = deer/serving + EXP
        inventory.user["Deer"] = inventory.user.get("Deer") - deer
        inventory.user["Meat"] = inventory.user.get("Meat") + deer/serving
    def sell_meat(meat,price):
        inventory.user["Dollars"] = meat * price + inventory.user.get("Dollars")
        inventory.user["Meat"] = inventory.user.get("Meat") - meat
        print(inventory.user)
    def file_exsist():
        f = open("data.txt", "w")
        f.writelines(str(inventory.user.get("HP")))
        f.writelines("\n")
        f.writelines(str(inventory.user.get("EXP")))
        f.writelines("\n")
        f.writelines(str(inventory.user.get("Keys")))
        f.writelines("\n")
        f.writelines(str(inventory.user.get("Gold")))
        f.writelines("\n")
        f.writelines(str(inventory.user.get("Silver")))
        f.writelines("\n")
        f.writelines(str(inventory.user.get("Dollars")))
        f.writelines("\n")
        f.writelines(str(inventory.user.get("Deer")))
        f.writelines("\n")
        f.writelines(str(inventory.user.get("Meat")))
        f.close()
        inventory.stats()
    def start():
        import sys
        inventory.get_stuff_on_load()
        print("You Are Going To Pick Up Keys And Gold")
        ready = True
        while ready == True:
            inventory.game_keys_and_gold()
            print(inventory.user)
            ready = False
            if ready == False:
                print("You Are Going To Pick Up Gold And Silver")
                ready = True
                while ready == True:
                    inventory.game_gold_and_silver()
                    print(inventory.user)
                    ready = False
                    if ready == False:
                        print("You Are Going To Pick Up Silver And Dollars")
                        ready = True
                        while ready == True:
                            inventory.game_silver_and_dollar()
                            print(inventory.user)
                            ready = False
                            if ready == False:
                                while inventory.Store == True:
                                    inventory.store()
                                    if inventory.Store == False:
                                        hunt = input("Do You Want To Hunt?\n")
                                        while hunt == "Yes":
                                            inventory.hunting()
                                            hunt = input("Do You Want To Hunt?\n")
                                            inventory.stats()
                                            if hunt == "No":
                                                inventory.cooking(inventory.user.get("Deer"),2,inventory.user.get("HP"),inventory.user.get("EXP"))
                                                print(inventory.user)
                                                inventory.sell_meat(inventory.user.get("Meat"),12.5)
                                                print("TIP: If You Want To Keep Stats Put The Information Into A Spreadsheet")
                                                inventory.file_exsist()
inventory.start()
