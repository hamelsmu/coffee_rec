from __future__ import print_function
import argparse

COUNTRIES = {
    "Balinese": "Bali",
    "Bolivian": "Bolivia",
    "Brazilian": "Brazil",
    "Costa Rican": "Costa Rican",
    "Dominican": "Dominican Republic",
    "Salvadorean": "El Salvador",
    "Ethiopian": "Ethiopia",
    "Guatemalan": "Guatemala",
    "Indian": "India",
    "Kenyan": "Kenya",
    "Malian": "Mali",
    "Mexican": "Mexico",
    "Panamanian": "Panama",
    "Peruvian": "Peru",
    "Sumatran": "Sumatra",
}


class Coffee(object):
    @classmethod
    def fromname(cls, name):
        # to be implemented
        raise NotImplementedError


def parse(name):
    # to be implemented
    pass


def summarize(file):
    # to be implemented
    pass


def recommend(file):
    # to be implemented
    pass


def main():
    parser = argparse.ArgumentParser(description='TextNow Coffee Tasting')
    subparsers = parser.add_subparsers(dest='command', help='command')

    commands = ['parse', 'summarize', 'recommend']
    parsers = {
        c: subparsers.add_parser(c) for c in commands
    }

    parsers['parse'].add_argument('arg', help='coffee descriptive name')
    parsers['summarize'].add_argument('arg', help='input csv file',
                                      type=argparse.FileType('r'))
    parsers['recommend'].add_argument('arg', help='input csv file',
                                      type=argparse.FileType('r'))
    args = parser.parse_args()
    globals()[args.command](args.arg)


if __name__ == '__main__':
    main()
