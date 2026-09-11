from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='724a17a3-cc91-56ea-9887-e40b728edac6',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kartana.Name',
    display_name='Kartana',
    searchable_by=['Kartana', 'Basic', 'Ultra Beast', 'Kartana'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=101,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=798,
    abilities=[
        Attack(
            title='Divine Paper',
            game_text='If your opponent has exactly 6 Prize cards remaining, this attack does 90 more damage.',
            cost={PokemonTypes.METAL: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
