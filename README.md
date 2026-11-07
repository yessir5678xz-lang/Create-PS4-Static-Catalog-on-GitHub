# PS4 SSPI Static Catalog Builder

This repository contains a builder for SSPI's `embedded-catalog-v1` static source format.

## Quick start

1. Edit `catalog/example.json` and add titles plus package links you own or are authorized to distribute.
2. Open **Actions → Build SSPI source → Run workflow**.
3. Keep the default catalog path or enter your own JSON path, then run it.
4. Open the completed workflow run and download the **sspi-gssource** artifact.
5. Add the downloaded `.gssource` in SSPI under **Settings → Connections → Manage sources → Add a source link**. Host the file at a direct HTTPS download URL if SSPI requires a URL.

The builder project is included in `SSPI-Static-Catalog-Builder.zip`; the workflow extracts it and runs its Python builder. No third-party Python packages are required.

## Catalog entries

- Use PS4 title IDs such as `CUSA12345`; PS5 PPSA IDs are not supported by this engine.
- Package kinds: `base`, `update`, `dlc`, or `unknown`.
- `accessType`: `Direct` for a direct file URL, or `HosterLanding` for a host page.
- Use only HTTP(S) package URLs you control or are authorized to share.
- Never include Real-Debrid, TorBox, AllDebrid, Premiumize API keys, cookies, session tokens, or personal credentials in catalog files.

The included example uses `.invalid`, a reserved non-working domain. Replace it before expecting a download to work.

## Important

A successful build checks the source archive's structure and metadata. It does not prove every download URL works or guarantee compatibility with every SSPI release. Test with a permitted homebrew/test package first.

## References

- SSPI guide: https://xyhlo.github.io/SSPI/
- SSPI source: https://github.com/Xyhlo/SSPI
