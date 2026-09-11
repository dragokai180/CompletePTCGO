from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3e157a1-cb38-5b29-b1d8-13249f9e31c6',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    display_name='Porygon',
    searchable_by=['Porygon', 'Basic', 'Porygon'],
    subtypes=['Basic'],
    collector_number=142,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=137,
    abilities=[
        Attack(
            title='Data Displacement',
            game_text="Flip a coin. If heads, move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
