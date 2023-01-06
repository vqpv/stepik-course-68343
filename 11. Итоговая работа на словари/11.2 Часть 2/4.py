def build_query_string(params):
    return "&".join(sorted([k + "=" + str(v) for k, v in params.items()]))
