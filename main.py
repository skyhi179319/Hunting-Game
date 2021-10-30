class inventory:
    user = {
        "HP": 90,
        "EXP": 0,
        "Keys": 0,
        "Gold": 0,
        "Silver": 0,
        "Dollars": 0,
        "Deer": 0,
        "Meat": 0,
    }
    store_items = {
        "Knife": 10,
        "Pistol": 2,
        "Rifle": 3
    }
    Store = True
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
    def convert_money(price):
        silver_count = 0
        while inventory.user.get("Dollars") - price >= price:
            silver_count = silver_count + 1
        inventory.user["Silver"] = inventory.user.get("Silver") + silver_count
    def generate_knife_price():
        import random
        import sys
        if inventory.store_items.get("Knife") >= 1:
            generate_dollar_ammount = [5,10,15,20,25,30]
            generate_ammount = random.choice(generate_dollar_ammount)
            if inventory.user.get("Dollars") >= generate_ammount:
                print("You Have Bought A Hunting Knife")
                inventory.user["Knife"] = 1
                #inventory.user["Knife"] = 1 + inventory.user.get("Knife")
                inventory.user["Dollars"] = inventory.user.get("Dollars") - generate_ammount
            elif inventory.user.get("Dollars") <= generate_ammount:
                print("You Do Not Have Enough Money To Buy This")
                inventory.store("Start")
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
                inventory.user["Pistol"] = 1
                #inventory.user["Pistol"] = 1 + inventory.user.get("Pistol")
                inventory.user["Silver"] = inventory.user.get("Silver") - generate_ammount
            elif inventory.user.get("Silver") <= generate_ammount:
                print("You Do Not Have Enough Money To Buy This")
                inventory.store("Start")
        if inventory.store_items.get("Pistol") <= 0:
           sys.exit()
    def generate_Rifle_price():
        import random
        import sys
        if inventory.store_items.get("Rifle") >= 1:
            generate_gold_ammount = [5,10,15,20,25,30]
            generate_ammount = random.choice(generate_gold_ammount)
            if inventory.user.get("Gold") >= generate_ammount:
                print("You Have Bought A Hunting Rifrle")
                inventory.user["Rifle"] = 1
                #inventory.user["Rifle"] = 1 + inventory.user.get("Rifle")
                inventory.user["Gold"] = inventory.user.get("Gold") - generate_ammount
            elif inventory.user.get("Gold") <= generate_ammount:
                print("You Do Not Have Enough Money To Buy This")
                inventory.store("Start")
        if inventory.store_items.get("Pistol") <= 0:
           sys.exit()
    def store(gamePos):
        if(gamePos == "Start"):
            print("You Are At The Hunting Store And You Must Buy An Item")
            pick_item = input("Knife,Pistol,Rifle\n")
            if pick_item == "Knife":
                inventory.generate_knife_price()
                inventory.Store = False
            if pick_item == "Pistol":
                inventory.generate_Pistol_price()
                inventory.Store = False
            if pick_item == "Rifle":
                inventory.generate_Rifle_price()
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
        if "Rifle" in inventory.user:
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
    def start():
        import sys
        inventory.get_stuff_on_load()
        print("You Are Going To Pick Up Items")
        ready = True
        if ready == True:
            inventory.game_gold_and_silver()
            inventory.game_silver_and_dollar()
            ready = False
        ready = True
        while ready == True:
            print(inventory.user)
            ready = False
            if ready == False:
                while inventory.Store == True:
                    # starts store
                    inventory.store("Start")
                    if inventory.Store == False:
                        hunt = input("Do You Want To Hunt?\n")
                        while hunt == "Yes":
                            inventory.hunting()
                            hunt = input("Do You Want To Hunt?\n")
                        else:
                            inventory.cooking(inventory.user.get("Deer"),2,inventory.user.get("HP"),inventory.user.get("EXP"))
                            print(inventory.user)
                            inventory.sell_meat(inventory.user.get("Meat"),12.5)
                            print("TIP: If You Want To Keep Stats Put The Information Into A Spreadsheet")
                            inventory.file_exsist()
inventory.start()
