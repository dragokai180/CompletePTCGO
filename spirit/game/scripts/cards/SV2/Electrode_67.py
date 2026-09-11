from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad865914-e32c-5cc1-856b-9a9597377c0d',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name',
    display_name='Electrode',
    searchable_by=['Electrode', 'Stage 1', 'Electrode'],
    subtypes=['Stage 1'],
    collector_number=67,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    family_id=100,
    abilities=[
        Attack(
            title='Lightning Ball',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
