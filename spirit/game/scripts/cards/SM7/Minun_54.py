from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c3095ba-b2e3-55b0-baae-b7c7a0f48888',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name',
    display_name='Minun',
    searchable_by=['Minun', 'Basic', 'Minun'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=312,
    abilities=[
        Attack(
            title='Ditch and Draw',
            game_text='You may discard any number of cards from your hand. Then, draw cards until you have 5 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electro Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
