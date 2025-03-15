class HelloWorldNode:
    """
    A simple node that displays the text "Hello World".
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Defines the input types for the node. In this case, we have no inputs.
        """
        return {
            "required": {},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_hello_world"
    CATEGORY = "MyCustomNodes"

    def get_hello_world(self):
        """
        Returns the text "Hello World".
        """
        return ("Hello World",)