class Util:
    ######################################################
    # Helper functions

    def isValidRow(self, row):
        # If not 4 columns, reject
        if len(row) != 4:
            return False

        # If id or login is not alphanumeric, reject
        if not row[0].isalnum() or not row[1].isalnum():
            return False

        # If salary is not decimal or below 0, reject
        try:
            sal = float(row[3])
            if sal < 0:
                return False
        except ValueError:
            return False

        return True

    def isDuplicated(self, column):
        # Check if column contains any duplicates
        if len(column) == len(set(column)):
            return False
        return True

    def isNone(self, val):
        if val == None:
            return True
        return False

    def isValidParams(self, minSal, maxSal, offset, limit, sort):
        # If param empty, reject
        if self.isNone(minSal) or self.isNone(maxSal) or self.isNone(offset) or self.isNone(limit) or self.isNone(sort) or sort == '':
            return False

        # If salary params invalid, reject
        if minSal < 0 or maxSal < 0 or maxSal < minSal:
            return False

        # If limit or offset params invalid, reject
        if offset < 0 or limit < 0 or limit > 30:
            return False

        # If sort sign not valid, reject
        if sort[0] != '-' and sort[0] != ' ' and sort[0] != '+' and sort[:3] != '%2B':
            return False

        # if sort key not valid, reject
        keys = ['id', 'name', 'login', 'salary']
        if sort[:3] == '%2B':
            if sort[3:] not in keys:
                return False
        else:
            if sort[1:] not in keys:
                return False

        return True

    def prepareParams(self, minSal, maxSal, offset, limit, sort):
        params = None
        sorting = ''
        # If sort sign is URI encoded +
        if sort[:3] == '%2B':
            params = (minSal, maxSal, limit, offset)
            sorting = sort[3:] + ' ASC'
        else:
            # If sort sign is -
            if sort[0] == '-':
                params = (minSal, maxSal, limit, offset)
                sorting = sort[1:] + ' DESC'
            # If sort sign is + or replaced with space
            else:
                params = (minSal, maxSal, limit, offset)
                sorting = sort[1:] + ' ASC'
        return params, sorting
