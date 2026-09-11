from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='063970cc-790d-5c0f-b736-7851b303d92e',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name',
    display_name='Mr. Mime',
    searchable_by=['Mr. Mime', 'Basic', 'MrMime'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=122,
    abilities=[
        Ability(
            title='Trick Reveal',
            game_text="Once during your turn (before your attack), you may have both you and your opponent reveal your hands. This power can't be used if Mr. Mime is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Juggling',
            game_text='Flip 4 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
