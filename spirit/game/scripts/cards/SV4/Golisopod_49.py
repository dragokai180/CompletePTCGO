from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eac191ee-b87b-502e-8e12-db6fde5ad10e',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name',
    display_name='Golisopod',
    searchable_by=['Golisopod', 'Stage 1', 'Golisopod'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name',
    family_id=767,
    abilities=[
        Attack(
            title='Powerful Cross',
            game_text="This attack does 20 damage for each card in your opponent's hand.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
