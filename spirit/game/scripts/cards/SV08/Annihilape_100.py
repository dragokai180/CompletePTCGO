from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

async def destined_fight(ctx):
    """Both Active Pokémon are Knocked Out."""
    await ctx.knock_out(ctx.defender)
    await ctx.knock_out(ctx.attacker)

card = PokemonCardDef(
    guid="0f51215c-aa14-548a-8826-5eb24f8e9110",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name",
    display_name="Annihilape",
    searchable_by=["Annihilape","Stage 2","Annihilape"],
    subtypes=["Stage 2"],
    collector_number=100,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    family_id=56,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    abilities=[
        Attack(
            title="Tantrum",
            game_text="This Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=130,
            effect=condition_attack(self_conditions=(SpecialConditions.CONFUSED,)),
        ),
        Attack(
            title="Destined Fight",
            game_text="Both Active Pokémon are Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=destined_fight,
        ),
    ],
)
