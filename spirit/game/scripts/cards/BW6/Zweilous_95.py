from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import destructive_beam

card = PokemonCardDef(
    guid="a949ed4f-75ea-5534-a7b4-81eaecfdfdfe",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous","Stage 1","Zweilous"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=destructive_beam,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 2},
            damage=80,
        ),
    ],
)
