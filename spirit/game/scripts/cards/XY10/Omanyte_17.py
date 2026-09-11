from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='036d3cca-9ce1-5ec3-b0b3-0f31f54abb61',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name',
    display_name='Omanyte',
    searchable_by=['Omanyte', 'Restored', 'Omanyte'],
    subtypes=['Restored'],
    collector_number=17,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.RESTORED,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.HelixFossilOmanyte.Name',
    family_id=138,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)
