param([string]$OriginalDll, [string]$PatchedDll, [string]$CecilDll)
$ErrorActionPreference = 'Stop'
Add-Type -Path (Resolve-Path -LiteralPath $CecilDll).Path
$original = [Mono.Cecil.AssemblyDefinition]::ReadAssembly((Resolve-Path -LiteralPath $OriginalDll).Path)
$patched = [Mono.Cecil.AssemblyDefinition]::ReadAssembly((Resolve-Path -LiteralPath $PatchedDll).Path)
function FilterMethod($assembly) {
    ($assembly.MainModule.Types | Where-Object {$_.FullName -ceq 'I.W'}).Methods |
        Where-Object {$_.Name -ceq 'Filter'}
}
function EvaluateFoilCase($instruction, [bool]$hasFacet, [bool]$foil, [bool]$parallel) {
    $stack = [Collections.Generic.Stack[object]]::new()
    for ($step = 0; $step -lt 30; $step++) {
        $next = $instruction.Next
        switch ($instruction.OpCode.Code.ToString()) {
            'Ldarg_1' { $stack.Push('archetype') }
            'Ldloca' { $stack.Push('facet-address') }
            'Ldloc' { $stack.Push('facet') }
            'Callvirt' {
                $null = $stack.Pop()
                switch ($instruction.Operand.Name) {
                    'TryGetOne' { $null = $stack.Pop(); $stack.Push($hasFacet) }
                    'get_IsFoil' { $stack.Push($foil) }
                    'get_IsParallelFoil' { $stack.Push($parallel) }
                    default { throw 'Unexpected call in patched filter' }
                }
            }
            'Brfalse' { if (!$stack.Pop()) { $next = $instruction.Operand } }
            'Ldc_I4_0' { $stack.Push($false) }
            'Ceq' { $right = $stack.Pop(); $left = $stack.Pop(); $stack.Push($left -eq $right) }
            'Ret' { return [bool]$stack.Pop() }
            default { throw ('Unexpected instruction: ' + $instruction) }
        }
        $instruction = $next
    }
    throw 'Filter did not return'
}
try {
    $before = FilterMethod $original
    $after = FilterMethod $patched
    $oldSwitch = $before.Body.Instructions | Where-Object {$_.OpCode.Code -eq 'Switch'}
    $newSwitch = $after.Body.Instructions | Where-Object {$_.OpCode.Code -eq 'Switch'}
    for ($i = 0; $i -lt $before.Body.Instructions.Count; $i++) {
        $a = $before.Body.Instructions[$i]; $b = $after.Body.Instructions[$i]
        if ($a.OpCode.Code -eq 'Switch') { continue }
        if ($a.ToString() -cne $b.ToString()) { throw "Original instruction changed: $i" }
    }
    for ($i = 0; $i -lt 32; $i++) {
        if ($i -notin @(9,10) -and $oldSwitch.Operand[$i].Offset -ne $newSwitch.Operand[$i].Offset) {
            throw "Unrelated filter changed: $i"
        }
    }
    foreach ($hasFacet in @($false,$true)) {
        foreach ($foil in @($false,$true)) {
            foreach ($parallel in @($false,$true)) {
                $reverse = EvaluateFoilCase $newSwitch.Operand[9] $hasFacet $foil $parallel
                $regular = EvaluateFoilCase $newSwitch.Operand[10] $hasFacet $foil $parallel
                if ($reverse -ne ($hasFacet -and $parallel)) { throw 'Reverse-holo predicate failed' }
                if ($regular -ne ($hasFacet -and $foil -and !$parallel)) { throw 'Regular-holo predicate failed' }
            }
        }
    }
    Write-Output 'PASS: 16 foil truth cases; original instructions and other 30 filters preserved.'
} finally { $original.Dispose(); $patched.Dispose() }
