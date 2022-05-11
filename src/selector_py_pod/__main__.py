
from selector_py_pod.adapters.cli_arguments import args
from selector_py_pod.config import build_config
from selector_py_pod.domain.config import build_adapters, build_outputs
from selector_py_pod.domain.selector import build_selection
from selector_py_pod.domain.utils import parse_show_id


def main(args):
    config = build_config(args.env)
    adapters = build_adapters(config)
    outputs = build_outputs(config)

    show_id = args.show_id
    name = args.name
    description = args.description
    k = args.episodes_amount

    adapter_name, channel_id = parse_show_id(show_id)
    adapter = adapters.get(adapter_name)
    selection = build_selection(name, description, channel_id, adapter, k=k)
    for o in args.outputs:
        outputs.get(o, outputs.get('serial')).post(selection)


main(args)
