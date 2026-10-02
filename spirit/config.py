"""Global server addressing config — the single place to set the host players connect to."""
import os
import json
from pathlib import Path


def _read_local_settings(path):
    """Optional host-only settings; the root JSON file is ignored by Git."""
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict):
        raise ValueError('local_settings.json must contain an object')
    for key in ('coins_per_win', 'coins_per_loss'):
        if key in data and (type(data[key]) is not int or data[key] < 0):
            raise ValueError(f'{key} must be a nonnegative integer')
    if 'grant_all_cards_on_registration' in data and type(data['grant_all_cards_on_registration']) is not bool:
        raise ValueError('grant_all_cards_on_registration must be true or false')
    if 'public_host' in data and (not isinstance(data['public_host'], str) or not data['public_host'].strip()):
        raise ValueError('public_host must be a nonempty string')
    return data


_LOCAL_SETTINGS = _read_local_settings(Path(__file__).resolve().parents[1] / 'local_settings.json')
GRANT_ALL_CARDS_ON_REGISTRATION = _LOCAL_SETTINGS.get('grant_all_cards_on_registration', False)
MATCH_COINS_PER_WIN = _LOCAL_SETTINGS.get('coins_per_win', 1000)
MATCH_COINS_PER_LOSS = _LOCAL_SETTINGS.get('coins_per_loss', 200)

# The address players use to reach this server (IP or domain, no scheme/port).
# For public hosting set this to your public IP/domain, or export SPIRIT_PUBLIC_HOST.
# The client is redirected here mid-login (ConnectionService), so 127.0.0.1 only works
# when the client runs on the same machine as the server.
PUBLIC_HOST = os.environ.get("SPIRIT_PUBLIC_HOST", _LOCAL_SETTINGS.get('public_host', '127.0.0.1'))

HTTP_PORT = int(os.environ.get("SPIRIT_HTTP_PORT", "8000"))
TCP_PORT = int(os.environ.get("SPIRIT_TCP_PORT", "39389"))

HTTP_BASE_URL = f"http://{PUBLIC_HOST}:{HTTP_PORT}"
PLACEHOLDER_IMG = f"{HTTP_BASE_URL}/placeholder.png"

# --- Operational tunables (env-overridable; safe defaults chosen to never affect legit play) ---
LOG_LEVEL = os.environ.get("SPIRIT_LOG_LEVEL", "INFO").upper()

# Outbound send: abort a socket whose write buffer never drains within this many
# seconds (a wedged/zero-window peer). Largest payloads are a few-hundred-KB SGS
# snapshots, so a stalled drain past this is a dead peer, not a slow one.
SEND_TIMEOUT_SECONDS = float(os.environ.get("SPIRIT_SEND_TIMEOUT", "60"))

# Inbound read idle deadlines. The client pings regularly, so a header that never
# arrives for this long is a half-open/dead socket. Pre-auth is tighter to reap
# port-scanners and stalled handshakes before they allocate a router.
IDLE_TIMEOUT_SECONDS = float(os.environ.get("SPIRIT_IDLE_TIMEOUT", "240"))
PREAUTH_TIMEOUT_SECONDS = float(os.environ.get("SPIRIT_PREAUTH_TIMEOUT", "60"))

# Max bytes an inbound zlib body may expand to (decompression-bomb guard). Legit
# client-originated compressed payloads are decks/telemetry, well under 1 MB.
MAX_DECOMPRESSED_BYTES = int(os.environ.get("SPIRIT_MAX_DECOMPRESSED", str(16 * 1024 * 1024)))

# Hard cap on simultaneous TCP connections (0 = unlimited). Excess accepts are
# closed immediately, before a router is built.
MAX_CONNECTIONS = int(os.environ.get("SPIRIT_MAX_CONNECTIONS", "0"))

# Per-connection inbound packet-rate token bucket (abuse guard). Generous enough
# that normal offer/reply cadence and reconnect replay never trip it.
INBOUND_RATE_PER_SEC = float(os.environ.get("SPIRIT_INBOUND_RATE", "80"))
INBOUND_RATE_BURST = float(os.environ.get("SPIRIT_INBOUND_BURST", "240"))

# On login, top every account up to 4 tradable copies of each non-basic card
# (same as admin "grant-all-cards"). Set SPIRIT_GRANT_ALL_CARDS_ON_LOGIN=0 to disable.
GRANT_ALL_CARDS_ON_LOGIN = os.environ.get(
    "SPIRIT_GRANT_ALL_CARDS_ON_LOGIN", "1"
).strip().lower() not in ("0", "false", "no", "off")
