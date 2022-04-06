#!/usr/bin/env bash

# LHS rather than just `mullvad account get | ...` b/c doing that led to some weird
# rust panic error about a broken stdout pipe. This change makes LHS output all be on
# one line though.
echo `mullvad account get` | cut -d " " -f 3 > account
