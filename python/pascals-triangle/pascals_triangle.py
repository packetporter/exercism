def rows(row_count):
    """
    The function calculates the pascal triangle values upto the given row count

    :param row_count: int - number of rows in the pascal triangle
    :return preceding_rows: list of tuples  
    """
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    if row_count == 2:
        return [[1], [1, 1]]
    # Initialise a new row with 1's as first and last digits
    new_row = [1, 1]
    # Get a variable to rescursively calculate the rows
    preceding_rows = rows(row_count-1)
    # Get the last row form the preceding rows list
    previous_row = preceding_rows[-1]
    # The length of the previous rows gives index ranges that can be used to calculate the succeding rows using formula
    # C(n,k) = C(n-1,k-1) + C(n-1,k) where C is the value of the digit in row n and index k
    for ind in range(1, len(previous_row)):
        new_row.insert(-1, (previous_row[ind-1] + previous_row[ind]))
    preceding_rows.append(new_row)

    return preceding_rows


