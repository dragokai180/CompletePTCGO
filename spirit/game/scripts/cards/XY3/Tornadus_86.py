from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18073539-656f-5059-aa52-c1fa6384946e',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name',
    display_name='Tornadus',
    searchable_by=['Tornadus', 'Basic', 'Tornadus'],
    subtypes=['Basic'],
    collector_number=86,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=641,
    abilities=[
        Attack(
            title='Push Down',
            game_text='You may have your opponent switch his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Twister Throw',
            game_text='If you have the same number of cards in your hand as your opponent, this attack does 60 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
