from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2f8bbe9c-724b-5db6-a06a-458b5fed21ed',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name',
    display_name='Toxel',
    searchable_by=['Toxel', 'Basic', 'Toxel'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=848,
    abilities=[
        Attack(
            title='Whimsy Tackle',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
