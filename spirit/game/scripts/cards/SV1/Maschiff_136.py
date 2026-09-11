from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0bb9f98-a3f1-541f-a355-351576f8f94f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name',
    display_name='Maschiff',
    searchable_by=['Maschiff', 'Basic', 'Maschiff'],
    subtypes=['Basic'],
    collector_number=136,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=942,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
