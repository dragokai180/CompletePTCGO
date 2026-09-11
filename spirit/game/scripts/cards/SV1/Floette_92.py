from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='571755a0-8055-5fec-824c-8053397a00a1',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name',
    display_name='Floette',
    searchable_by=['Floette', 'Stage 1', 'Floette'],
    subtypes=['Stage 1'],
    collector_number=92,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    family_id=669,
    abilities=[
        Attack(
            title='Magical Leaf',
            game_text='Flip a coin. If heads, this attack does 30 more damage, and heal 30 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
