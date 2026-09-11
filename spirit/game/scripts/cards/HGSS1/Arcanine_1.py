from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='71b60231-f4c6-5fb0-9d9a-99497d60e43c',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name',
    display_name='Arcanine',
    searchable_by=['Arcanine', 'Stage 1', 'Arcanine'],
    subtypes=['Stage 1'],
    collector_number=1,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    family_id=58,
    abilities=[
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Fire Mane',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
