from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import gust_attack


def _is_metal_energy(card):
    return energy_provides_type(card, PokemonTypes.METAL.value)


async def metallic_hammer(ctx):
    """150, +150 more if you discard 3 Metal Energy from this Pokemon."""
    bonus = 0
    metal = [e for e in ctx.attached_energies(ctx.attacker) if _is_metal_energy(e)]
    if len(metal) >= 3 and await ctx.ask_yes_no(
        "Discard 3 Metal Energy from this Pokémon and have this attack do 150 more damage?"
    ):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 3, predicate=_is_metal_energy,
            prompt="Choose 3 Metal Energy to discard from this Pokémon",
        )
        if len(discarded) >= 3:
            bonus = 150
    await ctx.deal_damage(150 + bonus)


card = PokemonCardDef(
    guid="62696373-03a8-5971-a5c0-3200a5b9a750",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross","Stage 2","Metagross"],
    subtypes=["Stage 2"],
    collector_number=61,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Bounce Back",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.METAL: 1},
            damage=60,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Metallic Hammer",
            game_text="You may discard 3 Metal Energy from this Pokémon and have this attack do 150 more damage.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            damage_operator="+",
            effect=metallic_hammer,
        ),
    ],
)
