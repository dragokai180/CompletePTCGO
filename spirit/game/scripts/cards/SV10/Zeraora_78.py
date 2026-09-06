from spirit.game.data_utils import PokemonCardDef, Attack, is_pokemon_ex
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import is_in_active_spot


async def thunder_raid(ctx):
    """Discard all Energy, then 210 to 1 of the opponent's Benched Pokémon ex."""
    await ctx.discard_energy_from(
        ctx.attacker, 99,
        prompt="Choose Energy to discard from this Pokémon",
    )
    await snipe_attack(
        210,
        pool=lambda p: is_pokemon_ex(p.archetype_id) and not is_in_active_spot(p),
        prompt="Choose 1 of your opponent's Benched Pokémon ex",
    )(ctx)


card = PokemonCardDef(
    guid="8f47379e-062c-5819-bd38-3853619ee5f6",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name",
    display_name="Zeraora",
    searchable_by=["Zeraora","Basic","Zeraora"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    family_id=807,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Thunder Raid",
            game_text="Discard all Energy from this Pokémon, and this attack does 210 damage to 1 of your opponent's Benched Pokémon ex. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            effect=thunder_raid,
        ),
    ],
)
