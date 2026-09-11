# Local card artwork

Card and product images are intentionally excluded from the CompletePTCGO
source repository. They are copyrighted assets and add several gigabytes of
generated binary data to Git history.

Supply the local asset archive referred to by this project as the **cbrew
bundles**, then import the artwork before starting the server:

```powershell
$env:PTCGO_ART_SOURCE_DIR = "C:\path\to\cbrew bundles"
python -m spirit.tools.ptcgo_local_assets --source $env:PTCGO_ART_SOURCE_DIR
```

The importer writes card textures below this directory and the server compiles
the required AssetBundles into `spirit/assets/bundleCache/`. Both outputs stay
local and must not be committed.
