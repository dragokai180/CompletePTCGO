from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='93fa23f1-f762-5b26-afcd-80c4662f31e4',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    display_name='Caterpie',
    searchable_by=['Caterpie', 'Basic', 'Caterpie'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=10,
    abilities=[
        Attack(
            title='Leaf Munch',
            game_text="If your opponent's Active Pokémon is a Grass Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
