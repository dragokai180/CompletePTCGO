from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df86243f-c4c7-56ac-9060-18fbee4e8066',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name',
    display_name='Toxtricity',
    searchable_by=['Toxtricity', 'Stage 1', 'Toxtricity'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name',
    family_id=848,
    abilities=[
        Attack(
            title='Mach Bolt',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
