import ldclient

class LDdanotestproject(LDClient):
    
    def ld_test_bool(self, user: dict, details: bool=False):
        """Woohoo flagging

        :param dict user: a dictionary containing parameters for the end user requesting the flag
        :param boolean details: call variation with details

        :return: one of the flag's variation values, or the default value.
        :rtype: bool
        """
        if details:
            return self.variation("test-bool", user, False)
        else:
            return self.variation_detail("test-bool", user, False)
    
    def ld_test_flag(self, user: dict, details: bool=False):
        """

        :param dict user: a dictionary containing parameters for the end user requesting the flag
        :param boolean details: call variation with details

        :return: one of the flag's variation values, or the default value.
        :rtype: bool
        """
        if details:
            return self.variation("test-flag", user, False)
        else:
            return self.variation_detail("test-flag", user, False)
    
    def ld_test_rule_swap(self, user: dict, details: bool=False):
        """

        :param dict user: a dictionary containing parameters for the end user requesting the flag
        :param boolean details: call variation with details

        :return: one of the flag's variation values, or the default value.
        :rtype: 
        """
        if details:
            return self.variation("test-rule-swap", user, string2)
        else:
            return self.variation_detail("test-rule-swap", user, string2)
    
    def ld_example_test_flag_3(self, user: dict, details: bool=False):
        """This is an awesome feature that will be implemented.

        :param dict user: a dictionary containing parameters for the end user requesting the flag
        :param boolean details: call variation with details

        :return: one of the flag's variation values, or the default value.
        :rtype: bool
        """
        if details:
            return self.variation("ansible-random-new-name", user, False)
        else:
            return self.variation_detail("ansible-random-new-name", user, False)
    
    def ld_test_json(self, user: dict, details: bool=False):
        """

        :param dict user: a dictionary containing parameters for the end user requesting the flag
        :param boolean details: call variation with details

        :return: one of the flag's variation values, or the default value.
        :rtype: dict
        """
        if details:
            return self.variation("test-json", user, {'test2': 'value2'})
        else:
            return self.variation_detail("test-json", user, {'test2': 'value2'})
    
    def ld_test_number(self, user: dict, details: bool=False):
        """

        :param dict user: a dictionary containing parameters for the end user requesting the flag
        :param boolean details: call variation with details

        :return: one of the flag's variation values, or the default value.
        :rtype: int
        """
        if details:
            return self.variation("test-number", user, 24)
        else:
            return self.variation_detail("test-number", user, 24)
    