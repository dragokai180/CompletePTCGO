from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import retribution, signal_beam

card = PokemonCardDef(
    guid="e4cd5d55-d252-53c6-b4d8-95e4086561af",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=["Palpitoad","Stage 1","Palpitoad"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    abilities=[
        Attack(
            title="Supersonic",
            game_text="The Defending Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=signal_beam,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
