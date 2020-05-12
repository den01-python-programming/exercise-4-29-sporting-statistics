import pytest
import os

def test_exercise():
    os.chdir('src')

    import exercise

    input_values = ["data.csv","FURIA","data.csv","ENCE"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    exercise.input = mock_input
    exercise.print = lambda s : output.append(s)

    exercise.main()

    exercise.input = mock_input
    exercise.print = lambda s : output.append(s)

    exercise.main()

    assert output == ["File:","Team:","Games: 2","Wins: 1","Losses: 1",\
                      "File:","Team:","Games: 6","Wins: 3","Losses: 3"]
