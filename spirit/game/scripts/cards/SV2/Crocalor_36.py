from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5c97b70b-e4cd-5fc8-a404-1eaf8060b051',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name',
    display_name='Crocalor',
    searchable_by=['Crocalor', 'Stage 1', 'Crocalor'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    family_id=909,
    abilities=[
        Attack(
            title='Steady Firebreathing',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title='Hyper Voice',
            cost={PokemonTypes.FIRE: 2},
            damage=70,
        ),
    ],
)
