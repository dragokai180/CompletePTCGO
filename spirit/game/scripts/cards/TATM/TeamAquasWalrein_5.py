from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='711c6159-4183-54b0-abf8-e30ce5a1f467',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasWalrein.Name',
    display_name="Team Aqua's Walrein",
    searchable_by=["Team Aqua's Walrein", 'Stage 2', 'TeamAquasWalrein'],
    subtypes=['Stage 2'],
    collector_number=5,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSealeo.Name',
    family_id=363,
    abilities=[
        Attack(
            title='Power Blow',
            game_text='This attack does 30 damage times the amount of Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Dual Blizzard',
            game_text="Discard 2 Water Energy attached to this Pokémon. This attack does 80 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
