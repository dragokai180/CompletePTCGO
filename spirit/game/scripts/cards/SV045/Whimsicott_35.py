from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34dbefee-51e6-5b63-a913-7357fb1c5622',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name',
    display_name='Whimsicott',
    searchable_by=['Whimsicott', 'Stage 1', 'Whimsicott'],
    subtypes=['Stage 1'],
    collector_number=35,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    family_id=546,
    abilities=[
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
        ),
    ],
)
