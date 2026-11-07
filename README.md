# PS4 SSPI Static Catalog Builder

This repository builds SSPI embedded-catalog-v1 package sources from catalog JSON.

## Build

1. Edit catalog/example.json with PS4 homebrew, public-domain packages, or packages you own and are authorized to distribute.
2. Open Actions → Build SSPI source → Run workflow.
3. Download the sspi-gssource artifact from the completed run.
4. Add the generated source to SSPI.

The builder is included in SSPI-Static-Catalog-Builder.zip. The workflow extracts it and builds the .gssource archive.

## Catalog data

Each title needs a supported PS4 title ID, name, and one or more package records. Package kinds are base, update, dlc, or unknown; access types are Direct and HosterLanding.

Only add homebrew, public-domain files, your own dumps, or files you are otherwise authorized to distribute. This repository does not scrape or mirror copyrighted game libraries.

## Local archive-password lookup

The helper in tools/password_lookup.py merges passwords you already know into a local catalog. Copy passwords.local.example.json to passwords.local.json, replace the example values, then run:

    python tools/password_lookup.py catalog/example.json catalog/with-local-passwords.json

Then build the output:

    python SSPI-Static-Catalog/tools/build_source.py catalog/with-local-passwords.json dist/private-source.gssource

The helper performs local lookup only. It does not retrieve, guess, scrape, or bypass passwords. Never commit passwords.local.json or publish a generated source containing private passwords. The local password file is ignored by Git.

## Download speed

A source file cannot change PS4 network settings or override SSPI's downloader. See docs/download-performance.md for practical tuning. SSPI already uses adaptive download connections; a fake speed-booster field would do nothing.

## References

- SSPI guide: https://xyhlo.github.io/SSPI/
- SSPI source: https://github.com/Xyhlo/SSPI
