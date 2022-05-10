
from selector_py_pod.adapters.cli_arguments import args
from selector_py_pod.domain.selector import build_selection
from selector_py_pod.domain.config import outputs
from json import dumps as json_dumps


def main(args):
    # spotify:6IAVb4s0xkX9l9Ym9hZjM5
    # youtube:UCFZ_ShKPRL2YEhoRZ1UmiyQ
    show_id = args.show_id
    name = args.name
    description = args.description
    selection = build_selection(
        name, description, show_id, k=args.episodes_amount)
    for o in args.outputs:
        outputs.get(o, outputs.get('serial')).post(selection)


main(args)
