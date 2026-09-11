from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ea35ae6-c536-5211-9161-81d516477bf1',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name',
    display_name='Spritzee',
    searchable_by=['Spritzee', 'Basic', 'Spritzee'],
    subtypes=['Basic'],
    collector_number=141,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=682,
    abilities=[
        Attack(
            title='Nap',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)
