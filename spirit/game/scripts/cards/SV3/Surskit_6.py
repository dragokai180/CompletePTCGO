from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d32bead-bc98-5711-b531-935febd287e3',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name',
    display_name='Surskit',
    searchable_by=['Surskit', 'Basic', 'Surskit'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=283,
    abilities=[
        Attack(
            title='Lunge',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
