from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='713a2b9c-e416-51e1-b7cd-394f21bcc65e',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name',
    display_name='Camerupt',
    searchable_by=['Camerupt', 'Stage 1', 'Camerupt'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name',
    family_id=322,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Eruption',
            game_text='Each player discards the top card of his or her deck. This attack does 60 more damage for each Energy card discarded in this way.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
