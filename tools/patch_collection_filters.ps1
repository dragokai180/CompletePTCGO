<#
Repair the two missing foil branches in the GX-support PTCGO client.
Use a Mono.Cecil.dll supplied by ILSpy (or Mono.Cecil), and write to a NEW
output file. Review/test that file and back up the installed client before
replacing it. This does not distribute any client binaries or artwork.
#>
param(
    [Parameter(Mandatory=$true)][string]$ClientDll,
    [Parameter(Mandatory=$true)][string]$CecilDll,
    [Parameter(Mandatory=$true)][string]$OutputPath
)
$ErrorActionPreference = 'Stop'
$sourcePath = (Resolve-Path -LiteralPath $ClientDll).Path
$destinationPath = [IO.Path]::GetFullPath($OutputPath)
if ($sourcePath -eq $destinationPath -or (Test-Path -LiteralPath $destinationPath)) {
    throw 'Choose a new output file; the installed client is never overwritten by this tool.'
}
Add-Type -Path (Resolve-Path -LiteralPath $CecilDll).Path
$assembly = [Mono.Cecil.AssemblyDefinition]::ReadAssembly($sourcePath)
try {
    $filterType = $assembly.MainModule.Types | Where-Object {$_.FullName -ceq 'I.W'}
    $method = $filterType.Methods | Where-Object {
        $_.Name -eq 'Filter' -and $_.Parameters.Count -eq 1 -and
        $_.Parameters[0].ParameterType.FullName -eq 'dwd.core.archetypes.ArchetypeComponent'
    }
    if (@($method).Count -ne 1) { throw 'Expected one typed collection-filter method.' }
    $switch = $method.Body.Instructions | Where-Object {$_.OpCode.Code -eq 'Switch'}
    if (@($switch).Count -ne 1 -or $switch.Operand.Count -ne 32) {
        throw 'Unsupported client filter layout; no output written.'
    }
    $existing = $method.Body.Instructions | Where-Object {
        $_.Operand -is [Mono.Cecil.MethodReference] -and $_.Operand.Name -eq 'get_IsParallelFoil'
    }
    if ($existing) { throw 'Client already handles parallel foil; no output written.' }
    if ($switch.Operand[9] -ne $switch.Operand[10] -or
        $switch.Operand[9].OpCode.Code -ne 'Ldloc_0' -or
        $switch.Operand[9].Next.OpCode.Code -ne 'Ret') {
        throw 'Foil branches are not the expected unimplemented cases; no output written.'
    }
    $foilLocal = $method.Body.Variables | Where-Object {$_.VariableType.FullName -ceq 'w.B'}
    $lookup = ($method.Body.Instructions | Where-Object {
        $_.Operand -is [Mono.Cecil.GenericInstanceMethod] -and
        $_.Operand.Name -eq 'TryGetOne' -and $_.Operand.GenericArguments[0].FullName -ceq 'w.B'
    } | Select-Object -First 1).Operand
    $foilType = $assembly.MainModule.Types | Where-Object {$_.FullName -ceq 'w.B'}
    $isFoil = $foilType.Methods | Where-Object Name -eq 'get_IsFoil'
    $isParallel = $foilType.Methods | Where-Object Name -eq 'get_IsParallelFoil'
    if (!$foilLocal -or !$lookup -or !$isFoil -or !$isParallel) { throw 'Missing native foil contract.' }
    $il = $method.Body.GetILProcessor()
    $op = [Mono.Cecil.Cil.OpCodes]
    foreach ($index in @(9,10)) {
        $entry = $il.Create($op::Ldarg_1)
        $noMatch = $il.Create($op::Ldc_I4_0)
        $switch.Operand[$index] = $entry
        $il.Append($entry)
        $il.Append($il.Create($op::Ldloca, $foilLocal))
        $il.Append($il.Create($op::Callvirt, $lookup))
        $il.Append($il.Create($op::Brfalse, $noMatch))
        if ($index -eq 10) {
            $il.Append($il.Create($op::Ldloc, $foilLocal))
            $il.Append($il.Create($op::Callvirt, $isFoil))
            $il.Append($il.Create($op::Brfalse, $noMatch))
        }
        $il.Append($il.Create($op::Ldloc, $foilLocal))
        $il.Append($il.Create($op::Callvirt, $isParallel))
        if ($index -eq 10) {
            $il.Append($il.Create($op::Ldc_I4_0))
            $il.Append($il.Create($op::Ceq))
        }
        $il.Append($il.Create($op::Ret))
        $il.Append($noMatch)
        $il.Append($il.Create($op::Ret))
    }
    $assembly.Write($destinationPath)
    Write-Output 'Patched Reverse Holo and Regular Holo filters; all other branches preserved.'
} finally { $assembly.Dispose() }
