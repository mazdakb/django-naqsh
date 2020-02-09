NON_FIELD_ERRORS = "__generic__"


class MarketplaceError(Exception):
    """Base Marketplace Error

    An base error class to be used throughout the marketplace.

    Notes:
        - inspired by `django.core.exceptions.ValidationError`
    """

    def __init__(self, message, code=None, params=None):
        """
        The `message` argument can be a single error, a list of errors, or a
        dictionary that maps field names to lists of errors. What we define as
        an "error" can be either a simple string or an instance of
        MarketplaceError with its message attribute set, and what we define as
        list or dictionary can be an actual `list` or `dict` or an instance
        of MarketplaceError with its `error_list` or `error_dict` attribute set.
        """
        super().__init__(message, code, params)

        if isinstance(message, MarketplaceError):
            if hasattr(message, "error_dict"):
                message = message.error_dict
            elif not hasattr(message, "message"):
                message = message.error_list
            else:
                message, code, params = message.message, message.code, message.params

        if isinstance(message, dict):
            self.error_dict = {}
            for field, messages in message.items():
                if not isinstance(messages, MarketplaceError):
                    messages = MarketplaceError(messages)
                self.error_dict[field] = messages.error_list

        elif isinstance(message, list):
            self.error_list = []
            for msg in message:
                # Normalize plain strings to instances of MarketplaceError.
                if not isinstance(msg, MarketplaceError):
                    msg = MarketplaceError(msg)
                if hasattr(msg, "error_dict"):
                    self.error_list.extend(sum(msg.error_dict.values(), []))
                else:
                    self.error_list.extend(msg.error_list)

        else:
            self.message = message
            self.code = code
            self.params = params
            self.error_list = [self]

    @property
    def message_dict(self):
        # Trigger an AttributeError if this MarketplaceError
        # doesn't have an error_dict.
        getattr(self, "error_dict")

        return dict(self)

    @property
    def messages(self):
        if hasattr(self, "error_dict"):
            return sum(dict(self).values(), [])
        return list(self)

    def update_error_dict(self, error_dict):
        if hasattr(self, "error_dict"):
            for field, error_list in self.error_dict.items():
                error_dict.setdefault(field, []).extend(error_list)
        else:
            error_dict.setdefault(NON_FIELD_ERRORS, []).extend(self.error_list)
        return error_dict

    def __iter__(self):
        if hasattr(self, "error_dict"):
            for field, errors in self.error_dict.items():
                yield field, list(MarketplaceError(errors))
        else:
            for error in self.error_list:
                message = error.message
                if error.params:
                    message %= error.params
                yield str(message)

    def __str__(self):
        if hasattr(self, "error_dict"):
            return repr(dict(self))
        return repr(list(self))

    def __repr__(self):
        return "MarketplaceError(%s)" % self
