# Security policy

CompletePTCGO is preservation and interoperability software for a discontinued
game client. It has not been hardened as a public internet service.

## Safe deployment

- Run the server on a trusted private network unless you have independently
  reviewed and secured the deployment.
- Replace Brandon's original default test password before allowing other users
  to connect.
- Never commit `server.key`, account databases, logs, extracted client files,
  or cbrew bundles.
- Keep the supported PTCGO client and the server isolated from sensitive
  systems and credentials.

## Reporting a vulnerability

Open a private GitHub security advisory in the CompletePTCGO repository. Do not
include real credentials, private keys, account databases, or proprietary game
assets in the report.
