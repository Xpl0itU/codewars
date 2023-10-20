def make_readable(seconds):
    hours = seconds // 3600
    remaining = seconds - hours * 3600
    minutes = remaining // 60
    remaining = remaining - minutes * 60
    return f"{hours:02}:{minutes:02}:{remaining:02}"