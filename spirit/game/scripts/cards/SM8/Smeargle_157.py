from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='62f853c5-d6d1-550d-b02c-155346035ddc',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name',
    display_name='Smeargle',
    searchable_by=['Smeargle', 'Basic', 'Smeargle'],
    subtypes=['Basic'],
    collector_number=157,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=235,
    abilities=[
        Attack(
            title='Stunning Likeness',
            game_text='Your opponent reveals their hand. You may use the effect of a Supporter card you find there as the effect of this attack.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tail Smash',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
