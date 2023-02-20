is_num = lambda x: x.replace(".", "", 1).isdigit() or (x[0] == "-" and x[1:].replace(".", "", 1).isdigit())
