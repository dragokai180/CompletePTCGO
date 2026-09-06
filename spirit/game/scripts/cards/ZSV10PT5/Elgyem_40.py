from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per

async def energy_warp(ctx):
    """Move an Energy from 1 of your opponent's Benched Pokémon to their Active Pokémon."""
    opp_active = ctx.opponent_active()
    candidates = [p for p in ctx.opponent_bench() if ctx.attached_energies(p)]
    if opp_active is None or not candidates:
        return
    source = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Benched Pokémon"
    )
    if source is None or ctx.effects_blocked(source):
        return
    energies = ctx.attached_energies(source)
    energy = energies[0]
    if len(energies) > 1:
        picked = await ctx.choose_cards(
            energies, 1, prompt="Choose an Energy to move to the Active Pokémon"
        )
        if not picked:
            return
        energy = picked[0]
    await ctx.move_energy(energy, opp_active)

card = PokemonCardDef(
    guid="e4d0ced3-688f-5d0a-88d3-3e14cd150e1a",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem","Basic","Elgyem"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=605,
    abilities=[
        Attack(
            title="Slight Shift",
            game_text="Move an Energy from 1 of your opponent's Pokémon to another of their Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_warp,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
