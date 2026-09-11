from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2b0dbfa2-7732-5568-b756-0313cb1b6428',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name',
    display_name='Camerupt',
    searchable_by=['Camerupt', 'Stage 1', 'Camerupt'],
    subtypes=['Stage 1'],
    collector_number=32,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name',
    family_id=322,
    abilities=[
        Attack(
            title='Eruption',
            game_text="Discard the top card of each player's deck. This attack does 100 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Steaming Stomp',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
