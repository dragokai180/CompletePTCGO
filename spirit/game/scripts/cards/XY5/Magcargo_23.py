from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='152e6e47-ab61-5078-a710-c94181f3c2c0',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name',
    display_name='Magcargo',
    searchable_by=['Magcargo', 'Stage 1', 'Magcargo'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name',
    family_id=218,
    abilities=[
        Attack(
            title='Flame Burst',
            game_text="This attack does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
