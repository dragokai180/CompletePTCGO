from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a18bc024-0831-521a-ae14-01d2e686c3cf',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    display_name='Metapod',
    searchable_by=['Metapod', 'Stage 1', 'Metapod'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    family_id=10,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title='Shed Skin',
            game_text='Heal 40 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
