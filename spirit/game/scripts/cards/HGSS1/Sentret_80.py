from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e97d3aea-bc3e-5704-b300-0776bb8671b1',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name',
    display_name='Sentret',
    searchable_by=['Sentret', 'Basic', 'Sentret'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=161,
    abilities=[
        Attack(
            title='Scout',
            game_text="Look at your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
