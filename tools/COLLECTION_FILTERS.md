# Collection filter repairs

The server supplies missing labels and native collection facets for card
attributes. Restart the updated server and reconnect the client to refresh
those records. Celebrations Classic Collection is hidden from expansion
filters; the main Celebrations expansion remains available.

Two additional filters, **Reverse Holo** and **Regular Holo**, were empty
branches in the GX-support client's collection filter method. These require
a client-side patch; updating the server alone cannot repair those branches.
The patch is source-only. No client DLL, artwork or foil material is supplied.

## Apply the optional client patch

Close the game. Obtain `Mono.Cecil.dll` from Mono.Cecil or ILSpy, then run
PowerShell from the repository root:

```powershell
./tools/patch_collection_filters.ps1 -ClientDll "C:/path/to/Managed/pie-src.dll" -CecilDll "C:/path/to/Mono.Cecil.dll" -OutputPath "C:/path/to/pie-src.filters.dll"
./tests/test_client_filter_patch.ps1 -OriginalDll "C:/path/to/Managed/pie-src.dll" -PatchedDll "C:/path/to/pie-src.filters.dll" -CecilDll "C:/path/to/Mono.Cecil.dll"
```

Use a new output path. The patcher refuses to overwrite the installed DLL or
an existing output, and rejects an unexpected/already-patched method layout.
The test checks 16 foil truth cases and verifies that the other 30 filter
branches and original instructions are unchanged.

After a successful test, back up the installed `pie-src.dll`, then copy the
generated DLL into the same Managed directory under the name `pie-src.dll`.
Restart the game. Restore your backup to undo the client patch. Never publish
either DLL in this repository.
