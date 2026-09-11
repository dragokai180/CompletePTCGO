from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1f9285e6-e026-5bfb-9b2b-80edc21e16be',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name',
    display_name='Mr. Mime',
    searchable_by=['Mr. Mime', 'Basic', 'MrMime'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Attack(
            title='Happy Mime',
            game_text='Each player draws a card.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Double Slap',
            game_text='Flip 2 coins. This attack does 40 damage for each heads.',
            cost={PokemonTypes.FAIRY: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
