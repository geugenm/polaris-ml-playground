class CleanerParameters():
    def __init__(self):
        self._row_max_na_percentage = None
        self._col_max_na_percentage = None

    @property
    def col_max_na_percentage(self):
        """
        Return the col_max_na_percentage value as Integer.

        """

        return self._col_max_na_percentage

    @col_max_na_percentage.setter
    def col_max_na_percentage(self, col_max_na_percentage):
        self._col_max_na_percentage = col_max_na_percentage

    @property
    def row_max_na_percentage(self):
        """
        Return the row_max_na_percentage value as Integer.

        """

        return self._row_max_na_percentage

    @row_max_na_percentage.setter
    def row_max_na_percentage(self, row_max_na_percentage):
        self._row_max_na_percentage = row_max_na_percentage
