# PS4 SSPI Static Catalog Builder

This repository builds SSPI embedded-catalog-v1 package sources from catalog JSON.

## Build and install from a phone

1. Edit catalog/example.json with PS4 homebrew, public-domain packages, or packages you own and are authorized to distribute.
2. Open Actions → Build SSPI source → Run workflow, or push a catalog change.
3. The workflow builds the .gssource and publishes it as a GitHub Release asset.
4. Copy this direct asset URL:
   https://github.com/yessir5678xz-lang/Create-PS4-Static-Catalog-on-GitHub/releases/download/sspi-source-latest/personal-library.gssource
5. On the PS4, open SSPI → OPTIONS → Settings → Connections → Connect your phone. Scan the QR code with your Android phone.
6. Keep SSPI open. On the phone page, open Sources, paste the direct asset URL and tap Install source on PS4.
7. On the PS4, open Manage sources and confirm the source is enabled.

The phone and PS4 must be on the same reachable network. Do not use a GitHub HTML page URL; the phone page needs the direct .gssource asset URL. Keep the pairing QR code and URL private.

## Download optimization reality

SSPI already starts a download with six connections and increases them only while total throughput improves, up to 25. It remembers server resets and respects lower per-provider limits. A .gssource is data-only: SSPI does not execute code from a source, so a source cannot install a downloader extension, override connection policy, or create bandwidth beyond the PS4/ISP/host/storage limits.

See docs/download-performance.md for practical tuning.

## Catalog data

Each title needs a supported PS4 title ID, name, and package records. Package kinds are base, update, dlc, or unknown; access types are Direct and HosterLanding.

Only add homebrew, public-domain files, your own dumps, or files you are otherwise authorized to distribute. This repository does not scrape or mirror copyrighted game libraries.

## Local archive-password lookup

The helper in tools/password_lookup.py merges passwords you already know into a local catalog. Copy passwords.local.example.json to passwords.local.json, replace the example values, then run:

    python tools/password_lookup.py catalog/example.json catalog/with-local-passwords.json

Then build the output:

    python SSPI-Static-Catalog/ tools/build_source.py catalog/with-local-passwords.json dist/private-source.gssource

The helper performs local lookup only. It does not retrieve, guess, scrape, or bypass passwords. Never commit passwords.local.json or publish a generated source containing private passwords. The local password file is ignored by Git.

## References

- SSPI guide: https://xyhlo.github.io/SSPI/
- SSPI source: https://github.com/Xyhlo/SSPI
