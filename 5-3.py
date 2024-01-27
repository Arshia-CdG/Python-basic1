class Soldier:
    def __init__(self, id, health, x, y):
        self.id = id
        self.health = health
        self.x = x
        self.y = y

class Melee(Soldier):
    def __init__(self, id, x, y):
        super().__init__(id, 100, x, y)

class Archer(Soldier):
    def __init__(self, id, x, y):
        super().__init__(id, 100, x, y)

class Game:
    def __init__(self, n):
        self.board = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]
        self.player1_turn = True
        self.player1_soldiers = {}
        self.player2_soldiers = {}

    def new_soldier(self, soldier_type, id, x, y):
        if self.player1_turn:
            if id in self.player1_soldiers:
                print("duplicate tag")
                return
            else:
                if soldier_type == "melee":
                    soldier = Melee(id, x, y)
                    self.player1_soldiers[id] = soldier
                else:
                    soldier = Archer(id, x, y)
                    self.player1_soldiers[id] = soldier
            self.player1_turn = False
        else:
            if id in self.player2_soldiers:
                print("duplicate tag")
                return
            else:
                if soldier_type == "melee":
                    soldier = Melee(id, x, y)
                    self.player2_soldiers[id] = soldier
                else:
                    soldier = Archer(id, x, y)
                    self.player2_soldiers[id] = soldier
            self.player1_turn = True
        self.board[x][y].append(soldier)
        
    def move(self, id, direction):
        dx = 0
        dy = 0
        if direction == "up":
            dy = -1
        elif direction == "down":
            dy = 1
        elif direction == "left":
            dx = -1
        elif direction == "right":
            dx = 1

        if self.player1_turn:
            soldiers = self.player1_soldiers
            self.player1_turn = False
        else:
            soldiers = self.player2_soldiers
            self.player1_turn = True

        if id in soldiers:
            soldier = soldiers[id]
            new_x = soldier.x + dx
            new_y = soldier.y + dy
            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]):
                self.board[soldier.x][soldier.y].remove(soldier)
                self.board[new_x][new_y].append(soldier)
                soldier.x = new_x
                soldier.y = new_y
            else:
                print("out of bounds")
        else:
            print("soldier does not exist")

    def attack(self, attacker_id, target_id):
        if attacker_id in self.player1_soldiers and target_id in self.player2_soldiers and self.player1_turn:
            attacker = self.player1_soldiers[attacker_id]
            target = self.player2_soldiers[target_id]
            self.player1_turn = False
        elif attacker_id in self.player2_soldiers and target_id in self.player1_soldiers and self.player1_turn == False:
            attacker = self.player2_soldiers[attacker_id]
            target = self.player1_soldiers[target_id]
            self.player1_turn = True
        else:
            print("soldier does not exist")
            return

        distance = abs(attacker.x - target.x) + abs(attacker.y - target.y)
        if isinstance(attacker, Archer) and distance > 2:
            print("the target is too far")
            return
        elif isinstance(attacker, Melee) and distance > 1:
            print("the target is too far")
            return

        target.health -= 20 if isinstance(attacker, Melee) else 10
        if target.health <= 0:
            del self.board[target.x][target.y]
            if target in self.player1_soldiers.values():
                del self.player1_soldiers[target.id]
            else:
                del self.player2_soldiers[target.id]
            print("target eliminated")

    def info(self, id):
        if id in self.player1_soldiers and self.player1_turn:
            soldier = self.player1_soldiers[id]
            self.player1_turn = False
        elif id in self.player2_soldiers and self.player1_turn == False:
            soldier = self.player2_soldiers[id]
            self.player1_turn = True
        else:
            print("soldier does not exist")
            return
        print(f"health: {soldier.health}")
        print(f"location: {soldier.x} {soldier.y}")

    def who_is_in_the_lead(self):
        player1_health = sum(s.health for s in self.player1_soldiers.values())
        player2_health = sum(s.health for s in self.player2_soldiers.values())
        
        if player1_health > player2_health:
            print("Player 1 is in the lead")
        elif player2_health > player1_health:
            print("Player 2 is in the lead")
        else:
            print("draw")


def main():            
    n = int(input())
    game = Game(n)

    while True:
        command = input().split()
        if command[0] == "new":
            game.new_soldier(command[1], int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "move":
            game.move(int(command[1]), command[2])
        elif command[0] == "attack":
            game.attack(int(command[1]), int(command[2]))
        elif command[0] == "info":
            game.info(int(command[1]))
        elif command[0] == "who":
            game.who_is_in_the_lead()
        elif command[0] == "end":
            break
    
if __name__ == "__main__":
    main()
