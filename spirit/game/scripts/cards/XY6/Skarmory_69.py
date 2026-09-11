from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3546018f-7b61-5476-a328-38152124f94f',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name',
    display_name='Skarmory',
    searchable_by=['Skarmory', 'Basic', 'Skarmory'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=227,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Blow Through',
            game_text='If there is any Stadium card in play, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
