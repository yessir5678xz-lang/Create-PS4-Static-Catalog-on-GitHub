# PS4 download performance notes

A package source supplies searchable metadata and download/hoster URLs. It does not control the PS4 network stack, SSPI's connection count, router QoS, or a hoster's rate limits.

## Practical improvements

1. Prefer Ethernet from the PS4 to the router. If using Wi-Fi, use 5 GHz and keep the console close to the access point.
2. Avoid VPNs and proxy hops unless they solve a specific routing or ISP problem.
3. Use a supported debrid/service account with sufficient plan quota and choose a reliable hoster/link.
4. Keep the staging drive healthy and fast, with ample free space. Extraction and verification can become the bottleneck.
5. Avoid other large downloads or streaming traffic on the same connection.
6. Test a small authorized package from two hosts at different times; host performance varies.

## SSPI connection handling

SSPI release notes describe adaptive connections: downloads begin with multiple connections and add more only while throughput improves. A source file cannot force a higher connection count or bypass host limits. Leave adaptive behavior enabled.

## What this project can optimize

- Include accurate direct URLs where distribution is authorized.
- Prefer reliable mirrors and remove stale links.
- Include file size and SHA-256 when known.
- Keep base, update, DLC and multipart metadata accurate.

There is no source-side setting that guarantees maximum speed. Throughput is limited by the slowest part of the path: PS4 network, ISP route, debrid provider, hoster, storage write speed, or extraction.
