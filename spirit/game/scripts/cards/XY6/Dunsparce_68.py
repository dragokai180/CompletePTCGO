from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad59da46-6a65-5214-a230-35150f962774',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name',
    display_name='Dunsparce',
    searchable_by=['Dunsparce', 'Basic', 'Dunsparce'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=206,
    abilities=[
        Attack(
            title='Burrow',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
