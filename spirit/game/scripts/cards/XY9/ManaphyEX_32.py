from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='376194e2-8ffa-59aa-97c9-cf87d13861ce',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ManaphyEX.Name',
    display_name='Manaphy-EX',
    searchable_by=['Manaphy-EX', 'Basic', 'EX', 'ManaphyEX'],
    subtypes=['Basic', 'EX'],
    collector_number=32,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=490,
    abilities=[
        Ability(
            title='Aqua Tube',
            game_text='Each of your Pokémon that has any Water Energy attached to it has no Retreat Cost.',
            passive=standard_passive('Each of your Pokémon that has any Water Energy attached to it has no Retreat Cost.'),
        ),
        Attack(
            title='Mineral Pump',
            game_text='Heal 30 damage from each of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
