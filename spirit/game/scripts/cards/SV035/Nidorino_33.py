from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d57747ff-0f54-5098-888e-26c33219218d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name',
    display_name='Nidorino',
    searchable_by=['Nidorino', 'Stage 1', 'Nidorino'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    family_id=32,
    abilities=[
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title='Superpowered Horns',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
