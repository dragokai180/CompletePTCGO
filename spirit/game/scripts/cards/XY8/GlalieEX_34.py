from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4ec81b5a-a313-56d3-b66a-ab18c0244793',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GlalieEX.Name',
    display_name='Glalie-EX',
    searchable_by=['Glalie-EX', 'Basic', 'EX', 'GlalieEX'],
    subtypes=['Basic', 'EX'],
    collector_number=34,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=362,
    abilities=[
        Attack(
            title='Ice Breath',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Instant Freeze',
            game_text='If you have the same number of cards in your hand as your opponent, this attack does 100 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
