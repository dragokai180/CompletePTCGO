from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='de8e3838-f272-58e9-8176-19dc83476226',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name',
    display_name='Falinks',
    searchable_by=['Falinks', 'Basic', 'Falinks'],
    subtypes=['Basic'],
    collector_number=119,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=870,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Reckless Charge Together',
            game_text='If Falinks is on your Bench, this attack does 90 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
