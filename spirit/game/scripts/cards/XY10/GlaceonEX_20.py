from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1de258b-0622-53e4-9137-d5cda537ba31',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonEX.Name',
    display_name='Glaceon-EX',
    searchable_by=['Glaceon-EX', 'Basic', 'EX', 'GlaceonEX'],
    subtypes=['Basic', 'EX'],
    collector_number=20,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=471,
    abilities=[
        Attack(
            title='Second Bite',
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Crystal Ray',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Evolution Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
