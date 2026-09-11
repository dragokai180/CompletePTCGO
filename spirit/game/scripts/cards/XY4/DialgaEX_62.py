from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d195b85f-e153-5a4b-ac46-2d8b408096c0',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DialgaEX.Name',
    display_name='Dialga-EX',
    searchable_by=['Dialga-EX', 'Basic', 'EX', 'DialgaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=62,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title='Chrono Wind',
            game_text="If the Defending Pokémon is a Pokémon-EX, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Full Metal Impact',
            game_text='Discard 2 Metal Energy attached to this Pokémon.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
