from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be88144c-032c-548e-b92f-d8ae90964d2d',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name',
    display_name='Beldum',
    searchable_by=['Beldum', 'Basic', 'Beldum'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=374,
    abilities=[
        Attack(
            title='Lunge Out',
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title='Single Smash',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
