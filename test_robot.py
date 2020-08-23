import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST

def test_south_turn(robot):
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH

def test_west_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST

def test_north_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.NORTH

def test_illegal_move(robot):
    robot.turn();
    robot.turn();

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1



#move test
def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2

def test_move_north_twice(robot):
    robot.move()
    robot.move()
    state = robot.state()
    assert state['row'] == 8
    assert state['col'] == 1

def test_move_north_triple(robot):
    robot.move()
    robot.move()
    robot.move()
    state = robot.state()
    assert state['row'] == 7
    assert state['col'] == 1


def test_move_west_error(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_move_north_error(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_move_east_error(robot):
    robot.turn()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    with pytest.raises(IllegalMoveException):
        robot.move()
#move test end



def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_with_one_move(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_with_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_with_mult_move(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 6
    assert state['col'] == 1

def test_all_back_track_with_mult_move(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 6
    assert state['col'] == 1
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 7
    assert state['col'] == 1
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 8
    assert state['col'] == 1
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1