from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='308710e5-f132-5a35-9a3a-710c9042521a',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name',
    display_name='Pidgeotto',
    searchable_by=['Pidgeotto', 'Stage 1', 'Pidgeotto'],
    subtypes=['Stage 1'],
    collector_number=163,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name',
    family_id=16,
    abilities=[
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
