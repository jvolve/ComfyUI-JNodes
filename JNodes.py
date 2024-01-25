import re

class J_StringContains:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
                "substring": ("STRING", { "multiline": False, "default": "" }),
                "success_result": ("STRING", { "multiline": False, "default": "" }),
                "default_result": ("STRING", { "multiline": False, "default": "" }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)

    FUNCTION = "string_contains"

    OUTPUT_NODE = True

    CATEGORY = "JNodes"

    def string_contains(self, input_str, substring, success_result, default_result):
        if substring.lower() in input_str.lower():
            return (success_result,)
        
        return (default_result,)

class J_StringAppend:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
                "append": ("STRING", { "multiline": False, "default": "" }),
                "separator": ("STRING", { "multiline": False, "default": "" }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)

    FUNCTION = "string_append"

    OUTPUT_NODE = True

    CATEGORY = "JNodes"

    def string_append(self, input_str, append_str, separator):
        result = input_str + separator + append_str
        
        return (result,)

class J_StringSplit:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
                "split_chars": ("STRING", { "multiline": False, "default": "," }),
                "trim_whitespace": ("BOOLEAN", { "default": True }),
                "other_trim_chars": ("STRING", { "multiline": False, "default": "" }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string_list",)

    FUNCTION = "string_split"

    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "JNodes"

    def string_split(self, input_str, split_chars, trim_whitespace, other_trim_chars):
        delimiters = list(set(split_chars))
        split_pattern = '|'.join(map(re.escape, delimiters))
        
        result = re.split(split_pattern, input_str)
        
        trim_chars = "" + other_trim_chars
        if trim_whitespace:
            trim_chars += " "
        
        unique_trim_chars = "".join(set(trim_chars))
        
        for i, s in enumerate(result):
            result[i] = s.strip(unique_trim_chars)
        
        return (result,)

class J_StringSelect:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # "input": ("LIST", {"forceInput": True}),
                "input": ("STRING", { "multiline": False, "default": "", "forceInput": True }),
                "select": ("INT", { "default": 0, "min": 0, "step": 1, "display": "number" }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("selected",)

    FUNCTION = "string_select"

    OUTPUT_NODE = True

    CATEGORY = "JNodes"

    def string_select(self, input_list, select_index):
        print(f"input_list: {input_list}", sep="\n")
        result = input_list[select_index]
        return (result,)



NODE_CLASS_MAPPINGS = {
    "J_StringContains": J_StringContains,
    "J_StringAppend": J_StringAppend,
    "J_StringSplit": J_StringSplit,
    "J_StringSelect": J_StringSelect,
}
