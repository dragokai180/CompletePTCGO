from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='429b93bc-63ea-5d83-9140-1fb891c23b82',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name',
    display_name='Lilligant',
    searchable_by=['Lilligant', 'Stage 1', 'Lilligant'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name',
    family_id=548,
    abilities=[
        Attack(
            title='Petal Blizzard',
            game_text="This attack does 10 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Petal Dance',
            game_text='Flip 3 coins. This attack does 40 damage for each heads. This Pokémon is now Confused.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
