from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e25e3160-d54c-561d-821b-2878dd3b15e9',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HeracrossEX.Name',
    display_name='Heracross-EX',
    searchable_by=['Heracross-EX', 'Basic', 'EX', 'HeracrossEX'],
    subtypes=['Basic', 'EX'],
    collector_number=4,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=214,
    abilities=[
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Giga Power',
            game_text='You may do 40 more damage. If you do, this Pokémon does 20 damage to itself. | When a Pokémon-EX has been Knocked Out, your opponent takes 2 Prize cards.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
