from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6cfe14a6-522f-55f5-829d-e69de132c9ac',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name',
    display_name='Drampa',
    searchable_by=['Drampa', 'Basic', 'Drampa'],
    subtypes=['Basic'],
    collector_number=159,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=780,
    abilities=[
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Dragon Arcana',
            game_text='If this Pokémon has 2 or more different types of basic Energy attached to it, this attack does 70 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
