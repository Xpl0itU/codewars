def solution(args):
    ranges = []
    range_start = None
    range_end = None

    for num in args:
        if range_start is None:
            range_start = num

        if range_end == None or num == range_end + 1:
            range_end = num
        else:
            if range_start == range_end - 1:
                ranges.append((range_start, range_start))
                ranges.append((range_end, range_end))
            else:
                ranges.append((range_start, range_end))
            range_start = num
            range_end = num

    if range_start != None:
        if range_start == range_end - 1:
            ranges.append((range_start, range_start))
            ranges.append((range_end, range_end))
        else:
            ranges.append((range_start, range_end))

    final_string = ""
    for start, end in ranges:
        if start == end:
            final_string += str(start)
        else:
            final_string += f"{start}-{end}"
        final_string += ","
    return final_string[:-1]