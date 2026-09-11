from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0cd6a391-3dec-5fa7-b860-db146ab05157',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    display_name='Salandit',
    searchable_by=['Salandit', 'Basic', 'Salandit'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=757,
    abilities=[
        Attack(
            title='Grass Fire',
            game_text="Discard a Grass Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
