#!/usr/bin/env python3

from argpi import Arguments, ArgumentDescription, FetchType

args = Arguments().__capture__()

args.__add__("add", ArgumentDescription().name("add argument").shorthand("-a"))
args.__add__("remove", ArgumentDescription().name("remove argument").shorthand("-r"))

args.__analyse__()

if args.__there__("add"):
    print("add is present")
    if args.__argument_has_value__("add"):
        print("add has a value")
        print(f"Arguments: {args.__fetch__('add', FetchType.TILL_LAST)}")
        print(f"Arguments: {args.__fetch__('add', FetchType.SINGULAR)}")
    else:
        print("add has no value")
else:
    print("add is not present")


if args.__there__("remove"):
    print("remove is present")
    if args.__argument_has_value__("remove"):
        print("remove has a value")
        print(f"Arguments: {args.__fetch__('remove', FetchType.TILL_NEXT)}")
    else:
        print("remove has no value")
else:
    print("remove is not present")
