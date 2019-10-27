class Tank:
    def __init__(self, model, health, armor, damage):
        self.model =  model
        self.health = health
        self.armor = armor 
        self.damage = damage
        self.alive = True

    def print_info(self):
        print("модель: " + self.model)
        print("Здоровье: " + str(self.health))
        print("Броня: " + str(self.armor))
        print("Урон: " + str(self.damage))
        
        if self.alive == True:
            print("Танк Жив")
        else:
            print("Танк мёртв")

    def shoot(self, enemy):
        enemy.health = enemy.health - self.damage
        if enemy.health <= 0:
            enemy.health = 0
            enemy.alive = False









tank_1= Tank('T-34', 1000, 100,160 )
tank_2= Tank('FluffyAttak-28', 150, 10, 1000)
#tank_1.print_info()
#tank_1.shoot(tank_2)
#tank_2.print_info()

class STank(Tank):
    def __init__(self, model, health, armor, damage, dop_health):
        super().__init__(health, armor, damage)
        self.dop_health = dop_health
    
    def rapair(self):
        print("чиню...")
        print("починился")



SupTank = STank('AtomCat-220', 1000, 100, 300, True)
#комментарий
