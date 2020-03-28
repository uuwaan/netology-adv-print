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
    yield start
    for index, item in enumerate(items):
        yield str(item) + (sep if index < sep_index else "")
    yield end


def _sep_specials(item, specs="\r\n"):
    if len(specs) == 0:
        yield item
    else:
        sep_items = item.split(specs[0])
        sep_index = len(sep_items) - 1
        for sub_index, sub_item in enumerate(sep_items):
            yield from _sep_specials(sub_item, specs[1:])
            if sub_index < sep_index:
                yield specs[0]


def _mfwrite(files, flush, s):
    for f in files:
        if not f:
            continue
        f.write(s)
        if flush:
            f.flush()
