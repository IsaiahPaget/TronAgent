from game_object.ObjectManager import InstantiateObject, ObjectManager
from position import Position
from lightcycle.LightCycleHead import LightCycleHead
from Wall import Wall
from settings import PLAYER_HEAD_COLOR, PLAYER_TAIL_COLOR, PLAYER_TWO_HEAD_COLOR, PLAYER_TWO_TAIL_COLOR, WALL_COLOR_LEFT, WALL_COLOR_RIGHT, WALL_COLOR_BOTTOM, WALL_COLOR_TOP, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE


class ObjectLoader:

    def __init__(self) -> None:
        self._object_manager = ObjectManager()

    def load_objects(self) -> None:
        self._load_players()
        self._load_walls()

    def _load_players(self) -> None:
        InstantiateObject(
            LightCycleHead(
                Position(300, 450), 
                "player_one", 
                PLAYER_HEAD_COLOR,
                PLAYER_TAIL_COLOR
            )
        )
        # InstantiateObject(
        #     LightCycleHead(
        #         Position(150, 450), 
        #         "player_two", 
        #         PLAYER_TWO_HEAD_COLOR,
        #         PLAYER_TWO_TAIL_COLOR
        #     )
        # )

    def _load_walls(self) -> None:
        x_len = int(SCREEN_WIDTH / BLOCK_SIZE) - 1
        y_len = int(SCREEN_HEIGHT / BLOCK_SIZE) - 1

        # TOP
        for x_top in range(x_len):
            self._object_manager.attach(
                Wall(
                    Position(x_top * BLOCK_SIZE, 0),
                    f"wall_top_{x_top}",
                    WALL_COLOR_TOP
                )
            )
        
        # BOTTOM
        for x_bottom in range(x_len):
            self._object_manager.attach(
                Wall(
                    Position(x_bottom * BLOCK_SIZE + BLOCK_SIZE, y_len * BLOCK_SIZE),
                    f"wall_bottom_{x_bottom}",
                    WALL_COLOR_BOTTOM
                )
            )

        # RIGHT
        for y_right in range(y_len):
            self._object_manager.attach(
                Wall(
                    Position(x_len * BLOCK_SIZE, y_right * BLOCK_SIZE),
                    f"wall_right_{y_right}",
                    WALL_COLOR_RIGHT
                )
            )

        # LEFT
        for y_left in range(y_len):
            self._object_manager.attach(
                Wall(
                    Position(0, y_left * BLOCK_SIZE + BLOCK_SIZE),
                    f"wall_left_{y_left}",
                    WALL_COLOR_LEFT
                )
            )
        
