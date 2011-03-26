# coding: utf-8

import optparse

def main():
    parser = optparse.OptionParser()
    parser.add_option(
        "--config",
        default = "server.conf",
        dest = "conf",
        help = "config file path"
    )
    parser.add_option(
        "--command",
        dest = "command",
        help = "Command name"
    )
    parser.add_option(
        "--convert",
        action="store_true",
        dest = "convert",
        help = "Auto convert database"
    )

    options, args = parser.parse_args()
    print options.conf, options.command, options.convert

if __name__ == "__main__":
    main()
