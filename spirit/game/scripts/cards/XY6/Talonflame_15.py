from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be7330ed-de06-58f3-948e-3b052562e494',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name',
    display_name='Talonflame',
    searchable_by=['Talonflame', 'Stage 2', 'Talonflame'],
    subtypes=['Stage 2'],
    collector_number=15,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Grand Loop',
            game_text='Draw 3 cards. You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Brave Bird',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
