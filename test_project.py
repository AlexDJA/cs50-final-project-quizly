from project import generate_numbers, check_answer, feedback

def test_generate_numbers():
    f1, s1 = generate_numbers(1)
    f2, s2 = generate_numbers(2)
    f3, s3 = generate_numbers(3)

    assert 0 <= f1 <= 100
    assert 0 <= s1 <= 100
    assert -100 <= f2 <= 100
    assert -100 <= s2 <= 100
    assert -50 <= f3 <= 50
    assert -11 <= s3 <= 11

def test_check_answer():
    assert check_answer("8", 8) == True
    assert check_answer("034", 34) == True
    assert check_answer("41", 14) == False

def test_feedback():
    assert feedback(5, 5) == "Outstanding! 💯"
    assert feedback(17, 20) == "Amazing! So close to perfection! 🤩"
    assert feedback(3, 10) == "Don't give up! Try practicing more quizzes and you will see better results! 💪"
