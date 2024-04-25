import click
from .utils import get_mat, get_summary
from mp_api.client import MPRester


@click.command(
    help="Material search with API key, property, range, and number of elements"
)
@click.argument("api_key", type=str)
@click.argument("property", type=str)
@click.argument("min", type=float)
@click.argument("max", type=float)
@click.argument("num", type=int)
def main(api_key, property, min, max, num):
    print("\n".join(get_mat(api_key, property, float(min), float(max), int(num))))
    # mat = get_mat(api_key, property, min, max, num)
    # print("Materials:", mat)
