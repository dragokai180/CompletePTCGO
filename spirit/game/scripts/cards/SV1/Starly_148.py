from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b8f5ffe-61b5-5f12-8c9a-4332107cab6b',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name',
    display_name='Starly',
    searchable_by=['Starly', 'Basic', 'Starly'],
    subtypes=['Basic'],
    collector_number=148,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=396,
    abilities=[
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
