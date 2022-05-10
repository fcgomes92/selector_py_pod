def parse_show_id(show_id: str) -> list[str]:
    adapter_name = show_id[0:3]
    channel_id = show_id[4:]
    return adapter_name, channel_id
