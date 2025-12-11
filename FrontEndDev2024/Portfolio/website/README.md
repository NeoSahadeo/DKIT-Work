# Oto

The sound platform.

## What is Oto

Oto is the Japanese word for 'sound'. It's a Spotify 'clone'
that allows free music streaming; assuming the music exists on
my Gitlab repo.

There is technically no managed backend for the site. It uses
the Gitlab v4 api to make queries and download raw data.
All other processing happens client-side.

## Stack

Svelte/Svelekit 5 is used to framework the site.

I utilise [Music Metadata](https://github.com/borewit/music-metadata) to
parse music data embedded in the .mp3 files as writing my own
parser is a little time consuming.

Everything else is either built from scratch or donated by [Helios3](https://github.com/NeoSahadeo/Helios3Demo)
I made a few weeks back.

## Contributing

Not accepting any. The code is horrendous. If I ever plan to continue this project
I will re-write the entire system from scratch, hopefully with the
idea of adding in a database and scalability.

# LICENSE

Copyright (C) Neo Sahadeo - All Rights Reserved

This source code is protected under international copyright law. All rights
reserved and protected by the copyright holders.
This file is confidential and only available to authorized individuals with the
permission of the copyright holders.  If you encounter this file and do not have
permission, please contact the copyright holders and delete this file.
