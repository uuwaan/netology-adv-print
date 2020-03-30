import sys


def adv_print(*args, **kwargs):
    start = str(kwargs.get("start", ""))
    sep = str(kwargs.get("sep", " "))
    end = str(kwargs.get("end", "\n"))
    max_line = kwargs.get("max_line")
    file = kwargs.get("file", sys.stdout)
    flush = kwargs.get("flush", False)
    in_file = kwargs.get("in_file")
    line_len = 0
    for item in _prn_items(args, start, end, sep):
        for sub_item in _sep_specials(item):
            item_len = len(sub_item)
            if sub_item in ("\n", "\r"):
                line_len = -1
            elif max_line and line_len + item_len > max_line:
                line_len = 0
                _mfwrite((file, in_file), flush, "\n")
            line_len += item_len
            _mfwrite((file, in_file), flush, sub_item)


def _prn_items(items, start, end, sep):
    sep_index = len(items) - 1
    result = [start]
    result.extend(
        str(item) + (sep if index < sep_index else "")
        for index, item in enumerate(items)
    )
    result.append(end)
    return result


def _sep_specials(item, specs="\r\n"):
    sep_items = item.split(specs[0])
    sep_index = len(sep_items) - 1
    result = []
    for sub_index, sub_item in enumerate(sep_items):
        if len(specs) > 1:
            result.extend(_sep_specials(sub_item, specs[1:]))
        else:
            result.append(sub_item)
        if sub_index < sep_index:
            result.append(specs[0])
    return result


def _mfwrite(files, flush, s):
    for f in files:
        if not f:
            continue
        f.write(s)
        if flush:
            f.flush()
