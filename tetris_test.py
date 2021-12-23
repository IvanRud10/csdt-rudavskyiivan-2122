import unittest
from tetris_game import Board
from tetris_model import BoardData, Shape

# unittests
class GameSettingsTest(unittest.TestCase):
    def setUp(self):
        self.boardspeed = Board.speed
        self.width = BoardData.width
        self.height = BoardData.height

    def test_of_speed(self):
        self.assertEqual(self.boardspeed, 10, "Wrong speed")

    def test_size_of_width(self):
        self.assertEqual(self.width, 10, "Wrong width")

    def test_size_of_height(self):
        self.assertEqual(self.height, 20, "Wrong height")


# integration tests
class CoordinatesTest(unittest.TestCase):
    def setUp(self):
        self.Shape = Shape()
        self.coords1 = self.Shape.getCoords(0, 1, 0)
        self.coords2 = self.Shape.getCoords(2, -1, 1)
        self.coords3 = self.Shape.getCoords(3, -1, 0)
        self.getBoundingOffsets = self.Shape.getBoundingOffsets(2)

    def test_coords1(self):
        self.assertEqual(next(self.coords1), (1, 0), "Wrong coordinates")

    def test_coords2(self):
        self.assertEqual(next(self.coords2), (-1, 1), "Wrong coordinates")

    def test_coords3(self):
        self.assertEqual(next(self.coords3), (-1, 0), "Wrong coordinates")

    def test_offsets(self):
        self.assertEqual(
            self.getBoundingOffsets, (0, 0, 0, 0), "Wrong bounding offsets"
        )


class MoveDownTest(unittest.TestCase):
    def setUp(self):
        self.BoardData = BoardData()
        self.movelines = self.BoardData.moveDown()
        self.droplines = self.BoardData.dropDown()

    def test_move_down(self):
        self.assertFalse(self.movelines > 0, "Lines value does not match ")

    def test_drop_down(self):
        self.assertEqual(self.droplines, 0, "Wrong lines")


if __name__ == "__main__":
    unittest.main()
