#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2022 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
from argparse import ArgumentParser
from ._help import print_help_msg
from .fosslight_scanner import run_main, PKG_NAME
from fosslight_util.help import print_package_version


def main():
    parser = ArgumentParser(description='FOSSLight Scanner', prog='fosslight_scanner', add_help=False)
    parser.add_argument('mode', nargs='?', help='source| dependency| binary| reuse| all| compare', default="all")
    parser.add_argument('--path', '-p', help='Path to analyze', type=str, dest='path', default="")
    parser.add_argument('--wget', '-w', help='Link to be analyzed', type=str, dest='link', default="")
    parser.add_argument('--file', '-f', help='Scanner output file format (excel,yaml), Compare mode (excel,html,yaml,json)',
                        type=str, dest='file', default="")
    parser.add_argument('--output', '-o', help='Output directory or file', type=str, dest='output', default="")
    parser.add_argument('--dependency', '-d', help='Dependency arguments', type=str, dest='dep_argument', default="")
    parser.add_argument('--url', '-u', help="DB Url", type=str, dest='db_url', default="")
    parser.add_argument('--core', '-c', help='Number of processes to analyze source', type=int, dest='core', default=-1)
    parser.add_argument('--raw', '-r', help='Keep raw data',  action='store_true', dest='raw', default=False)
    parser.add_argument('--timer', '-t', help='Hide the progress bar',  action='store_true', dest='timer', default=False)
    parser.add_argument('--version', '-v', help='Print version',  action='store_true', dest='version', default=False)
    parser.add_argument('--help', '-h', help='Print help message', action='store_true', dest='help')
    parser.add_argument('--yaml', '-y', help='Two FOSSLight reports in yaml format', nargs=2, default="")
    try:
        args = parser.parse_args()
    except SystemExit:
        print_help_msg()

    if args.help:
        print_help_msg()
    elif args.version:
        print_package_version(PKG_NAME, "FOSSLight Scanner Version:")
    else:
        if args.yaml:
            before_yaml = args.yaml[0]
            after_yaml = args.yaml[1]
        else:
            before_yaml = ''
            after_yaml = ''

        run_main(args.mode, args.path, args.dep_argument, args.output, args.file,
                 args.link, args.db_url, args.timer, args.raw, args.core, before_yaml, after_yaml)


if __name__ == "__main__":
    main()
