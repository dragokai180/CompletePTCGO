from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe656356-d2ee-5ca0-9016-16230b203fc5',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name',
    display_name='Quaxly',
    searchable_by=['Quaxly', 'Basic', 'Quaxly'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=912,
    abilities=[
        Attack(
            title='Water Splash',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
