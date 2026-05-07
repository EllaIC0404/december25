from src.helpers.file_helpers import read_csv


def test_read_csv():
    # Arrange
    filename = "data/stock_data.csv"
    # Act
    data = read_csv(filename)
    # Assert
    assert len(data) > 0

