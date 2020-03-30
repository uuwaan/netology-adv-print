from functools import partial
from itertools import chain


def adv_print(*args, **kwargs):
    start = str(kwargs.pop("start", ""))
    sep = str(kwargs.pop("sep", " "))
    end = str(kwargs.pop("end", "\n"))
    max_line = kwargs.pop("max_line", None)
    in_file = kwargs.pop("in_file", None)
    _print = partial(print, sep="", end="", **kwargs)
    prn_items = chain.from_iterable(map(_sep_specs,
                                        _prn_items(args, start, end, sep)))
    line_len = 0
    out_items = []
    for item in prn_items:
        item_len = len(item)
        if item in ("\n", "\r"):
            line_len = -1
        elif max_line and line_len + item_len > max_line:
            line_len = 0
            out_items.append("\n")
        line_len += item_len
        out_items.append(item)
    _print(*out_items)
    if in_file:
        _print(*out_items, file=in_file)


def _prn_items(items, start, end, sep):
    sep_index = len(items) - 1
    result = [start]
    result.extend(
        str(item) + (sep if index < sep_index else "")
        for index, item in enumerate(items)
    )
    result.append(end)
    return result


def _sep_specs(item, specs="\r\n"):
    sep_items = item.split(specs[0])
    sep_index = len(sep_items) - 1
    result = []
    for sub_index, sub_item in enumerate(sep_items):
        if len(specs) > 1:
            result.extend(_sep_specs(sub_item, specs[1:]))
        else:
            result.append(sub_item)
        if sub_index < sep_index:
            result.append(specs[0])
    return result
