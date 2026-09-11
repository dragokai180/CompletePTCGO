from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9c3eac51-b720-5fc3-bbc6-e9626c5ae56a',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name',
    display_name='Cacnea',
    searchable_by=['Cacnea', 'Basic', 'Cacnea'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=331,
    abilities=[
        Ability(
            title='Counterattack Quills',
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title='Light Punch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
