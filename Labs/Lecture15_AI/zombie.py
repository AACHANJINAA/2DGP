import random
import math
import game_framework
import game_world
import winsound

from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf
from pico2d import *
import game_world

import server
from ball import Ball



class TargetMarker:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.image = load_image('hand_arrow.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)














# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10













animation_names = ['Attack', 'Dead', 'Idle', 'Walk']






class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]


<<<<<<< HEAD
    def prepare_patrol_points(self):
        positions = [(43, 750), (1118, 750), (1050, 530), (575, 220), (235, 33), (575, 220), (1050, 530), (1118, 750)]
        # 좌표 획득 시 기준 위치가 왼쪽 위
        self.patrol_positions = []
        for p in positions:
            self.patrol_positions.append((p[0], 1024 - p[1]))  # pico2d 상의 좌표계를 이용하도록 변경

    def __init__(self):
        self.prepare_patrol_points()
        self.ptrol_order = 1
        self.x, self.y = self.patrol_positions[0]
=======

    def __init__(self):
        #self.x, self.y = 1280 / 4 * 3, 1024 / 4 * 3
        self.x, self.y = random.randint(100, 1180), random.randint(100, 924)
        self.tx, self.ty = random.randint(100, 1180), random.randint(100, 924)
>>>>>>> c0296a243c1f50f168834b49f662a7f8cb8c036f
        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.frame = 0.0
        self.build_behavior_tree()

        self.target_ball = None
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 0

        self.target_marker = TargetMarker(self.tx, self.ty)
        game_world.add_object(self.target_marker, 1)


<<<<<<< HEAD

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 1.03
            self.dir = random.random() * 2 * math.pi # 방향을 라디안 값으로 설정
            print('Wander Success')
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def wait(self):
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <= 0:
            self.wait_timer = 2.0
            return BehaviorTree.SUCCESS

        return BehaviorTree.RUNNING

    def find_player(self):
        distance = (server.boy.x - self.x) ** 2 + (server.boy.y - self.y) ** 2

        if distance < (PIXEL_PER_METER * 10) ** 2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
        return BehaviorTree.FAIL

    def move_to_player(self):
        def move_to_player(self):
            self.speed = RUN_SPEED_PPS

        self.dir = math.atan2(server.boy.y - self.y, server.boy.x - self.x)
        return BehaviorTree.SUCCESS

    def get_next_position(self):
        self.target_x, self.target_y = self.patrol_points[self.patrol_order % len(self.patrol_positions)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        self.speed = RUN_SPEED_PPS

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2
        if distance < PIXEL_PER_METER ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING



    def build_behavior_tree(self):
        wander_node = LeafNode('Wander', self.wander)
        wait_node = LeafNode('Wait', self.wait)

        wander_wait_node = SequenceNode('WanderWait')
        wander_wait_node.add_children(wander_node, wait_node)

        get_next_position_node = LeafNode("Get Next Position", self.get_next_position)
        move_to_target_node = LeafNode("Move to Target", self.move_to_target)
        patrol_node = SequenceNode("Patrol")
        patrol_node.add_children(get_next_position_node, move_to_target_node)
        self.bt = BehaviorTree(patrol_node)

        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)

        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)

        self.bt = BehaviorTree(wander_chase_node)


    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.bt.run()

=======
    def calculate_current_position(self):
>>>>>>> c0296a243c1f50f168834b49f662a7f8cb8c036f
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)


    def find_random_location(self):
        # fill here
        pass

    def move_to(self, radius = 0.5):
        # fill here
        pass

    def play_beep(self):
        winsound.Beep(440, 100)
        return BehaviorTree.SUCCESS

    def find_ball_location(self):
        # fill here
        pass

    def calculate_squared_distance(self, a, b):
        return (a.x-b.x)**2 + (a.y-b.y)**2

    def move_to_boy(self):
        # fill here
        pass

    def flee_from_boy(self):
        # fill here
        pass

    def build_behavior_tree(self):
        # fill here
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        # fill here
        self.calculate_current_position()

    def draw(self):
        self.font.draw(self.x - 60, self.y + 50, '%7d' % self.hp, (0, 0, 255))
        #fill here
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        if 'zombie:ball' == group:
            self.hp += 100
