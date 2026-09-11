from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1d7c40a5-013f-5a21-8825-cfcd540ea519',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name',
    display_name='Staraptor',
    searchable_by=['Staraptor', 'Stage 2', 'Staraptor'],
    subtypes=['Stage 2'],
    collector_number=127,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name',
    family_id=396,
    abilities=[
        Attack(
            title='Cyclone Slash',
            game_text='Before doing damage, have your opponent switch his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Brave Bird',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
