from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='44151fcc-9b75-5983-8f87-ce13631b5570',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name',
    display_name='Lechonk',
    searchable_by=['Lechonk', 'Basic', 'Lechonk'],
    subtypes=['Basic'],
    collector_number=156,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=915,
    abilities=[
        Attack(
            title='Whimsy Tackle',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
