from .version_update import HelloWorldNode

NODE_CLASS_MAPPINGS = {
    "HelloWorldNode": HelloWorldNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HelloWorldNode": "Hello World",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']