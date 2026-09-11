from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c82b138d-80e4-5550-b53e-5fe5a562b823',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name',
    display_name='Crocalor',
    searchable_by=['Crocalor', 'Stage 1', 'Crocalor'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    family_id=909,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
