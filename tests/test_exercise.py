import pytest
import src.exercise

def test_exercise():
    input_values = ["data.csv","FURIA","data.csv","ENCE"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["File:","Team:","Games: 2","Wins: 1","Losses: 1",\
                      "File:","Team:","Games: 6","Wins: 3","Losses: 3"]
